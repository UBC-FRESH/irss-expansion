#!/usr/bin/env python3
"""Check that each public source URL still resolves.

The registry cites public IRSS, Silva21, DOI, and GitHub pages. This module performs
the source-refresh check: it reads every unique URL, follows redirects, and classifies
the response as ``ok``, ``blocked``, or ``broken``. It never edits the registry.

A publisher that returns 401, 403, 405, or 429 is treated as ``blocked``: the page may
exist but refuses an automated client. Those rows are reported and do not fail the run.
A network error, a redirect failure, or any other HTTP status is ``broken`` and fails
the run. The check is a dated snapshot, not a guarantee that the content was read.

Command-line usage::

    python scripts/refresh_sources.py
    python scripts/refresh_sources.py --json
    python scripts/refresh_sources.py --limit 10

Exit status is 0 when no source is broken. It is 1 when at least one source is broken.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from check_registry import load_registry

DEFAULT_REGISTRY: Path = Path(__file__).resolve().parent.parent / "registry" / "candidates.yaml"
USER_AGENT: str = "Mozilla/5.0 (compatible; irss-expansion-maintenance/0.1)"
BLOCKED_STATUSES: frozenset[int] = frozenset({401, 403, 405, 429})


@dataclass(frozen=True)
class SourceResult:
    """One source URL and the outcome of its refresh check.

    Attributes
    ----------
    url : str
        Public URL from the registry.
    candidates : tuple of str
        Candidate identifiers that cite the URL.
    status : int or None
        HTTP status, or ``None`` for a network or redirect failure.
    effective_url : str
        Final URL after redirects, when the client reached one.
    outcome : {"ok", "blocked", "broken"}
        Classification of the response.
    detail : str
        Error text, or an empty string.
    """

    url: str
    candidates: tuple[str, ...]
    status: int | None
    effective_url: str
    outcome: str
    detail: str


def collect_sources(data: dict[str, Any]) -> list[tuple[str, tuple[str, ...]]]:
    """Collect every unique source URL and the candidates that cite it.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed registry.

    Returns
    -------
    list of tuple of (str, tuple of str)
        Sorted ``(url, candidate_ids)`` pairs. A URL cited by several candidates is
        listed once.
    """
    cited: dict[str, list[str]] = {}
    for candidate in data.get("candidates", []):
        if not isinstance(candidate, dict):
            continue
        candidate_id = str(candidate.get("id", ""))
        for source in candidate.get("sources", []):
            if not isinstance(source, dict):
                continue
            url = source.get("url")
            if isinstance(url, str) and url.startswith(("http://", "https://")):
                cited.setdefault(url, [])
                if candidate_id not in cited[url]:
                    cited[url].append(candidate_id)
    return [(url, tuple(cited[url])) for url in sorted(cited)]


def classify(status: int | None) -> str:
    """Classify an HTTP status or a failed request.

    Parameters
    ----------
    status : int or None
        HTTP status, or ``None`` for a network or redirect failure.

    Returns
    -------
    {"ok", "blocked", "broken"}
        ``ok`` for 2xx, ``blocked`` for a publisher that refuses automated clients,
        and ``broken`` for everything else.
    """
    if status is None:
        return "broken"
    if 200 <= status < 300:
        return "ok"
    if status in BLOCKED_STATUSES:
        return "blocked"
    return "broken"


def probe_url(url: str, *, timeout: float = 20.0) -> tuple[int | None, str, str]:
    """Request one URL and return its status, effective URL, and error detail.

    Parameters
    ----------
    url : str
        URL to request.
    timeout : float, optional
        Seconds to allow the request to run.

    Returns
    -------
    tuple of (int or None, str, str)
        HTTP status or ``None``, effective URL after redirects, and error detail.
    """
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.geturl(), ""
    except urllib.error.HTTPError as exc:
        return exc.code, exc.url, str(exc)
    except (urllib.error.URLError, OSError) as exc:
        return None, url, f"{type(exc).__name__}: {exc}"


def refresh_sources(
    data: dict[str, Any],
    *,
    timeout: float = 20.0,
    limit: int | None = None,
) -> list[SourceResult]:
    """Check the public source URLs in a registry.

    Parameters
    ----------
    data : dict[str, Any]
        Parsed registry.
    timeout : float, optional
        Seconds to allow each request to run.
    limit : int or None, optional
        Maximum number of unique URLs to check. ``None`` checks all of them.

    Returns
    -------
    list of SourceResult
        One result per checked URL, in sorted URL order.
    """
    sources = collect_sources(data)
    if limit is not None:
        sources = sources[:limit]
    results: list[SourceResult] = []
    for url, candidates in sources:
        status, effective_url, detail = probe_url(url, timeout=timeout)
        results.append(
            SourceResult(
                url=url,
                candidates=candidates,
                status=status,
                effective_url=effective_url,
                outcome=classify(status),
                detail=detail,
            )
        )
    return results


def render_text(results: list[SourceResult]) -> str:
    """Render a source-refresh summary and the rows that need attention.

    Parameters
    ----------
    results : list of SourceResult
        Outcomes to summarize.

    Returns
    -------
    str
        Counts by outcome, followed by one line per blocked or broken source.
    """
    counts = Counter(result.outcome for result in results)
    lines = [
        f"checked: {len(results)} unique source URLs",
        f"ok: {counts['ok']}",
        f"blocked: {counts['blocked']}",
        f"broken: {counts['broken']}",
    ]
    for outcome in ("blocked", "broken"):
        rows = [result for result in results if result.outcome == outcome]
        if not rows:
            continue
        lines.extend(["", f"{outcome}:"])
        for result in rows:
            status = result.status if result.status is not None else "no status"
            lines.append(f"- {result.url} ({status}); cited by {', '.join(result.candidates)}")
            if result.detail:
                lines.append(f"  {result.detail}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Run the source-refresh check from the command line.

    Parameters
    ----------
    argv : list of str or None, optional
        Arguments to parse. ``None`` reads ``sys.argv``.

    Returns
    -------
    int
        ``0`` when no source is broken, and ``1`` otherwise.
    """
    parser = argparse.ArgumentParser(description="Check that public source URLs resolve.")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--limit", type=int, default=None, help="check at most this many URLs")
    parser.add_argument("--json", action="store_true", help="emit a JSON record")
    args = parser.parse_args(argv)
    try:
        data = load_registry(args.registry)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    results = refresh_sources(data, timeout=args.timeout, limit=args.limit)
    broken = [result for result in results if result.outcome == "broken"]
    if args.json:
        payload = {"ok": not broken, "results": [asdict(result) for result in results]}
        print(json.dumps(payload, indent=2))
    else:
        print(render_text(results))
        if broken:
            print(f"FAILED: {len(broken)} broken source(s)", file=sys.stderr)
        else:
            print("OK: no broken source URLs")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
