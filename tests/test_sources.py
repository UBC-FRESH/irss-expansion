"""Tests for the public source-refresh check."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from email.message import Message
from pathlib import Path
from typing import Any

import pytest
import yaml

import refresh_sources as rs


class FakeResponse:
    """A minimal stand-in for the response object returned by ``urlopen``."""

    def __init__(self, status: int, url: str) -> None:
        self.status = status
        self._url = url

    def __enter__(self) -> FakeResponse:
        """Enter the response context."""
        return self

    def __exit__(self, *args: object) -> None:
        """Leave the response context."""
        return None

    def geturl(self) -> str:
        """Return the effective URL."""
        return self._url


def _registry() -> dict[str, Any]:
    """Return a minimal registry with one candidate and two cited URLs."""
    return {
        "candidates": [
            {
                "id": "INV-99",
                "sources": [
                    {"ref": "First", "url": "https://example.org/a"},
                    {"ref": "Second", "url": "https://example.org/b"},
                    {"ref": "Duplicate", "url": "https://example.org/a"},
                    {"ref": "Text only"},
                ],
            },
            {
                "id": "INV-98",
                "sources": [{"ref": "Third", "url": "https://example.org/a"}],
            },
            "not-a-candidate",
        ]
    }


def test_collect_sources_deduplicates_and_names_candidates() -> None:
    """A URL is checked once and keeps every candidate that cites it."""
    sources = rs.collect_sources(_registry())
    assert len(sources) == 2
    url, candidates = sources[0]
    assert url == "https://example.org/a"
    assert candidates == ("INV-99", "INV-98")


def test_classify_separates_ok_blocked_and_broken() -> None:
    """Status classes follow the documented rule."""
    assert rs.classify(200) == "ok"
    assert rs.classify(202) == "ok"
    assert rs.classify(403) == "blocked"
    assert rs.classify(429) == "blocked"
    assert rs.classify(404) == "broken"
    assert rs.classify(500) == "broken"
    assert rs.classify(None) == "broken"


def test_probe_url_returns_the_status_and_effective_url(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A successful request returns its status and final URL."""
    monkeypatch.setattr(
        urllib.request, "urlopen", lambda request, timeout: FakeResponse(200, "https://x.test/")
    )
    assert rs.probe_url("https://example.org/a") == (200, "https://x.test/", "")


def test_probe_url_returns_an_http_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """An HTTP error keeps its status and URL."""

    def fail(request: object, timeout: float) -> FakeResponse:
        raise urllib.error.HTTPError("https://example.org/a", 403, "Forbidden", Message(), None)

    monkeypatch.setattr(urllib.request, "urlopen", fail)
    status, url, detail = rs.probe_url("https://example.org/a")
    assert status == 403
    assert url == "https://example.org/a"
    assert detail


def test_probe_url_returns_a_network_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """A URL error is a broken source with no status."""

    def fail(request: object, timeout: float) -> FakeResponse:
        raise urllib.error.URLError("no route")

    monkeypatch.setattr(urllib.request, "urlopen", fail)
    status, url, detail = rs.probe_url("https://example.org/a")
    assert status is None
    assert url == "https://example.org/a"
    assert "URLError" in detail


def test_refresh_sources_honors_the_limit_and_classification(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The refresh returns one result per checked URL and respects the limit."""
    monkeypatch.setattr(
        urllib.request, "urlopen", lambda request, timeout: FakeResponse(200, "https://x.test/")
    )
    results = rs.refresh_sources(_registry(), limit=1)
    assert len(results) == 1
    assert results[0].outcome == "ok"
    assert results[0].candidates == ("INV-99", "INV-98")


def test_render_text_summarizes_and_lists_attention_rows() -> None:
    """The report counts outcomes and names blocked and broken rows."""
    results = [
        rs.SourceResult("https://ok.test", ("INV-1",), 200, "https://ok.test", "ok", ""),
        rs.SourceResult("https://blocked.test", ("INV-2",), 403, "", "blocked", "Forbidden"),
        rs.SourceResult("https://broken.test", ("INV-3",), None, "", "broken", "URLError"),
    ]
    text = rs.render_text(results)
    assert "checked: 3 unique source URLs" in text
    assert "ok: 1" in text
    assert "blocked: 1" in text
    assert "broken: 1" in text
    assert "https://blocked.test (403); cited by INV-2" in text
    assert "https://broken.test (no status); cited by INV-3" in text


def test_render_text_omits_empty_sections() -> None:
    """A clean run has no attention section."""
    results = [rs.SourceResult("https://ok.test", ("INV-1",), 200, "", "ok", "")]
    assert "\nblocked:\n" not in rs.render_text(results)


def _write_registry(tmp_path: Path) -> Path:
    """Write the minimal registry to a temporary file."""
    path = tmp_path / "registry.yaml"
    path.write_text(yaml.safe_dump(_registry()), encoding="utf-8")
    return path


def test_main_reports_a_missing_registry(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """An unreadable registry returns 1."""
    assert rs.main(["--registry", str(tmp_path / "missing.yaml")]) == 1
    assert "error:" in capsys.readouterr().err


def test_main_prints_json_for_a_clean_run(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """A 2xx response yields a green JSON record."""
    monkeypatch.setattr(
        urllib.request, "urlopen", lambda request, timeout: FakeResponse(200, "https://x.test/")
    )
    assert rs.main(["--registry", str(_write_registry(tmp_path)), "--json", "--limit", "1"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["ok"] is True
    assert len(payload["results"]) == 1


def test_main_prints_text_for_a_blocked_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """A blocked publisher is reported but does not fail the run."""

    def fail(request: object, timeout: float) -> FakeResponse:
        raise urllib.error.HTTPError("https://example.org/a", 403, "Forbidden", Message(), None)

    monkeypatch.setattr(urllib.request, "urlopen", fail)
    assert rs.main(["--registry", str(_write_registry(tmp_path))]) == 0
    output = capsys.readouterr().out
    assert "blocked: 2" in output
    assert "OK: no broken source URLs" in output


def test_main_fails_on_a_broken_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """A network failure returns 1 and names the broken count."""

    def fail(request: object, timeout: float) -> FakeResponse:
        raise urllib.error.URLError("no route")

    monkeypatch.setattr(urllib.request, "urlopen", fail)
    assert rs.main(["--registry", str(_write_registry(tmp_path))]) == 1
    assert "FAILED: 2 broken source(s)" in capsys.readouterr().err
