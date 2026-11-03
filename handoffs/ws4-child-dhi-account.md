Task identifier: P54.1
Parent phase issue: #375
Status: planned
Branch: `feature/p53-environmental-accounts`
Related planning: `ROADMAP.md` (Phase 53)
Source register: candidate `BIO-01`

## Goal

Ingest one Dynamic Habitat Indices product and expose it as a biodiversity
account in ws4, with a trajectory under a scenario and a web/report surface.

## Scope

- Ingest one DHI product (annual layers) for the AOI.
- Attach the layers to fragments or blocks without changing growth.
- Report the DHI trajectory under at least two existing schedules.
- Add a caveat note on scale and interpretation.
- Add a report block and a web layer.

## Out of scope

- A species-specific habitat model or a full SDM.
- A new DHI algorithm or a global biodiversity product.
- A change to the optimisation objective.
- Carbon accounting. It is owned by P51.

## Subtasks

- [ ] Choose the DHI product and document its version and licence.
- [ ] Add the ingest adapter and the AOI coverage check.
- [ ] Define the account name, unit, and level/flow semantics.
- [ ] Emit the trajectory for two schedules.
- [ ] Add the report block and web layer.
- [ ] Document the scale and interpretation caveats.
- [ ] Add tests for coverage, missing data, and reproducibility.

## Acceptance criteria

- The layer covers the AOI, or the report names the gaps.
- The account is reproducible from the source raster and the schedule.
- The trajectory is reported for at least two schedules.
- The caveat note is present in the report.
- The tests fail if the source version or coverage check is dropped.

## Verification

```bash
python scripts/dashboard.py
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Ingest adapter.
- Account and trajectory output.
- Report block and web layer.
- Docs page and changelog entry.

## Risks

- **DHI is a productivity surrogate**, not a species observation. Do not present
  it as a habitat suitability model.
- **Scale mismatch.** DHI is coarse relative to a fragment; state the resolution.
- **Vintage.** Record the year and source version.

## Public sources

- IRSS biodiversity and DHI publications:
  <https://irsslab.forestry.ubc.ca/research/biodiversity/>
- Planning source: IRSS x Silva21 expansion mine (2026-10-25).
