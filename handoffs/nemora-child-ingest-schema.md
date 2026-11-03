Task identifier: P5.3
Parent phase issue: #7
Status: planned
Branch: `feature/p5-uncertainty-sampling`
Related planning: `ROADMAP.md` (Phase 5)
Source register: candidate `DATA-04`

## Goal

Publish a shared tidy inventory ingest schema and migrate one FAIB/FIA/HPS path
to it, with byte-level regression fixtures.

## Scope

- Define the tidy schema for inventory releases (plots, trees, species, units,
  provenance).
- Add a validator and a migration note.
- Migrate one ingest path to the schema.
- Keep the existing output byte-identical on the fixture.
- Add a nightly check or extend the existing one.

## Out of scope

- Migrating every source at once.
- A new downloader or a new data source.
- A database or a data portal.
- Changing downstream model inputs beyond the schema boundary.

## Subtasks

- [ ] Define the schema fields, units, and provenance.
- [ ] Add the validator and failure tests.
- [ ] Migrate one ingest path.
- [ ] Add byte-level regression fixtures.
- [ ] Extend the nightly check.
- [ ] Document the migration and the remaining paths.
- [ ] Add a changelog entry.

## Acceptance criteria

- The migrated path reproduces the existing output on the fixture.
- The schema rejects a missing key and an unknown unit.
- The nightly ingest still passes.
- The migration note names the remaining paths and the order.
- The tests fail if the schema version or provenance is dropped.

## Verification

```bash
python -m pytest
NEMORA_RUN_FAIB_INTEGRATION=1 NEMORA_RUN_FIA_INTEGRATION=1 \
  pytest tests/test_ingest_faib.py tests/test_ingest_fia.py
ruff check src tests
mypy src
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Schema and validator.
- Migrated path and fixtures.
- Migration note and changelog entry.

## Risks

- **Upstream drift.** FAIB/FIA/HPS schemas change; the nightly job is the
  early-warning system.
- **Breaking scripts.** Keep a compatibility shim for one release.
- **Licensing.** Do not commit source data; commit only fixtures that are
  public-safe.

## Public sources

- Nemora ingest: <https://github.com/UBC-FRESH/nemora>
- FEMIC data preparation: <https://github.com/UBC-FRESH/femic>
