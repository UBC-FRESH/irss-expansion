"""Tests for the candidate registry validator and ranking."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest
import yaml

from check_registry import (
    build_ranking,
    load_registry,
    main,
    priority_score,
    render_ranking,
    validate_registry,
)
from render_registry import main as render_main
from render_registry import render

REGISTRY_PATH = Path(__file__).resolve().parent.parent / "registry" / "candidates.yaml"


def _valid_candidate() -> dict[str, Any]:
    """Return a minimal valid candidate for mutation in tests."""
    return {
        "id": "INV-99",
        "title": "A test candidate",
        "workstream": "INV",
        "status": "candidate",
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
    }


def _valid_registry() -> dict[str, Any]:
    """Return a minimal valid registry for mutation in tests."""
    return {
        "meta": {
            "workstreams": {"INV": "Inventory"},
            "status_values": ["queued", "shortlisted", "candidate", "deferred", "rejected"],
            "target_values": ["femic", "ws4", "cross"],
        },
        "candidates": [_valid_candidate()],
    }


def test_real_registry_is_valid() -> None:
    """The checked-in registry passes validation."""
    data = load_registry(REGISTRY_PATH)
    assert validate_registry(data) == []


def test_duplicate_id_is_rejected() -> None:
    """Two candidates may not share an identifier."""
    data = _valid_registry()
    second = deepcopy(data["candidates"][0])
    data["candidates"].append(second)
    errors = validate_registry(data)
    assert any("duplicated" in error for error in errors)


def test_unknown_target_is_rejected() -> None:
    """Targets must be declared in meta."""
    data = _valid_registry()
    data["candidates"][0]["fresh_targets"] = ["not-a-repo"]
    errors = validate_registry(data)
    assert any("unknown targets" in error for error in errors)


def test_wave_zero_requires_deferred_status() -> None:
    """A held candidate must be deferred, rejected, or still a candidate."""
    data = _valid_registry()
    data["candidates"][0]["wave"] = 0
    data["candidates"][0]["status"] = "queued"
    errors = validate_registry(data)
    assert any("wave 0" in error for error in errors)


def test_malformed_source_url_is_rejected() -> None:
    """Source URLs must be HTTP(S)."""
    data = _valid_registry()
    data["candidates"][0]["sources"][0]["url"] = "ftp://example.org/source"
    errors = validate_registry(data)
    assert any("must start with http" in error for error in errors)


def test_unknown_dependency_is_rejected() -> None:
    """Dependencies must name a registered candidate."""
    data = _valid_registry()
    data["candidates"][0]["dependencies"] = ["INV-77"]
    errors = validate_registry(data)
    assert any("unknown candidate" in error for error in errors)


def test_dependency_cycle_is_rejected() -> None:
    """A dependency cycle is a registry error."""
    data = _valid_registry()
    second = deepcopy(data["candidates"][0])
    second["id"] = "INV-98"
    data["candidates"][0]["dependencies"] = ["INV-98"]
    second["dependencies"] = ["INV-99"]
    data["candidates"].append(second)
    errors = validate_registry(data)
    assert any("dependency cycle" in error for error in errors)


def test_priority_score_uses_effort_points() -> None:
    """A small effort raises the score and an XL effort lowers it."""
    small = _valid_candidate() | {"effort": "S", "impact": 5, "readiness": 4, "risk": 2}
    large = _valid_candidate() | {"effort": "XL", "impact": 5, "readiness": 4, "risk": 2}
    assert priority_score(small) == 10.0
    assert priority_score(large) == 2.0


def test_priority_score_handles_invalid_risk() -> None:
    """A zero risk cannot produce a division error."""
    candidate = _valid_candidate() | {"risk": 0}
    assert priority_score(candidate) == 0.0


def test_ranking_is_sorted_by_score() -> None:
    """The ranking report puts the highest score first."""
    data = _valid_registry()
    second = deepcopy(data["candidates"][0])
    second["id"] = "INV-98"
    second["effort"] = "XL"
    data["candidates"].append(second)
    ranking = build_ranking(data)
    assert ranking[0]["id"] == "INV-99"
    assert ranking[0]["score"] >= ranking[1]["score"]


def test_render_ranking_includes_summary() -> None:
    """The rendered report names every candidate and the total."""
    data = _valid_registry()
    report = render_ranking(data)
    assert "INV-99" in report
    assert "total: 1" in report


def test_load_registry_rejects_non_mapping(tmp_path: Path) -> None:
    """A top-level list is not a registry."""
    path = tmp_path / "bad.yaml"
    path.write_text("- not\n- a\n- registry\n", encoding="utf-8")
    with pytest.raises(ValueError, match="mapping"):
        load_registry(path)


def test_render_top_queue_excludes_completed_candidates() -> None:
    """Completed work stays in detail but not in the active top queue."""
    data = _valid_registry()
    data["candidates"][0]["status"] = "complete"
    rendered = render(data)
    queue = rendered.split("## Top of the queue", 1)[1].split("## By workstream", 1)[0]
    assert "INV-99" not in queue
    assert "INV-99" in rendered


def test_load_registry_reports_a_missing_file(tmp_path: Path) -> None:
    """A missing file becomes a validation error that names the path."""
    with pytest.raises(ValueError, match="cannot read"):
        load_registry(tmp_path / "missing.yaml")


def test_load_registry_reports_invalid_yaml(tmp_path: Path) -> None:
    """Malformed YAML is reported instead of escaping as a parser error."""
    path = tmp_path / "broken.yaml"
    path.write_text("candidates: [\n", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid YAML"):
        load_registry(path)


def test_validation_requires_meta_mapping() -> None:
    """A metadata block that is not a mapping is rejected."""
    data = _valid_registry()
    data["meta"] = []
    errors = validate_registry(data)
    assert "meta must be a mapping" in errors


def test_validation_requires_workstreams_statuses_and_targets() -> None:
    """Each metadata list must be present and non-empty."""
    data = _valid_registry()
    data["meta"] = {
        "workstreams": [],
        "status_values": [],
        "target_values": [],
    }
    errors = validate_registry(data)
    assert "meta.workstreams must be a non-empty mapping" in errors
    assert "meta.status_values must be a non-empty list" in errors
    assert "meta.target_values must be a non-empty list" in errors


def test_validation_checks_workstream_keys_and_labels() -> None:
    """A workstream key must be a short code and its label must be text."""
    data = _valid_registry()
    data["meta"]["workstreams"] = {"bad-key": ""}
    errors = validate_registry(data)
    assert any("is not a short code" in error for error in errors)
    assert "meta.workstreams.bad-key must be a non-empty string" in errors


def test_validation_requires_candidates() -> None:
    """An empty candidate list is reported and stops the candidate checks."""
    data = _valid_registry()
    data["candidates"] = []
    assert validate_registry(data) == ["candidates must be a non-empty list"]


def test_validation_rejects_a_non_mapping_candidate() -> None:
    """A candidate row must be a mapping."""
    data = _valid_registry()
    data["candidates"].append("not a mapping")
    errors = validate_registry(data)
    assert "candidates[1] must be a mapping" in errors


def test_validation_reports_missing_candidate_keys() -> None:
    """A candidate that omits required keys is named, not guessed at."""
    data = _valid_registry()
    del data["candidates"][0]["title"]
    errors = validate_registry(data)
    assert any("is missing required keys: title" in error for error in errors)


def test_validation_rejects_a_malformed_id() -> None:
    """A candidate id must use the workstream-code grammar."""
    data = _valid_registry()
    data["candidates"][0]["id"] = "inv-99"
    errors = validate_registry(data)
    assert any("must look like 'INV-01'" in error for error in errors)


def test_validation_rejects_unknown_workstream_and_status() -> None:
    """A workstream and status must be declared in the metadata."""
    data = _valid_registry()
    data["candidates"][0]["workstream"] = "ZZZ"
    data["candidates"][0]["status"] = "unknown"
    errors = validate_registry(data)
    assert any("is not declared in meta" in error for error in errors)
    assert any("is not allowed" in error for error in errors)


def test_validation_rejects_bad_sources() -> None:
    """Sources must be a non-empty list of mappings with a ref and an HTTP URL."""
    data = _valid_registry()
    data["candidates"][0]["sources"] = []
    assert "candidates[0].sources must be a non-empty list" in validate_registry(data)

    data = _valid_registry()
    data["candidates"][0]["sources"] = ["not a mapping"]
    errors = validate_registry(data)
    assert "candidates[0].sources[0] must be a mapping" in errors
    assert "candidates[0].sources[0] is missing 'ref'" in errors
    assert "candidates[0].sources[0] is missing 'url'" in errors

    data = _valid_registry()
    data["candidates"][0]["sources"] = [{"ref": "", "url": "ftp://example.org"}]
    errors = validate_registry(data)
    assert "candidates[0].sources[0].ref must be a non-empty string" in errors
    assert any("must start with http" in error for error in errors)


def test_validation_rejects_bad_targets_effort_and_scores() -> None:
    """Targets, effort, and integer scores are range-checked."""
    data = _valid_registry()
    candidate = data["candidates"][0]
    candidate["fresh_targets"] = []
    candidate["effort"] = "XXL"
    candidate["impact"] = True
    candidate["readiness"] = 9
    candidate["risk"] = 0
    errors = validate_registry(data)
    assert "candidates[0].fresh_targets must be a non-empty list" in errors
    assert "candidates[0].effort 'XXL' must be one of S, M, L, XL" in errors
    assert "candidates[0].impact must be an integer" in errors
    assert "candidates[0].readiness must be between 1 and 5" in errors
    assert "candidates[0].risk must be between 1 and 5" in errors


def test_validation_rejects_bad_dependencies() -> None:
    """A dependency list must contain known, non-self, well-formed ids."""
    data = _valid_registry()
    data["candidates"][0]["dependencies"] = "INV-01"
    assert "candidates[0].dependencies must be a list" in validate_registry(data)

    data = _valid_registry()
    data["candidates"][0]["id"] = "INV-99"
    data["candidates"][0]["dependencies"] = ["", "bad", "INV-99", "INV-77"]
    errors = validate_registry(data)
    assert "candidates[0].dependencies must be a non-empty string" in errors
    assert any("contains invalid id 'bad'" in error for error in errors)
    assert any("may not name itself" in error for error in errors)
    assert any("names unknown candidate 'INV-77'" in error for error in errors)


def test_priority_score_rejects_non_integer_inputs() -> None:
    """A missing or non-integer impact or readiness scores zero."""
    assert priority_score(_valid_candidate() | {"impact": "high"}) == 0.0
    assert priority_score(_valid_candidate() | {"readiness": None}) == 0.0


def test_build_ranking_skips_rows_that_are_not_mappings() -> None:
    """Only mappings can be ranked."""
    assert build_ranking({"candidates": ["not a mapping"]}) == []


def test_main_prints_the_ranking_for_a_valid_registry(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """The default output is the ranking plus the valid verdict."""
    path = tmp_path / "registry.yaml"
    path.write_text(yaml.safe_dump(_valid_registry()), encoding="utf-8")
    assert main(["--file", str(path)]) == 0
    output = capsys.readouterr().out
    assert "total: 1" in output
    assert "OK: registry is valid" in output


def test_main_prints_json_when_asked(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The JSON flag emits a machine-readable ranking."""
    path = tmp_path / "registry.yaml"
    path.write_text(yaml.safe_dump(_valid_registry()), encoding="utf-8")
    assert main(["--file", str(path), "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload[0]["id"] == "INV-99"
    assert payload[0]["score"] == 3.0


def test_main_reports_a_load_error(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """A missing registry file returns 1 and prints the error."""
    assert main(["--file", str(tmp_path / "missing.yaml")]) == 1
    assert "error: cannot read" in capsys.readouterr().err


def test_main_reports_validation_errors(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """An invalid registry returns 1 and names the error count."""
    path = tmp_path / "registry.yaml"
    data = _valid_registry()
    data["candidates"] = []
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    assert main(["--file", str(path)]) == 1
    error = capsys.readouterr().err
    assert "error: candidates must be a non-empty list" in error
    assert "FAILED: 1 registry error(s)" in error


def test_render_main_writes_markdown(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The renderer writes the generated register to the requested path."""
    registry = tmp_path / "registry.yaml"
    registry.write_text(yaml.safe_dump(_valid_registry()), encoding="utf-8")
    output = tmp_path / "docs" / "candidates.md"
    assert render_main(["--registry", str(registry), "--out", str(output)]) == 0
    assert "# Candidate register" in output.read_text(encoding="utf-8")
    assert f"wrote {output}" in capsys.readouterr().out


def test_render_main_reports_validation_errors(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """The renderer refuses an invalid registry and does not write output."""
    registry = tmp_path / "registry.yaml"
    data = _valid_registry()
    data["candidates"] = []
    registry.write_text(yaml.safe_dump(data), encoding="utf-8")
    output = tmp_path / "candidates.md"
    assert render_main(["--registry", str(registry), "--out", str(output)]) == 1
    assert "error: candidates must be a non-empty list" in capsys.readouterr().out
    assert not output.exists()


def test_render_includes_a_resolution_and_a_source_without_a_url() -> None:
    """A resolved candidate carries its resolution and a source may be text-only."""
    data = _valid_registry()
    data["candidates"][0]["resolution"] = "Merged as #1."
    data["candidates"][0]["sources"] = [{"ref": "A text source"}]
    rendered = render(data)
    assert "**Resolution.** Merged as #1." in rendered
    assert "- A text source" in rendered
