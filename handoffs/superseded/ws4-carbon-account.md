Task identifier: P<next>.1
Parent phase issue: #<parent>
Status: planned
Branch: `feature/p<next>-environmental-accounts`
Related planning: `ROADMAP.md` (Phase <next>)
Source register: candidate `CARB-01` (ws4 side)
Related ws3 draft: carbon contract (superseded).

## Goal

Emit a carbon account from one ws4 scenario using the carbon-account contract
that ws3 exposes from its CBM path. Version 0 may use existing volume curves
with a declared basic-density and carbon-fraction conversion; a biomass curve
family (`GRO-06`) is a later refinement.

## Scope

- Define the ws4 account fields: stand biomass, carbon stock, harvested
  biomass, product pool, emissions, and decay.
- Emit the account for one scenario.
- Add a report block and a scenario comparison view.
- Compare with the ws3 contract on a compatible scenario and record the
  difference.
- Label every conversion factor, boundary, and version.
- Add tests for the arithmetic, unit handling, and report wiring.

## Out of scope

- A new CBM implementation or a second carbon model. Reuse the ws3 contract.
- Soil carbon.
- A full life-cycle assessment or substitution model.
- A carbon market or credit model.
- Changing the optimisation objective. Risk-aware planning is `PLAN-01`.
- A new biomass curve family. That is `GRO-06`; v0 uses a declared conversion.

## Subtasks

- [ ] Define the account fields and level/flow semantics.
- [ ] Implement the account from the ws3 contract.
- [ ] Add the report block and scenario comparison.
- [ ] Add the ws3/ws4 reconciliation case.
- [ ] Add unit, arithmetic, and wiring tests.
- [ ] Document the boundary and assumptions.
- [ ] Add a changelog entry.

## Acceptance criteria

- Stand carbon equals biomass times the declared carbon fraction.
- The account declares its boundary: stand, product, and soil pools; what is in
  and what is out.
- The ws3 and ws4 paths agree within a stated tolerance on the shared boundary,
  or the difference is explained.
- Every conversion factor has a source and a version.
- The report block shows the account and its assumptions.
- A test fails if the carbon fraction or a unit is dropped.
- No objective or constraint changes are made.

## Verification

```bash
python scripts/dashboard.py
```

If the dashboard is unavailable, run the package checks in `pyproject.toml`
(`ruff`, `mypy`, `pytest`) and the docs build. Record the exact commands and
results in `CHANGE_LOG.md`.

## Artifacts

- Account implementation.
- Report block and comparison view.
- Reconciliation case and tests.
- Boundary note.
- Changelog entry.

## Risks

- **Boundary disagreement.** ws3 and ws4 may treat product pools and decay
  differently. Record the difference; do not average it away.
- **False precision.** A single carbon number without a band invites overuse.
  Label assumptions and add uncertainty where the data support it.
- **Conversion uncertainty.** Volume-to-biomass conversion is a stopgap until
  `GRO-06` lands. Make that explicit.
- **Double counting.** Harvested wood can appear as a product pool and as an
  emission. Define the accounting identity.

## Public sources

- ws3 CBM linkage and avoided-fire/avoided-harvest examples:
  <https://github.com/UBC-FRESH/ws3>
- Tompalski et al. 2024, biomass yield curves:
  <https://doi.org/10.1016/j.foreco.2024.121894>
- IRSS carbon research: <https://irsslab.forestry.ubc.ca/research/carbon/>
- FEMIC P109 log-grade value/cost accounts:
  <https://github.com/UBC-FRESH/femic>
