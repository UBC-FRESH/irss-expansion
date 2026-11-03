"""Validate and rank the IRSS/Silva21 expansion candidate registry.

The registry is the queue. This checker is its oracle: it fails on missing
fields, unknown values, duplicate identifiers, malformed sources, and
out-of-range scores. Run it before committing a registry change.

Usage
-----
    python scripts/check_registry.py
    python scripts/check_registry.py --file registry/candidates.yaml
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ID_PATTERN = re.compile(r"^[A-Z]{2,5}-\d{2}$")
EFFORT_POINTS: dict[str, int] = {"S": 1, "M": 2, "L": 3, "XL": 5}
REQUIRED_CANDIDATE_KEYS: tuple[str, ...] = (
    "id",
    "title",
    "workstream",
    "status",
    "wave",
    "sources",
    "what",
    "fresh_targets",
    "integration",
    "gap",
    "first_step",
    "effort",
    "impact",
    "readiness",
    "risk",
    "risks",
)
REQUIRED_SOURCE_KEYS: tuple[str, ...] = ("ref", "url")


def load_registry(path: Path) -> dict[str, Any]:
    """Load a registry YAML file and return the parsed mapping.

    Parameters
    ----------
    path : pathlib.Path
        Path to the registry YAML file.

    Returns
    -------
    dict[str, Any]
        Parsed registry.

    Raises
    ------
    ValueError
        If the file is not a mapping or cannot be parsed.
    """
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except OSError as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a mapping at the top level")
    return data


def _require_mapping(value: object, where: str, errors: list[str]) -> dict[str, Any]:
    """Return ``value`` if it is a mapping, otherwise record an error."""
    if not isinstance(value, dict):
        errors.append(f"{where} must be a mapping")
        return {}
    return value


def _require_string(value: object, where: str, errors: list[str]) -> str:
    """Return ``value`` if it is a non-empty string, otherwise record an error."""
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{where} must be a non-empty string")
        return ""
    return value.strip()


def _require_int(value: object, where: str, low: int, high: int, errors: list[str]) -> int:
    """Return ``value`` if it is an integer in range, otherwise record an error."""
    if isinstance(value, bool) or not isinstance(value, int):
        errors.append(f"{where} must be an integer")
        return low
    if value < low or value > high:
        errors.append(f"{where} must be between {low} and {high}")
    return value


def priority_score(candidate: dict[str, Any]) -> float:
    """Compute the screening priority score for one candidate.

    Parameters
    ----------
    candidate : dict[str, Any]
        A candidate mapping with numeric ``impact``, ``readiness`` and ``risk``
        fields and a valid ``effort`` code.

    Returns
    -------
    float
        ``(impact * readiness) / (effort_points * risk)`` rounded to two
        decimals. Returns ``0.0`` for an invalid effort code or non-positive
        risk so that validation, not scoring, reports the problem.
    """
    effort = str(candidate.get("effort", ""))
    points = EFFORT_POINTS.get(effort)
    impact = candidate.get("impact")
    readiness = candidate.get("readiness")
    risk = candidate.get("risk")
    if not isinstance(impact, int) or not isinstance(readiness, int):
        return 0.0
    if not isinstance(risk, int) or risk <= 0 or points is None:
        return 0.0
    return round((impact * readiness) / (points * risk), 2)


def _find_dependency_cycle(graph: dict[str, list[str]]) -> list[str] | None:
    """Return one dependency cycle as a path, or ``None`` when acyclic."""
    visited: set[str] = set()
    path: list[str] = []

    def visit(node: str) -> list[str] | None:
        if node in path:
            start = path.index(node)
            return [*path[start:], node]
        if node in visited:
            return None
        path.append(node)
        for neighbour in graph.get(node, []):
            cycle = visit(neighbour)
            if cycle:
                return cycle
        path.pop()
        visited.add(node)
        return None

    for node in graph:
        cycle = visit(node)
        if cycle:
            return cycle
    return None


def validate_registry(data: dict[str, Any]) -> list[str]:
    """Validate a parsed registry and return a list of human-readable errors.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed registry mapping.

    Returns
    -------
    list[str]
        Validation errors. An empty list means the registry is valid.
    """
    errors: list[str] = []
    meta = _require_mapping(data.get("meta"), "meta", errors)
    if meta:
        workstreams = meta.get("workstreams")
        if not isinstance(workstreams, dict) or not workstreams:
            errors.append("meta.workstreams must be a non-empty mapping")
        else:
            for key, label in workstreams.items():
                if not isinstance(key, str) or not ID_PATTERN.match(f"{key}-00"):
                    errors.append(f"meta.workstreams key {key!r} is not a short code")
                _require_string(label, f"meta.workstreams.{key}", errors)
        status_values = meta.get("status_values")
        if not isinstance(status_values, list) or not status_values:
            errors.append("meta.status_values must be a non-empty list")
        target_values = meta.get("target_values")
        if not isinstance(target_values, list) or not target_values:
            errors.append("meta.target_values must be a non-empty list")

    raw_candidates = data.get("candidates")
    if not isinstance(raw_candidates, list) or not raw_candidates:
        errors.append("candidates must be a non-empty list")
        return errors

    allowed_status = {str(item) for item in meta.get("status_values", [])}
    allowed_targets = {str(item) for item in meta.get("target_values", [])}
    allowed_workstreams = {str(item) for item in meta.get("workstreams", {})}
    seen_ids: set[str] = set()
    dependency_map: dict[str, list[str]] = {}

    for index, raw in enumerate(raw_candidates):
        where = f"candidates[{index}]"
        candidate = _require_mapping(raw, where, errors)
        if not candidate:
            continue
        missing = [key for key in REQUIRED_CANDIDATE_KEYS if key not in candidate]
        if missing:
            errors.append(f"{where} is missing required keys: {', '.join(missing)}")
            continue

        candidate_id = _require_string(candidate["id"], f"{where}.id", errors)
        if candidate_id and not ID_PATTERN.match(candidate_id):
            errors.append(f"{where}.id {candidate_id!r} must look like 'INV-01'")
        if candidate_id in seen_ids:
            errors.append(f"{where}.id {candidate_id!r} is duplicated")
        seen_ids.add(candidate_id)

        _require_string(candidate["title"], f"{where}.title", errors)
        workstream = _require_string(candidate["workstream"], f"{where}.workstream", errors)
        if workstream and allowed_workstreams and workstream not in allowed_workstreams:
            errors.append(f"{where}.workstream {workstream!r} is not declared in meta")
        status = _require_string(candidate["status"], f"{where}.status", errors)
        if status and allowed_status and status not in allowed_status:
            errors.append(f"{where}.status {status!r} is not allowed")
        _require_int(candidate["wave"], f"{where}.wave", 0, 3, errors)

        sources = candidate["sources"]
        if not isinstance(sources, list) or not sources:
            errors.append(f"{where}.sources must be a non-empty list")
        else:
            for source_index, source in enumerate(sources):
                source_where = f"{where}.sources[{source_index}]"
                source_map = _require_mapping(source, source_where, errors)
                for key in REQUIRED_SOURCE_KEYS:
                    if key not in source_map:
                        errors.append(f"{source_where} is missing {key!r}")
                if "ref" in source_map:
                    _require_string(source_map["ref"], f"{source_where}.ref", errors)
                if "url" in source_map:
                    url = _require_string(source_map["url"], f"{source_where}.url", errors)
                    if url and not url.startswith(("http://", "https://")):
                        errors.append(f"{source_where}.url must start with http:// or https://")

        for key in ("what", "gap", "first_step", "risks"):
            _require_string(candidate[key], f"{where}.{key}", errors)

        targets = candidate["fresh_targets"]
        if not isinstance(targets, list) or not targets:
            errors.append(f"{where}.fresh_targets must be a non-empty list")
        else:
            unknown = [str(item) for item in targets if str(item) not in allowed_targets]
            if unknown:
                errors.append(f"{where}.fresh_targets has unknown targets: {', '.join(unknown)}")

        _require_string(candidate["integration"], f"{where}.integration", errors)
        effort = _require_string(candidate["effort"], f"{where}.effort", errors)
        if effort and effort not in EFFORT_POINTS:
            errors.append(f"{where}.effort {effort!r} must be one of S, M, L, XL")
        _require_int(candidate["impact"], f"{where}.impact", 1, 5, errors)
        _require_int(candidate["readiness"], f"{where}.readiness", 1, 5, errors)
        _require_int(candidate["risk"], f"{where}.risk", 1, 5, errors)

        dependencies = candidate.get("dependencies", [])
        if not isinstance(dependencies, list):
            errors.append(f"{where}.dependencies must be a list")
        else:
            clean_dependencies: list[str] = []
            for dependency in dependencies:
                dependency_text = _require_string(dependency, f"{where}.dependencies", errors)
                if not dependency_text:
                    continue
                if not ID_PATTERN.match(dependency_text):
                    errors.append(f"{where}.dependencies contains invalid id {dependency_text!r}")
                elif dependency_text == candidate_id:
                    errors.append(f"{where}.dependencies may not name itself")
                else:
                    clean_dependencies.append(dependency_text)
            dependency_map[candidate_id] = clean_dependencies

        held_status = candidate["status"] in {"deferred", "rejected", "candidate"}
        if candidate["wave"] == 0 and not held_status:
            errors.append(f"{where}: wave 0 candidates must be deferred, rejected, or candidate")

    known_ids = set(dependency_map)
    for candidate_id, dependencies in dependency_map.items():
        for dependency in dependencies:
            if dependency not in known_ids:
                errors.append(f"{candidate_id}.dependencies names unknown candidate {dependency!r}")

    cycle = _find_dependency_cycle(dependency_map)
    if cycle:
        errors.append(f"dependency cycle: {' -> '.join(cycle)}")

    return errors


def build_ranking(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return candidates sorted by descending priority score.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed registry mapping.

    Returns
    -------
    list[dict[str, Any]]
        Candidate mappings with a derived ``score`` field, highest score first.
    """
    ranking: list[dict[str, Any]] = []
    for candidate in data.get("candidates", []):
        if not isinstance(candidate, dict):
            continue
        enriched = dict(candidate)
        enriched["score"] = priority_score(candidate)
        ranking.append(enriched)
    return sorted(
        ranking,
        key=lambda item: (-float(item["score"]), int(item.get("wave", 9)), str(item["id"])),
    )


def render_ranking(data: dict[str, Any]) -> str:
    """Render a compact plain-text ranking and summary.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed registry mapping.

    Returns
    -------
    str
        Human-readable report.
    """
    ranking = build_ranking(data)
    lines = ["id      wave score effort impact ready risk  title"]
    for item in ranking:
        lines.append(
            f"{item['id']!s:7} {item['wave']:>4} {item['score']:>5.2f} "
            f"{item['effort']!s:>6} {item['impact']:>6} {item['readiness']:>5} "
            f"{item['risk']:>4}  {item['title']}"
        )
    candidates = data.get("candidates", [])
    lines.append("")
    lines.append(f"total: {len(candidates)}")
    lines.append(f"by wave: {dict(sorted(Counter(int(c['wave']) for c in candidates).items()))}")
    lines.append(
        f"by status: {dict(sorted(Counter(str(c['status']) for c in candidates).items()))}"
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Run the registry checker.

    Parameters
    ----------
    argv : list[str] | None, optional
        Command-line arguments. ``None`` uses ``sys.argv``.

    Returns
    -------
    int
        ``0`` when the registry is valid, ``1`` otherwise.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--file",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "registry" / "candidates.yaml",
        help="Path to the candidate registry YAML.",
    )
    parser.add_argument("--json", action="store_true", help="Emit the ranking as JSON.")
    args = parser.parse_args(argv)

    try:
        data = load_registry(args.file)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    errors = validate_registry(data)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} registry error(s)", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(build_ranking(data), indent=2))
    else:
        print(render_ranking(data))
        print("OK: registry is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
