Phase identifier: P<next> (proposed; confirm the next free phase after P50)
Status: planned
Branch: `feature/p<next>-environmental-accounts`
Roadmap: `ROADMAP.md`, section "Phase <next>: Environmental accounts"
Pull request: not opened yet

Source register: IRSS x Silva21 expansion mine, candidates `CARB-01`, `BIO-01`,
`BIO-02`, and `PLAN-03`.

## Goal

Make environmental values first-class ws4 outputs. The estate model already
reports volume, products, features, patches, spread, and roads. This phase adds
carbon, biodiversity, habitat structure, and landscape resilience as **accounts**
with units, provenance, and a report/web surface.

The phase does not change the optimisation objective. It makes the values
visible and comparable first; risk and resilience enter the objective only after
the accounts are trusted.

## Scope

- Carbon account v0 from the ws3 CBM contract (`CARB-01`).
- Dynamic Habitat Indices as biodiversity accounts (`BIO-01`).
- Forest structure habitat index from ALS (`BIO-02`).
- Spatial resilience metrics from existing patch/spread accounts (`PLAN-03`).
- A shared account contract: name, unit, period semantics (level vs flow),
  source, version, and uncertainty where available.
- Report and web exposure for each account.

## Out of scope

- A new carbon model or CBM implementation. Reuse the ws3 path.
- A species-specific habitat model or a full SDM.
- A change to the objective, constraints, or solver.
- A fire-spread simulator. Fire remains a hazard/expected-loss input.
- FEMIC P114 hydrology.
- A new data portal.

## Architecture notes

- Accounts follow the existing ws4 accounting semantics: accumulating accounts
  are summed over a period; level accounts are read at the period's end offset.
- Each account must declare whether it is a level or a flow, and its unit.
- The carbon account consumes the ws3 contract; it does not re-implement the
  CBM boundary.
- The DHI and structure habitat accounts are read-only layers attached to
  fragments or blocks; they do not change growth.
- The resilience metrics are derived from the schedule and patch topology, not
  from a new spatial model.

## Child task checklist

- [ ] #<child> `P<next>.1`: Emit the carbon account from the ws3 CBM contract (`CARB-01`)
- [ ] #<child> `P<next>.2`: Add the DHI biodiversity account (`BIO-01`)
- [ ] #<child> `P<next>.3`: Add the structure habitat index (`BIO-02`)
- [ ] #<child> `P<next>.4`: Add spatial resilience metrics (`PLAN-03`)

The carbon child is drafted first. The other three are queued in the register
and can be drafted when the carbon account has a merged consumer.

## Acceptance criteria

- Each account has a name, unit, level/flow semantics, source, and version.
- Each account is reproducible from the scenario and its declared inputs.
- Carbon reconciles with the ws3 contract within a stated tolerance.
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

## Closeout requirements

- Merge only when every child has a report/web surface and a test that can fail.
- Record the account names and units in the docs and changelog.
- Do not change the objective in this phase. Open a separate phase for
  risk-aware planning (`PLAN-01`).
- Do not tag or release as part of this phase.

## Risks

- **Boundary disagreement.** ws3 and ws4 may define product and decay pools
  differently. The contract comparison is the point; do not hide it.
- **False precision.** A carbon number with no uncertainty invites overuse.
  Label assumptions and add bands where possible.
- **Layer staleness.** DHI and habitat layers have vintages. Record them.
- **Metric redundancy.** Three resilience metrics can tell the same story.
  Validate that they respond differently to different schedules.

## Source register

- Candidate `CARB-01`: carbon account v0 across ws3 and ws4.
- Candidate `BIO-01`: Dynamic Habitat Indices as biodiversity layers.
- Candidate `BIO-02`: forest structure habitat index from ALS.
- Candidate `PLAN-03`: spatial resilience metrics for estate models.
- Live-repo overlap check performed 2026-10-25; the planning packet is not yet published.
