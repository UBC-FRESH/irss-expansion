"""Tests for the live issue and pull-request drift check."""

from __future__ import annotations

import datetime as dt
import json
import subprocess
from dataclasses import replace
from pathlib import Path

import pytest
import yaml

import check_issue_drift as cid
from check_maintenance import IssueCheck


def _check() -> IssueCheck:
    """Return a baseline open issue check."""
    return IssueCheck(
        candidate="INV-99",
        repo="UBC-FRESH/femic",
        number=1,
        kind="issue",
        expected="open",
        checked=dt.date(2026, 11, 3),
    )


def _schedule() -> dict[str, object]:
    """Return a minimal valid schedule with one issue check."""
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
        "reviews": [{"date": "2026-11-03", "kind": "baseline", "note": "notes/review.md"}],
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


def _runner(stdout: str = "{}", returncode: int = 0, stderr: str = "") -> cid.Runner:
    """Build a fake subprocess runner with fixed output."""

    def fake(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
        return subprocess.CompletedProcess([], returncode, stdout, stderr)

    return fake


def _write_schedule(tmp_path: Path) -> Path:
    """Write a valid schedule and the notes that it names."""
    (tmp_path / "notes" / "adr").mkdir(parents=True)
    for name in ("plan.md", "review.md", "adr/0001.md"):
        (tmp_path / "notes" / name).write_text("note\n", encoding="utf-8")
    path = tmp_path / "maintenance.yaml"
    path.write_text(yaml.safe_dump(_schedule()), encoding="utf-8")
    return path


def test_load_checks_returns_the_validated_records(tmp_path: Path) -> None:
    """A valid schedule yields its issue checks."""
    checks = cid.load_checks(_write_schedule(tmp_path))
    assert checks[0].candidate == "INV-99"


def test_load_checks_rejects_an_invalid_schedule(tmp_path: Path) -> None:
    """A schedule with a bad date is a value error."""
    path = tmp_path / "maintenance.yaml"
    path.write_text("meta: []\n", encoding="utf-8")
    with pytest.raises(ValueError, match="meta must be a mapping"):
        cid.load_checks(path)


def test_fetch_state_reads_an_open_issue() -> None:
    """An issue reads its state field."""
    result = cid.fetch_state(_check(), runner=_runner('{"state": "OPEN"}'))
    assert result.state == "open"
    assert result.detail == ""


def test_fetch_state_reads_a_merged_pull_request() -> None:
    """A pull request with a merge date is merged, whatever its state field says."""
    check = replace(_check(), kind="pr", expected="merged")
    result = cid.fetch_state(
        check, runner=_runner('{"state": "OPEN", "mergedAt": "2026-11-03T00:00:00Z"}')
    )
    assert result.state == "merged"


def test_fetch_state_reads_an_unmerged_pull_request() -> None:
    """A pull request with a null merge date reports its state."""
    check = replace(_check(), kind="pr", expected="open")
    result = cid.fetch_state(check, runner=_runner('{"state": "OPEN", "mergedAt": null}'))
    assert result.state == "open"


def test_fetch_state_reports_each_failure() -> None:
    """A failed command, a bad payload, and an unknown state all become details."""
    failed = cid.fetch_state(_check(), runner=_runner("", 2, "not found"))
    assert failed.state is None
    assert "exited 2" in failed.detail
    invalid = cid.fetch_state(_check(), runner=_runner("not json"))
    assert invalid.state is None
    assert "invalid JSON" in invalid.detail
    non_mapping = cid.fetch_state(_check(), runner=_runner("[1]"))
    assert non_mapping.state is None
    unknown = cid.fetch_state(_check(), runner=_runner('{"state": "DRAFT"}'))
    assert unknown.state is None
    assert "unexpected state" in unknown.detail


def test_fetch_state_reports_a_missing_gh() -> None:
    """An operating-system failure is a detail, not an exception."""

    def no_gh(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
        raise OSError("gh is not installed")

    result = cid.fetch_state(_check(), runner=no_gh)
    assert result.state is None
    assert "gh is not installed" in result.detail


def test_errors_from_results_report_mismatch_and_error() -> None:
    """A mismatch and a failed read become errors; a match does not."""
    matched = cid.DriftResult(_check(), "open", "")
    mismatch = cid.DriftResult(_check(), "closed", "")
    failed = cid.DriftResult(_check(), None, "gh failed")
    assert cid.errors_from_results([matched]) == []
    assert "expected open, live state is closed" in cid.errors_from_results([mismatch])[0]
    assert "gh failed" in cid.errors_from_results([failed])[0]


def test_check_issue_drift_reads_each_record() -> None:
    """The convenience wrapper reads the records and returns their errors."""
    assert cid.check_issue_drift([_check()], runner=_runner('{"state": "OPEN"}')) == []
    errors = cid.check_issue_drift([_check()], runner=_runner('{"state": "CLOSED"}'))
    assert "expected open" in errors[0]


def test_render_results_names_the_record_and_detail() -> None:
    """The plain report lists each record, its expectation, and any detail."""
    result = cid.DriftResult(_check(), None, "gh failed")
    text = cid.render_results([result])
    assert "UBC-FRESH/femic#1 (issue)" in text
    assert "ERROR" in text
    assert "gh failed" in text


def test_run_reads_the_schedule_and_returns_results(tmp_path: Path) -> None:
    """The run helper loads the schedule and reads every record."""
    results = cid.run(_write_schedule(tmp_path), runner=_runner('{"state": "OPEN"}'))
    assert results[0].state == "open"


def test_main_prints_json_and_text(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """The JSON and text paths report a green result."""
    path = _write_schedule(tmp_path)

    def fake_run(schedule: Path, **kwargs: object) -> list[cid.DriftResult]:
        return [cid.DriftResult(_check(), "open", "")]

    monkeypatch.setattr(cid, "run", fake_run)
    assert cid.main(["--schedule", str(path), "--json"]) == 0
    assert '"ok": true' in capsys.readouterr().out
    assert cid.main(["--schedule", str(path)]) == 0
    assert "OK: live target states match" in capsys.readouterr().out


def test_main_reports_an_invalid_schedule(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """An invalid schedule returns 1 and prints the error."""
    path = tmp_path / "maintenance.yaml"
    path.write_text("meta: []\n", encoding="utf-8")
    assert cid.main(["--schedule", str(path)]) == 1
    assert "error:" in capsys.readouterr().err


def test_main_reports_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """A live mismatch makes the command return 1."""
    path = _write_schedule(tmp_path)

    def fake_run(schedule: Path, **kwargs: object) -> list[cid.DriftResult]:
        return [cid.DriftResult(_check(), "closed", "")]

    monkeypatch.setattr(cid, "run", fake_run)
    assert cid.main(["--schedule", str(path)]) == 1
    assert "FAILED:" in capsys.readouterr().err


def test_main_uses_the_default_schedule(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """With no path argument, the default schedule is used."""
    monkeypatch.setattr(cid, "run", lambda path, **kwargs: [])
    assert cid.main([]) == 0
    assert "OK: live target states match" in capsys.readouterr().out


def test_json_payload_is_serializable() -> None:
    """The drift result fields are plain JSON values."""
    assert json.loads(json.dumps({"state": cid.DriftResult(_check(), "open", "").state}))
