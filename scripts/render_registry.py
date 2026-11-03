"""Render the candidate registry as a browsable Markdown document.

Usage
-----
    python scripts/render_registry.py
    python scripts/render_registry.py --out docs/candidates.md
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Any

from check_registry import (
    build_ranking,
    load_registry,
    priority_score,
    validate_registry,
)

DEFAULT_REGISTRY = Path(__file__).resolve().parent.parent / "registry" / "candidates.yaml"
DEFAULT_OUTPUT = Path(__file__).resolve().parent.parent / "docs" / "candidates.md"
QUEUE_STATUSES = frozenset({"queued", "shortlisted", "candidate", "adopted"})


def _escape(text: str) -> str:
    """Escape pipe characters so a value survives a Markdown table cell."""
    return text.replace("|", "\\|").replace("\n", " ")


def _targets(candidate: dict[str, Any]) -> str:
    """Format the FRESH targets for a table cell."""
    return ", ".join(f"`{item}`" for item in candidate.get("fresh_targets", []))


def _source_list(candidate: dict[str, Any]) -> str:
    """Format a candidate's sources as Markdown bullet lines."""
    lines: list[str] = []
    for source in candidate.get("sources", []):
        ref = _escape(str(source.get("ref", "source")))
        url = str(source.get("url", ""))
        lines.append(f"- [{ref}]({url})" if url else f"- {ref}")
    return "\n".join(lines)


def render(data: dict[str, Any]) -> str:
    """Render the registry as a Markdown document.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed and validated registry.

    Returns
    -------
    str
        Markdown document.
    """
    meta = data.get("meta", {})
    candidates = data.get("candidates", [])
    ranking = build_ranking(data)
    workstreams: dict[str, str] = dict(meta.get("workstreams", {}))

    lines: list[str] = [
        "# Candidate register",
        "",
        f"_{meta.get('project', 'IRSS x Silva21 expansion mine')}_",
        "",
        f"Generated: {meta.get('generated', 'unknown')}. "
        f"Candidates: {len(candidates)}. "
        f"Scoring: `{meta.get('scoring', {}).get('formula', 'not stated')}`.",
        "",
        "This file is generated from `registry/candidates.yaml`. "
        "Edit the registry, then run `python scripts/render_registry.py`.",
        "",
        "## Top of the queue",
        "",
        "| Rank | ID | Wave | Score | Effort | Impact | Readiness | Risk | Candidate |",
        "| ---: | --- | ---: | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    active_ranking = [item for item in ranking if item.get("status") in QUEUE_STATUSES]
    for rank, item in enumerate(active_ranking[:15], start=1):
        lines.append(
            f"| {rank} | `{item['id']}` | {item['wave']} | {item['score']:.2f} | "
            f"{item['effort']} | {item['impact']} | {item['readiness']} | {item['risk']} | "
            f"{_escape(str(item['title']))} |"
        )

    lines.extend(["", "## By workstream", ""])
    by_workstream: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidates:
        by_workstream[str(candidate["workstream"])].append(candidate)

    for code in sorted(by_workstream):
        label = workstreams.get(code, code)
        lines.extend(
            [
                f"### {label} (`{code}`)",
                "",
                "| ID | Wave | Score | Effort | Targets | Candidate | First step |",
                "| --- | ---: | ---: | --- | --- | --- | --- |",
            ]
        )
        for item in sorted(
            by_workstream[code],
            key=lambda candidate: (
                int(candidate["wave"]),
                -priority_score(candidate),
                str(candidate["id"]),
            ),
        ):
            score = priority_score(item)
            title = _escape(str(item["title"]))
            first_step = _escape(str(item["first_step"]))
            lines.append(
                f"| `{item['id']}` | {item['wave']} | {score:.2f} | {item['effort']} | "
                f"{_targets(item)} | {title} | {first_step} |"
            )
        lines.append("")

    lines.extend(["## Candidate detail", ""])
    for item in sorted(candidates, key=lambda candidate: str(candidate["id"])):
        lines.extend(
            [
                f"### `{item['id']}` — {item['title']}",
                "",
                f"- **Workstream:** {workstreams.get(str(item['workstream']), item['workstream'])}",
                f"- **Status / wave:** {item['status']} / {item['wave']}",
                f"- **FRESH targets:** {_targets(item)}",
                f"- **Integration:** {item['integration']}",
                f"- **Effort / impact / readiness / risk:** "
                f"{item['effort']} / {item['impact']} / {item['readiness']} / {item['risk']}",
                f"- **Screening score:** {priority_score(item):.2f}",
                "",
                f"**What.** {item['what']}",
                "",
                f"**Gap.** {item['gap']}",
                "",
                f"**First step.** {item['first_step']}",
                "",
                f"**Risks.** {item['risks']}",
                "",
                *([f"**Resolution.** {item['resolution']}", ""] if item.get("resolution") else []),
                "**Sources.**",
                "",
                _source_list(item),
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    """Render the registry to Markdown.

    Parameters
    ----------
    argv : list[str] | None, optional
        Command-line arguments. ``None`` uses ``sys.argv``.

    Returns
    -------
    int
        ``0`` on success, ``1`` on validation failure.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)

    data = load_registry(args.registry)
    errors = validate_registry(data)
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(data), encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
