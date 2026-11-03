#!/usr/bin/env python3
"""Check the maintenance schedule, the register, and the active-candidate records.

The registry is the queue. This module is the oracle for keeping it honest after the
release: it checks that the recorded cadence is arithmetically consistent, that the
generated register matches ``registry/candidates.yaml``, that every active candidate
names a recorded target record, and that the next review is not overdue when the
caller asks for a due-date check. It uses only the standard library and PyYAML.

Command-line usage::

    python scripts/check_maintenance.py
    python scripts/check_maintenance.py --due
    python scripts/check_maintenance.py --due --as-of 2027-02-02
    python scripts/check_maintenance.py --json

The default run is deterministic: it checks consistency but not the calendar. Pass
``--due`` for the monthly maintenance run, which fails when a review is overdue.

Exit status is 0 when no errors are found. Warnings are not part of this checker.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from check_registry import load_registry, validate_registry
from render_registry import render

DEFAULT_ROOT: Path = Path(__file__).resolve().parent.parent
DEFAULT_SCHEDULE: Path = DEFAULT_ROOT / "registry" / "maintenance.yaml"
DEFAULT_REGISTRY: Path = DEFAULT_ROOT / "registry" / "candidates.yaml"
DEFAULT_REGISTER: Path = DEFAULT_ROOT / "docs" / "candidates.md"

REPO_RE: re.Pattern[str] = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
CADENCE_FIELDS: tuple[str, ...] = (
    "review_cadence_days",
    "source_refresh_days",
    "issue_drift_days",
)
DATE_FIELDS: tuple[str, ...] = (
    "last_reviewed",
    "next_review_due",
    "last_source_refresh",
    "next_source_refresh_due",
    "last_issue_drift_check",
    "next_issue_drift_due",
)
CADENCE_PAIRS: tuple[tuple[str, str, str], ...] = (
    ("review_cadence_days", "last_reviewed", "next_review_due"),
    ("source_refresh_days", "last_source_refresh", "next_source_refresh_due"),
    ("issue_drift_days", "last_issue_drift_check", "next_issue_drift_due"),
)
RESOLUTION_STATUSES: frozenset[str] = frozenset({"complete", "adopted", "queued"})
ACTIVE_STATUSES: frozenset[str] = frozenset({"adopted", "queued"})
ISSUE_KINDS: frozenset[str] = frozenset({"issue", "pr"})
EXPECTED_STATES: frozenset[str] = frozenset({"open", "closed", "merged"})


@dataclass(frozen=True)
class IssueCheck:
    """One target issue or pull request that the drift check reads.

    Attributes
    ----------
    candidate : str
        Candidate identifier that the target record belongs to.
    repo : str
        Target repository in ``owner/name`` form.
    number : int
        Issue or pull-request number.
    kind : {"issue", "pr"}
        Whether the record is an issue or a pull request.
    expected : {"open", "closed", "merged"}
        State that the record must report at the audit date.
    checked : datetime.date
        Date of the recorded live check.
    """

    candidate: str
    repo: str
    number: int
    kind: str
    expected: str
    checked: dt.date


def load_schedule(path: Path) -> dict[str, Any]:
    """Load a maintenance schedule YAML file and return the parsed mapping.

    Parameters
    ----------
    path : pathlib.Path
        Path to the maintenance schedule.

    Returns
    -------
    dict[str, Any]
        Parsed schedule.

    Raises
    ------
    ValueError
        If the file cannot be read, is invalid YAML, or is not a mapping.
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


def _mapping(value: object, where: str, errors: list[str]) -> dict[str, Any]:
    """Return a mapping, or record an error and return an empty mapping.

    Parameters
    ----------
    value : object
        Value to inspect.
    where : str
        Field path used in the error message.
    errors : list of str
        Error list to append to.

    Returns
    -------
    dict[str, Any]
        The mapping, or an empty mapping when the value is not one.
    """
    if not isinstance(value, dict):
        errors.append(f"{where} must be a mapping")
        return {}
    return value


def _text(value: object, where: str, errors: list[str]) -> str:
    """Return a non-empty string, or record an error and return an empty string.

    Parameters
    ----------
    value : object
        Value to inspect.
    where : str
        Field path used in the error message.
    errors : list of str
        Error list to append to.

    Returns
    -------
    str
        The stripped text, or an empty string when the value is not non-empty text.
    """
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{where} must be a non-empty string")
        return ""
    return value.strip()


def _positive_int(value: object, where: str, errors: list[str]) -> int | None:
    """Return a positive integer, or record an error and return ``None``.

    Parameters
    ----------
    value : object
        Value to inspect.
    where : str
        Field path used in the error message.
    errors : list of str
        Error list to append to.

    Returns
    -------
    int or None
        The positive integer, or ``None`` when the value is invalid.
    """
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        errors.append(f"{where} must be a positive integer")
        return None
    return value


def _date(value: object, where: str, errors: list[str]) -> dt.date | None:
    """Parse an ISO date, or record an error and return ``None``.

    Parameters
    ----------
    value : object
        Value to inspect.
    where : str
        Field path used in the error message.
    errors : list of str
        Error list to append to.

    Returns
    -------
    datetime.date or None
        The parsed date, or ``None`` when the value is not an ISO date.
    """
    if not isinstance(value, str):
        errors.append(f"{where} must be an ISO date")
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        errors.append(f"{where} must be an ISO date, not {value!r}")
        return None


def parse_issue_checks(data: dict[str, Any]) -> list[IssueCheck]:
    """Read the issue checks from a validated schedule.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed schedule. Call :func:`validate_schedule` first.

    Returns
    -------
    list of IssueCheck
        One record per target issue or pull request.

    Raises
    ------
    ValueError
        If the issue-check entries do not have the validated shape.
    """
    raw_checks = data.get("issue_checks")
    if not isinstance(raw_checks, list):
        raise ValueError("issue_checks must be a list")
    checks: list[IssueCheck] = []
    for index, raw in enumerate(raw_checks):
        if not isinstance(raw, dict):
            raise ValueError(f"issue_checks[{index}] must be a mapping")
        checks.append(
            IssueCheck(
                candidate=str(raw["candidate"]),
                repo=str(raw["repo"]),
                number=int(raw["number"]),
                kind=str(raw["kind"]),
                expected=str(raw["expected"]),
                checked=dt.date.fromisoformat(str(raw["checked"])),
            )
        )
    return checks


def validate_schedule(data: dict[str, Any]) -> list[str]:
    """Validate the maintenance schedule and its arithmetic.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed schedule mapping.

    Returns
    -------
    list of str
        Human-readable errors. An empty list means the schedule is consistent.
    """
    errors: list[str] = []
    meta = _mapping(data.get("meta"), "meta", errors)
    if not meta:
        return errors

    cadence: dict[str, int] = {}
    for field in CADENCE_FIELDS:
        days = _positive_int(meta.get(field), f"meta.{field}", errors)
        if days is not None:
            cadence[field] = days
    dates: dict[str, dt.date] = {}
    for field in DATE_FIELDS:
        parsed_date = _date(meta.get(field), f"meta.{field}", errors)
        if parsed_date is not None:
            dates[field] = parsed_date
    _text(meta.get("owner"), "meta.owner", errors)
    _text(meta.get("procedure"), "meta.procedure", errors)
    _text(meta.get("decision"), "meta.decision", errors)

    for cadence_field, last_field, next_field in CADENCE_PAIRS:
        if cadence_field in cadence and last_field in dates and next_field in dates:
            expected = dates[last_field] + dt.timedelta(days=cadence[cadence_field])
            if dates[next_field] != expected:
                errors.append(
                    f"meta.{next_field} must be {expected.isoformat()}, "
                    f"the {cadence_field} after meta.{last_field}"
                )

    reviews = data.get("reviews")
    if not isinstance(reviews, list) or not reviews:
        errors.append("reviews must be a non-empty list")
    else:
        review_dates: list[dt.date] = []
        for index, raw in enumerate(reviews):
            review = _mapping(raw, f"reviews[{index}]", errors)
            if not review:
                continue
            review_date = _date(review.get("date"), f"reviews[{index}].date", errors)
            if review_date is not None:
                review_dates.append(review_date)
            _text(review.get("kind"), f"reviews[{index}].kind", errors)
            _text(review.get("note"), f"reviews[{index}].note", errors)
        if (
            review_dates
            and "last_reviewed" in dates
            and max(review_dates) != dates["last_reviewed"]
        ):
            errors.append("meta.last_reviewed must equal the latest review date")

    checks = data.get("issue_checks")
    if not isinstance(checks, list) or not checks:
        errors.append("issue_checks must be a non-empty list")
    else:
        for index, raw in enumerate(checks):
            where = f"issue_checks[{index}]"
            raw_check = _mapping(raw, where, errors)
            if not raw_check:
                continue
            _text(raw_check.get("candidate"), f"{where}.candidate", errors)
            repo = _text(raw_check.get("repo"), f"{where}.repo", errors)
            if repo and not REPO_RE.match(repo):
                errors.append(f"{where}.repo must look like 'owner/name'")
            _positive_int(raw_check.get("number"), f"{where}.number", errors)
            kind = _text(raw_check.get("kind"), f"{where}.kind", errors)
            expected_state = _text(raw_check.get("expected"), f"{where}.expected", errors)
            if kind and kind not in ISSUE_KINDS:
                errors.append(f"{where}.kind must be one of issue, pr")
            if expected_state and expected_state not in EXPECTED_STATES:
                errors.append(f"{where}.expected must be one of open, closed, merged")
            if kind == "issue" and expected_state == "merged":
                errors.append(f"{where}: an issue cannot have expected state merged")
            _date(raw_check.get("checked"), f"{where}.checked", errors)
    return errors


def check_files(root: Path, schedule: dict[str, Any]) -> list[str]:
    """Check that the procedure, decision, and review notes named by the schedule exist.

    Parameters
    ----------
    root : pathlib.Path
        Repository root that the paths are relative to.
    schedule : dict[str, Any]
        Parsed and validated schedule.

    Returns
    -------
    list of str
        One error per missing path. An empty list means every named file exists.
    """
    errors: list[str] = []
    meta = schedule.get("meta", {})
    if not isinstance(meta, dict):
        return ["meta must be a mapping"]
    for field in ("procedure", "decision"):
        value = meta.get(field)
        if isinstance(value, str) and value and not (root / value).is_file():
            errors.append(f"meta.{field} names a missing file: {value}")
    reviews = schedule.get("reviews", [])
    if isinstance(reviews, list):
        for index, review in enumerate(reviews):
            if not isinstance(review, dict):
                continue
            note = review.get("note")
            if isinstance(note, str) and note and not (root / note).is_file():
                errors.append(f"reviews[{index}].note names a missing file: {note}")
    return errors


def check_due(schedule: dict[str, Any], as_of: dt.date) -> list[str]:
    """Report every recurring check whose next date has passed.

    Parameters
    ----------
    schedule : dict[str, Any]
        Parsed schedule. Call :func:`validate_schedule` first.
    as_of : datetime.date
        Date to compare with the next-due dates.

    Returns
    -------
    list of str
        One error per overdue check, plus an error when the audit date precedes the
        recorded review.
    """
    meta = schedule.get("meta", {})
    if not isinstance(meta, dict):
        return ["meta must be a mapping"]
    errors: list[str] = []
    last_reviewed = _date(meta.get("last_reviewed"), "meta.last_reviewed", errors)
    if last_reviewed is not None and as_of < last_reviewed:
        errors.append(
            f"--as-of {as_of.isoformat()} precedes meta.last_reviewed {last_reviewed.isoformat()}"
        )
    for _, _, next_field in CADENCE_PAIRS:
        next_date = _date(meta.get(next_field), f"meta.{next_field}", errors)
        if next_date is not None and as_of > next_date:
            errors.append(f"meta.{next_field} is overdue since {next_date.isoformat()}")
    return errors


def check_register(
    registry_path: Path,
    register_path: Path,
) -> list[str]:
    """Check that the generated register matches the registry.

    Parameters
    ----------
    registry_path : pathlib.Path
        Path to ``registry/candidates.yaml``.
    register_path : pathlib.Path
        Path to the generated ``docs/candidates.md``.

    Returns
    -------
    list of str
        Validation errors, a read error, a missing-register error, or a staleness
        error. An empty list means the register is current.
    """
    try:
        data = load_registry(registry_path)
    except ValueError as exc:
        return [str(exc)]
    errors = validate_registry(data)
    if errors:
        return [f"registry: {error}" for error in errors]
    try:
        current = register_path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"cannot read {register_path}: {exc}"]
    expected = render(data)
    if current != expected:
        return [
            f"{register_path} is stale; run python scripts/render_registry.py after "
            "editing the registry"
        ]
    return []


def check_active_records(data: dict[str, Any], schedule: dict[str, Any]) -> list[str]:
    """Check the resolution and target-record requirements for the active queue.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed and validated registry.
    schedule : dict[str, Any]
        Parsed and validated schedule.

    Returns
    -------
    list of str
        Missing resolutions, missing issue checks, unknown candidates, and a completed
        candidate that still has an open target record.
    """
    errors: list[str] = []
    candidates = {
        str(row["id"]): row
        for row in data.get("candidates", [])
        if isinstance(row, dict) and "id" in row
    }
    for candidate_id, row in candidates.items():
        status = str(row.get("status", ""))
        resolution = str(row.get("resolution", "")).strip()
        if status in RESOLUTION_STATUSES and not resolution:
            errors.append(f"{candidate_id} is {status} but has no resolution")

    try:
        checks = parse_issue_checks(schedule)
    except (KeyError, TypeError, ValueError) as exc:
        return [*errors, f"issue_checks: {exc}"]

    checked_candidates = {check.candidate for check in checks}
    for candidate_id, row in candidates.items():
        if str(row.get("status", "")) in ACTIVE_STATUSES and candidate_id not in checked_candidates:
            errors.append(f"{candidate_id} is active but has no issue check")
    for check in checks:
        candidate_row = candidates.get(check.candidate)
        if candidate_row is None:
            errors.append(f"issue check names unknown candidate {check.candidate}")
            continue
        status = str(candidate_row.get("status", ""))
        if status == "complete" and check.expected == "open":
            errors.append(
                f"{check.candidate} is complete but {check.repo}#{check.number} "
                "is expected to be open"
            )
    return errors


def run(root: Path, *, as_of: dt.date | None = None) -> list[str]:
    """Run every maintenance check against a repository root.

    Parameters
    ----------
    root : pathlib.Path
        Repository root to check.
    as_of : datetime.date or None, optional
        Date for the due-date check. ``None`` skips that check.

    Returns
    -------
    list of str
        Every consistency error found. An empty list means the checks passed.
    """
    schedule_path = root / "registry" / "maintenance.yaml"
    try:
        schedule = load_schedule(schedule_path)
    except ValueError as exc:
        return [str(exc)]
    errors = validate_schedule(schedule)
    if errors:
        return errors
    errors.extend(check_files(root, schedule))
    errors.extend(
        check_register(root / "registry" / "candidates.yaml", root / "docs" / "candidates.md")
    )
    try:
        data = load_registry(root / "registry" / "candidates.yaml")
    except ValueError as exc:
        return [*errors, str(exc)]
    errors.extend(check_active_records(data, schedule))
    if as_of is not None:
        errors.extend(check_due(schedule, as_of))
    return errors


def main(argv: list[str] | None = None) -> int:
    """Run the maintenance checks from the command line.

    Parameters
    ----------
    argv : list of str or None, optional
        Arguments to parse. ``None`` reads ``sys.argv``.

    Returns
    -------
    int
        ``0`` when every check passes, and ``1`` otherwise.

    Raises
    ------
    SystemExit
        When the argument parser rejects the arguments.
    """
    parser = argparse.ArgumentParser(description="Check the maintenance surfaces.")
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=DEFAULT_ROOT,
        help="repository root to check (default: the checkout that contains this script)",
    )
    parser.add_argument(
        "--due",
        action="store_true",
        help="also fail when a review date has passed",
    )
    parser.add_argument(
        "--as-of",
        type=dt.date.fromisoformat,
        default=None,
        metavar="YYYY-MM-DD",
        help="date for the due check, with --due",
    )
    parser.add_argument("--json", action="store_true", help="emit a JSON record")
    args = parser.parse_args(argv)
    as_of = args.as_of
    if args.due and as_of is None:
        as_of = dt.date.today()
    if not args.due and as_of is not None:
        parser.error("--as-of requires --due")
    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    errors = run(root, as_of=as_of)
    if args.json:
        payload = {
            "ok": not errors,
            "as_of": as_of.isoformat() if as_of else None,
            "errors": errors,
        }
        print(json.dumps(payload, indent=2))
    else:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        if errors:
            print(f"FAILED: {len(errors)} maintenance error(s)", file=sys.stderr)
        else:
            print("OK: maintenance surfaces are consistent")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
