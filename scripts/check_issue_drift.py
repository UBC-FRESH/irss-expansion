#!/usr/bin/env python3
"""Compare the recorded active target records with their live GitHub state.

``registry/maintenance.yaml`` names the issues and pull requests that keep the active
queue honest. This module reads those records with ``gh`` and fails when the live state
differs from the expected state. It is a dated snapshot: run it on the recorded cadence
and write the result down. It does not edit any target repository.

Command-line usage::

    python scripts/check_issue_drift.py
    python scripts/check_issue_drift.py --json

Exit status is 0 when every live state matches. It is 1 for a mismatch or a failed
``gh`` call.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

from check_maintenance import (
    DEFAULT_SCHEDULE,
    IssueCheck,
    load_schedule,
    parse_issue_checks,
    validate_schedule,
)

Runner = Callable[..., subprocess.CompletedProcess[str]]


@dataclass(frozen=True)
class DriftResult:
    """The outcome of one live issue or pull-request read.

    Attributes
    ----------
    check : IssueCheck
        The recorded target record.
    state : str or None
        Live normalized state, or ``None`` when the read failed.
    detail : str
        Error text from ``gh``, or an empty string on success.
    """

    check: IssueCheck
    state: str | None
    detail: str


def load_checks(path: Path) -> list[IssueCheck]:
    """Load and validate the issue checks from a maintenance schedule.

    Parameters
    ----------
    path : pathlib.Path
        Path to ``registry/maintenance.yaml``.

    Returns
    -------
    list of IssueCheck
        The validated records to read.

    Raises
    ------
    ValueError
        If the schedule is unreadable or invalid.
    """
    schedule = load_schedule(path)
    errors = validate_schedule(schedule)
    if errors:
        raise ValueError("; ".join(errors))
    return parse_issue_checks(schedule)


def fetch_state(
    check: IssueCheck,
    *,
    runner: Runner = subprocess.run,
    timeout: float = 30.0,
) -> DriftResult:
    """Read one target record's live state with ``gh``.

    Parameters
    ----------
    check : IssueCheck
        Record to read.
    runner : callable, optional
        Subprocess runner, defaulting to :func:`subprocess.run`. Tests inject a fake.
    timeout : float, optional
        Seconds to allow the command to run.

    Returns
    -------
    DriftResult
        The normalized state, or a failure detail when the command or parse fails.
    """
    fields = "state,mergedAt" if check.kind == "pr" else "state"
    command = ("gh", check.kind, "view", str(check.number), "--repo", check.repo, "--json", fields)
    try:
        completed = runner(
            list(command), capture_output=True, text=True, check=False, timeout=timeout
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return DriftResult(check, None, f"gh failed: {exc}")
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip()
        return DriftResult(check, None, f"gh exited {completed.returncode}: {detail}")
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        return DriftResult(check, None, f"gh returned invalid JSON: {exc}")
    if not isinstance(payload, dict):
        return DriftResult(check, None, "gh returned a non-mapping payload")
    if check.kind == "pr" and payload.get("mergedAt"):
        return DriftResult(check, "merged", "")
    state = str(payload.get("state", "")).lower()
    if state in {"open", "closed"}:
        return DriftResult(check, state, "")
    return DriftResult(check, None, f"unexpected state {state!r}")


def errors_from_results(results: Sequence[DriftResult]) -> list[str]:
    """Turn drift results into the errors that a caller should report.

    Parameters
    ----------
    results : sequence of DriftResult
        Outcomes from :func:`fetch_state`.

    Returns
    -------
    list of str
        One error per failed read or state mismatch. An empty list means every live
        state matches its expectation.
    """
    errors: list[str] = []
    for result in results:
        check = result.check
        label = f"{check.candidate} {check.repo}#{check.number}"
        if result.state is None:
            errors.append(f"{label}: {result.detail}")
        elif result.state != check.expected:
            errors.append(f"{label}: expected {check.expected}, live state is {result.state}")
    return errors


def check_issue_drift(
    checks: Sequence[IssueCheck],
    *,
    runner: Runner = subprocess.run,
    timeout: float = 30.0,
) -> list[str]:
    """Compare every recorded target record with its live state.

    Parameters
    ----------
    checks : sequence of IssueCheck
        Records to read.
    runner : callable, optional
        Subprocess runner used by :func:`fetch_state`.
    timeout : float, optional
        Seconds to allow each command to run.

    Returns
    -------
    list of str
        One error per mismatch or failed read. An empty list means the live state
        matches every recorded expectation.
    """
    results = [fetch_state(check, runner=runner, timeout=timeout) for check in checks]
    return errors_from_results(results)


def render_results(results: Sequence[DriftResult]) -> str:
    """Render one line per recorded target record.

    Parameters
    ----------
    results : sequence of DriftResult
        Outcomes from :func:`fetch_state`.

    Returns
    -------
    str
        A plain-text report with the candidate, repository, expected, and live state.
    """
    lines = [f"{'CANDIDATE':<10}{'RECORD':<28}{'EXPECTED':<10}LIVE"]
    for result in results:
        check = result.check
        record = f"{check.repo}#{check.number} ({check.kind})"
        live = result.state if result.state is not None else "ERROR"
        lines.append(f"{check.candidate:<10}{record:<28}{check.expected:<10}{live}")
        if result.detail:
            lines.append(f"  {result.detail}")
    return "\n".join(lines)


def run(path: Path, *, runner: Runner = subprocess.run, timeout: float = 30.0) -> list[DriftResult]:
    """Read every recorded target record and return the outcomes.

    Parameters
    ----------
    path : pathlib.Path
        Path to the maintenance schedule.
    runner : callable, optional
        Subprocess runner used for each ``gh`` call.
    timeout : float, optional
        Seconds to allow each command to run.

    Returns
    -------
    list of DriftResult
        One outcome per recorded target record.

    Raises
    ------
    ValueError
        If the schedule is unreadable or invalid.
    """
    checks = load_checks(path)
    return [fetch_state(check, runner=runner, timeout=timeout) for check in checks]


def main(argv: list[str] | None = None) -> int:
    """Run the issue-drift check from the command line.

    Parameters
    ----------
    argv : list of str or None, optional
        Arguments to parse. ``None`` reads ``sys.argv``.

    Returns
    -------
    int
        ``0`` when every live state matches, and ``1`` otherwise.
    """
    parser = argparse.ArgumentParser(description="Check live issue and pull-request drift.")
    parser.add_argument("--schedule", type=Path, default=DEFAULT_SCHEDULE)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--json", action="store_true", help="emit a JSON record")
    args = parser.parse_args(argv)
    try:
        results = run(args.schedule, timeout=args.timeout)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    errors = errors_from_results(results)
    if args.json:
        payload = {
            "ok": not errors,
            "results": [
                {
                    "candidate": result.check.candidate,
                    "repo": result.check.repo,
                    "number": result.check.number,
                    "kind": result.check.kind,
                    "expected": result.check.expected,
                    "state": result.state,
                    "detail": result.detail,
                }
                for result in results
            ],
            "errors": errors,
        }
        print(json.dumps(payload, indent=2))
    else:
        print(render_results(results))
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        if errors:
            print(f"FAILED: {len(errors)} drift error(s)", file=sys.stderr)
        else:
            print("OK: live target states match the recorded expectations")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
