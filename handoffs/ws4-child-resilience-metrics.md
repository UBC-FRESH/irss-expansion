Task identifier: P54.3
Parent phase issue: #375
Status: planned
Branch: `feature/p53-environmental-accounts`
Related planning: `ROADMAP.md` (Phase 53)
Source register: candidate `PLAN-03`

## Goal

Add a compact set of spatial resilience metrics to ws4 so a planner can see how
a schedule changes landscape configuration, not only volume and cost.

## Scope

- Implement three metrics: a connectivity or barrier metric, an age-class
  diversity metric, and a patch-size or fragmentation metric.
- Derive them from the existing ws4 patch, spread, and schedule outputs.
- Report them as accounts with definitions and units.
- Compare at least two existing schedules.
- Do not put them in the objective.

## Out of scope

- A new spatial model or fire simulator.
- A change to the objective or constraints. Risk-aware planning is `PLAN-01`.
- A species-specific connectivity model.
- Carbon accounting. It is owned by P51.

## Subtasks

- [ ] Define the three metrics, units, and level/flow semantics.
- [ ] Implement them from the existing patch/spread accounts.
- [ ] Add a report block and scenario comparison.
- [ ] Add a property test: identical schedules produce identical metrics.
- [ ] Compare two schedules and record the expected direction of change.
- [ ] Document the definitions, caveats, and redundancy check.
- [ ] Add a web surface if the report alone is not enough.

## Acceptance criteria

- Identical schedules produce identical metrics.
- The metrics change in the expected direction for a deliberately fragmented
  schedule.
- The definitions and units are in the report.
- At least one metric is shown to be non-redundant with the others.
- No objective or constraint changes are made.

## Verification

```bash
python scripts/dashboard.py
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Metric implementations.
- Report/comparison output.
- Property test and schedule comparison.
- Docs page and changelog entry.

## Risks

- **Metric redundancy.** Three metrics can tell the same story; test it.
- **Scale sensitivity.** Patch metrics depend on the topology and block
  aggregation. State the scale.
- **False precision.** A single index can hide the pattern. Report components.

## Public sources

- IRSS landscape pattern and disturbance research:
  <https://irsslab.forestry.ubc.ca/research/disturbance-habitat-change/>
- ws4 patch and spread accounts:
  <https://github.com/UBC-FRESH/ws4>
- Planning source: IRSS x Silva21 expansion mine (2026-10-25).
