"""Tests for the maintenance schedule, register freshness, and active records."""

from __future__ import annotations

import datetime as dt
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest
import yaml

import check_maintenance as cm
from render_registry import render


def _candidate() -> dict[str, Any]:
    """Return a minimal valid candidate for registry and active-record tests."""
    return {
        "id": "INV-99",
        "title": "A test candidate",
        "workstream": "INV",
        "status": "queued",
        "wave": 1,
        "sources": [{"ref": "A source", "url": "https://example.org/source"}],
        "what": "A test candidate description.",
        "fresh_targets": ["femic"],
        "integration": "algorithm",
        "gap": "A test gap.",
        "first_step": "A test first step.",
        "effort": "M",
        "impact": 4,
        "readiness": 3,
        "risk": 2,
        "risks": "A test risk.",
        "resolution": "Tracked as example/repo#1.",
    }


def _registry() -> dict[str, Any]:
    """Return a minimal valid registry."""
    return {
        "meta": {
            "workstreams": {"INV": "Inventory"},
            "status_values": ["queued", "adopted", "complete", "deferred", "rejected"],
            "target_values": ["femic", "ws4", "cross"],
        },
        "candidates": [_candidate()],
    }


def _schedule() -> dict[str, Any]:
    """Return a consistent baseline maintenance schedule."""
    return {
        "meta": {
            "owner": "The maintainers",
            "procedure": "notes/plan.md",
            "decision": "notes/adr/0001.md",
            "review_cadence_days": 90,
            "source_refresh_days": 180,
            "issue_drift_days": 30,
            "last_reviewed": "2026-11-03",
            "next_review_due": "2027-02-01",
            "last_source_refresh": "2026-11-03",
            "next_source_refresh_due": "2027-05-02",
            "last_issue_drift_check": "2026-11-03",
            "next_issue_drift_due": "2026-12-03",
        },
        "reviews": [
            {
                "date": "2026-11-03",
                "kind": "baseline",
                "note": "notes/review.md",
            }
        ],
        "issue_checks": [
            {
                "candidate": "INV-99",
                "repo": "UBC-FRESH/femic",
                "number": 1,
                "kind": "issue",
                "expected": "open",
                "checked": "2026-11-03",
            }
        ],
    }


def _write_root(tmp_path: Path) -> Path:
    """Write a repository root that the maintenance checks can read."""
    (tmp_path / "registry").mkdir()
    (tmp_path / "docs").mkdir()
    (tmp_path / "notes" / "adr").mkdir(parents=True)
    (tmp_path / "notes" / "plan.md").write_text("plan\n", encoding="utf-8")
    (tmp_path / "notes" / "review.md").write_text("review\n", encoding="utf-8")
    (tmp_path / "notes" / "adr" / "0001.md").write_text("decision\n", encoding="utf-8")
    data = _registry()
    registry = tmp_path / "registry" / "candidates.yaml"
    registry.write_text(yaml.safe_dump(data), encoding="utf-8")
    (tmp_path / "docs" / "candidates.md").write_text(render(data), encoding="utf-8")
    (tmp_path / "registry" / "maintenance.yaml").write_text(
        yaml.safe_dump(_schedule()), encoding="utf-8"
    )
    return tmp_path


def test_validate_schedule_accepts_the_baseline() -> None:
    """The baseline schedule is arithmetically consistent."""
    assert cm.validate_schedule(_schedule()) == []


def test_validate_schedule_rejects_a_non_mapping_meta() -> None:
    """Metadata must be a mapping, and that stops the remaining checks."""
    assert cm.validate_schedule({"meta": []}) == ["meta must be a mapping"]


def test_validate_schedule_reports_bad_values_and_dates() -> None:
    """Cadence, date, text, review, and issue-check defects are all reported."""
    data = _schedule()
    data["meta"] = {
        "owner": "",
        "procedure": "",
        "decision": "",
        "review_cadence_days": 0,
        "source_refresh_days": "soon",
        "issue_drift_days": True,
        "last_reviewed": "not-a-date",
        "next_review_due": 3,
        "last_source_refresh": None,
        "next_source_refresh_due": "2027-13-01",
        "last_issue_drift_check": "2026-11-03",
        "next_issue_drift_due": "2026-12-03",
    }
    data["reviews"] = []
    data["issue_checks"] = "not-a-list"
    errors = cm.validate_schedule(data)
    assert "meta.review_cadence_days must be a positive integer" in errors
    assert "meta.source_refresh_days must be a positive integer" in errors
    assert "meta.issue_drift_days must be a positive integer" in errors
    assert "meta.last_reviewed must be an ISO date, not 'not-a-date'" in errors
    assert "meta.next_review_due must be an ISO date" in errors
    assert "reviews must be a non-empty list" in errors
    assert "issue_checks must be a non-empty list" in errors


def test_validate_schedule_checks_date_arithmetic() -> None:
    """A next date that is not the cadence after the last date is an error."""
    data = _schedule()
    data["meta"]["next_review_due"] = "2027-02-02"
    assert "meta.next_review_due must be 2027-02-01" in cm.validate_schedule(data)[0]


def test_validate_schedule_checks_the_latest_review_and_entries() -> None:
    """Review entries and issue-check entries are shape-checked."""
    data = _schedule()
    data["reviews"] = [
        {"date": "2026-11-02", "kind": "", "note": ""},
        "not-a-mapping",
    ]
    data["meta"]["last_reviewed"] = "2026-11-03"
    data["issue_checks"] = [
        {
            "candidate": "",
            "repo": "not a repo",
            "number": 0,
            "kind": "card",
            "expected": "unknown",
            "checked": "today",
        },
        {
            "candidate": "INV-99",
            "repo": "UBC-FRESH/femic",
            "number": 2,
            "kind": "issue",
            "expected": "merged",
            "checked": "2026-11-03",
        },
        "not-a-mapping",
    ]
    errors = cm.validate_schedule(data)
    assert "meta.last_reviewed must equal the latest review date" in errors
    assert "reviews[0].kind must be a non-empty string" in errors
    assert "reviews[1] must be a mapping" in errors
    assert "issue_checks[0].repo must look like 'owner/name'" in errors
    assert "issue_checks[0].number must be a positive integer" in errors
    assert "issue_checks[0].kind must be one of issue, pr" in errors
    assert "issue_checks[0].expected must be one of open, closed, merged" in errors
    assert "issue_checks[1]: an issue cannot have expected state merged" in errors
    assert "issue_checks[0].checked must be an ISO date, not 'today'" in errors
    assert "issue_checks[2] must be a mapping" in errors


def test_parse_issue_checks_rejects_bad_shapes() -> None:
    """Parsing requires a list of mappings with every key."""
    with pytest.raises(ValueError, match="must be a list"):
        cm.parse_issue_checks({"issue_checks": "bad"})
    with pytest.raises(ValueError, match="must be a mapping"):
        cm.parse_issue_checks({"issue_checks": ["bad"]})
    with pytest.raises(KeyError):
        cm.parse_issue_checks({"issue_checks": [{}]})
    checks = cm.parse_issue_checks(_schedule())
    assert checks[0].candidate == "INV-99"
    assert checks[0].checked == dt.date(2026, 11, 3)


def test_check_due_reports_overdue_and_early_dates() -> None:
    """A review is overdue after its next date, and the audit cannot precede the review."""
    assert cm.check_due(_schedule(), dt.date(2026, 12, 3)) == []
    errors = cm.check_due(_schedule(), dt.date(2027, 2, 2))
    assert "meta.next_review_due is overdue since 2027-02-01" in errors
    assert "meta.next_issue_drift_due is overdue since 2026-12-03" in errors
    assert cm.check_due({"meta": []}, dt.date(2026, 11, 3)) == ["meta must be a mapping"]
    early = cm.check_due(_schedule(), dt.date(2026, 11, 2))
    assert "--as-of 2026-11-02 precedes meta.last_reviewed 2026-11-03" in early


def test_check_files_reports_missing_procedure_decision_and_review() -> None:
    """Every file named by the schedule must exist under the root."""
    data = _schedule()
    errors = cm.check_files(Path("/nonexistent"), data)
    assert len(errors) == 3
    assert cm.check_files(Path("/nonexistent"), {"meta": []}) == ["meta must be a mapping"]
    relaxed = _schedule()
    relaxed["reviews"] = ["not-a-mapping"]
    assert len(cm.check_files(Path("/nonexistent"), relaxed)) == 2


def test_check_register_detects_a_stale_or_missing_document(tmp_path: Path) -> None:
    """The generated register must match the registry byte for byte."""
    root = _write_root(tmp_path)
    registry = root / "registry" / "candidates.yaml"
    register = root / "docs" / "candidates.md"
    assert cm.check_register(registry, register) == []
    register.write_text("# stale\n", encoding="utf-8")
    assert "is stale" in cm.check_register(registry, register)[0]
    register.unlink()
    assert "cannot read" in cm.check_register(registry, register)[0]
    registry.write_text("candidates: []\n", encoding="utf-8")
    assert cm.check_register(registry, register)[0].startswith("registry:")
    registry.unlink()
    assert "cannot read" in cm.check_register(registry, register)[0]


def test_check_active_records_accepts_the_baseline() -> None:
    """A queued candidate with a resolution and one issue check is consistent."""
    assert cm.check_active_records(_registry(), _schedule()) == []


def test_check_active_records_reports_missing_and_unknown_records() -> None:
    """Resolution, issue-check coverage, and known candidates are enforced."""
    data = _registry()
    data["candidates"][0]["resolution"] = ""
    errors = cm.check_active_records(data, _schedule())
    assert "INV-99 is queued but has no resolution" in errors

    data = _registry()
    data["candidates"].append({"id": "INV-98", "status": "adopted", "resolution": "x"})
    data["candidates"].append({"id": "INV-97", "status": "complete", "resolution": "x"})
    schedule = _schedule()
    schedule["issue_checks"] = [
        {
            "candidate": "MISSING",
            "repo": "UBC-FRESH/femic",
            "number": 1,
            "kind": "issue",
            "expected": "open",
            "checked": "2026-11-03",
        },
        {
            "candidate": "INV-97",
            "repo": "UBC-FRESH/femic",
            "number": 2,
            "kind": "issue",
            "expected": "open",
            "checked": "2026-11-03",
        },
    ]
    errors = cm.check_active_records(data, schedule)
    assert "INV-98 is active but has no issue check" in errors
    assert "issue check names unknown candidate MISSING" in errors
    assert "INV-97 is complete but UBC-FRESH/femic#2 is expected to be open" in errors


def test_check_active_records_reports_unparseable_issue_checks() -> None:
    """A malformed issue-check entry becomes an error rather than an exception."""
    errors = cm.check_active_records(_registry(), {"issue_checks": [{}]})
    assert any(error.startswith("issue_checks:") for error in errors)


def test_run_and_main_cover_json_due_and_failure(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """The command runs the deterministic checks, the due check, and the JSON path."""
    root = _write_root(tmp_path)
    assert cm.run(root) == []
    assert cm.main([str(root), "--json"]) == 0
    assert '"ok": true' in capsys.readouterr().out
    assert cm.main([str(root), "--due", "--as-of", "2027-02-02"]) == 1
    assert "FAILED:" in capsys.readouterr().err
    assert cm.main([str(root)]) == 0
    assert "OK: maintenance surfaces are consistent" in capsys.readouterr().out


def test_run_reports_a_missing_or_invalid_schedule(tmp_path: Path) -> None:
    """A missing schedule and an invalid schedule are reported, not raised."""
    assert "cannot read" in cm.run(tmp_path)[0]
    (tmp_path / "registry").mkdir()
    (tmp_path / "registry" / "maintenance.yaml").write_text("meta: []\n", encoding="utf-8")
    assert cm.run(tmp_path) == ["meta must be a mapping"]


def test_run_reports_an_invalid_registry(tmp_path: Path) -> None:
    """A schedule may be valid while the registry is not."""
    root = _write_root(tmp_path)
    (root / "registry" / "candidates.yaml").write_text("candidates: []\n", encoding="utf-8")
    errors = cm.run(root)
    assert any(error.startswith("registry:") for error in errors)


def test_main_rejects_an_as_of_without_due(tmp_path: Path) -> None:
    """The date flag is meaningful only with the due check."""
    with pytest.raises(SystemExit) as excinfo:
        cm.main([str(tmp_path), "--as-of", "2026-11-03"])
    assert excinfo.value.code == 2


def test_main_rejects_a_missing_root(tmp_path: Path) -> None:
    """A root that is not a directory is a usage error."""
    with pytest.raises(SystemExit) as excinfo:
        cm.main([str(tmp_path / "missing")])
    assert excinfo.value.code == 2


def test_load_schedule_reports_a_missing_or_invalid_file(tmp_path: Path) -> None:
    """A missing file and invalid YAML are value errors."""
    with pytest.raises(ValueError, match="cannot read"):
        cm.load_schedule(tmp_path / "missing.yaml")
    broken = tmp_path / "broken.yaml"
    broken.write_text("meta: [\n", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid YAML"):
        cm.load_schedule(broken)
    not_mapping = tmp_path / "list.yaml"
    not_mapping.write_text("- one\n", encoding="utf-8")
    with pytest.raises(ValueError, match="mapping"):
        cm.load_schedule(not_mapping)


def test_validate_schedule_accepts_a_pr_check_with_merged_state() -> None:
    """A pull request may expect merged; only an issue may not."""
    data = _schedule()
    data["issue_checks"][0]["kind"] = "pr"
    data["issue_checks"][0]["expected"] = "merged"
    assert cm.validate_schedule(data) == []
    assert cm.validate_schedule(deepcopy(data)) == []
