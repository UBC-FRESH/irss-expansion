Phase identifier: P54
Status: planned
Branch: `feature/p53-environmental-accounts`
Roadmap: `ROADMAP.md`, section "Phase 53: Environmental accounts"
Pull request: not opened yet

Source register: IRSS x Silva21 expansion mine, candidates `BIO-01`, `BIO-02`,
and `PLAN-03`.

## Goal

Make biodiversity, habitat structure, and landscape resilience first-class ws4
accounts. The estate model already reports volume, products, features, patches,
spread, and roads. This phase adds three read-only environmental accounts with
units, provenance, and a report/web surface.

The phase does not change the optimisation objective. It makes the values
visible and comparable first; risk and resilience enter the objective only after
the accounts are trusted.

## Why now

- The carbon account is already in flight under **P51** (`#357`), with FEMIC
  **P115** (`#361`) producing the package. This phase covers the non-carbon
  values.
- DHI is a public, mature biodiversity product; the structure habitat index is a
  published ALS index; the resilience metrics reuse existing patch/spread
  accounts.
- All three are wave-1 candidates in the expansion register, and all three can
  be reported without a new optimisation model.

## Scope

- Dynamic Habitat Indices as biodiversity accounts (`BIO-01`).
- Forest structure habitat index from ALS (`BIO-02`).
- Spatial resilience metrics from existing patch/spread accounts (`PLAN-03`).
- A shared account contract: name, unit, level/flow semantics, source, version,
  and uncertainty where available.
- Report and web exposure for each account.

## Out of scope

- Carbon. It is owned by P51 and FEMIC P115.
- A species-specific habitat model or a full SDM.
- A change to the objective, constraints, or solver. Risk-aware planning is a
  later phase (`PLAN-01`).
- A fire-spread simulator. Fire remains a hazard/expected-loss input.
- FEMIC P114 hydrology.
- A new data portal.

## Architecture notes

- Accounts follow the existing ws4 accounting semantics: accumulating accounts
  are summed over a period; level accounts are read at the period's end offset.
- Each account must declare whether it is a level or a flow, and its unit.
- DHI and structure habitat are read-only layers attached to fragments or
  blocks; they do not change growth.
- The resilience metrics are derived from the schedule and patch topology, not
  from a new spatial model.
- The carbon account already demonstrates the account/report pattern; reuse it
  rather than inventing a second account surface.

## Child task checklist

- [ ] #376 `P54.1`: Add the DHI biodiversity account (`BIO-01`)
- [ ] #377 `P54.2`: Add the structure habitat index (`BIO-02`)
- [ ] #378 `P54.3`: Add spatial resilience metrics (`PLAN-03`)

## Acceptance criteria

- Each account has a name, unit, level/flow semantics, source, and version.
- Each account is reproducible from the scenario and its declared inputs.
- DHI and structure habitat accounts cover the AOI or report their gaps.
- Identical schedules produce identical resilience metrics.
- Every account appears in at least one report or web view.
- No objective or constraint changes are made in this phase.

## Verification

```bash
python scripts/dashboard.py
```

If the dashboard is unavailable, run the package checks in `pyproject.toml`
(`ruff`, `mypy`, `pytest`) and the docs build. Record the exact commands and
results in `CHANGE_LOG.md`.

## Phase setup

- [x] Create `feature/p54-environmental-accounts` from the current `main`.
- [x] Add the Phase 54 section to `ROADMAP.md` and link `#375` (commit `9b9b9bf`).
- [ ] Confirm the account pattern against P51 carbon (`#357`) and reuse it.
- [x] Post a progress comment on `#375` when the branch and roadmap entry exist.

## Closeout requirements

- Merge only when every child has a report/web surface and a test that can fail.
- Record the account names and units in the docs and changelog.
- Do not change the objective in this phase. Open a separate phase for
  risk-aware planning (`PLAN-01`).
- Do not tag or release as part of this phase.

## Risks

- **Layer staleness.** DHI and habitat layers have vintages. Record them.
- **Metric redundancy.** Three resilience metrics can tell the same story.
  Validate that they respond differently to different schedules.
- **False precision.** A habitat index is not a species observation. Label it.
- **Scope creep into carbon.** Carbon has its own phase; link to it, do not
  duplicate it.

## Source register

- Candidate `BIO-01`: Dynamic Habitat Indices as biodiversity layers.
- Candidate `BIO-02`: forest structure habitat index from ALS.
- Candidate `PLAN-03`: spatial resilience metrics for estate models.
- Live-repo overlap check performed 2026-10-25; the planning packet is not yet published.
