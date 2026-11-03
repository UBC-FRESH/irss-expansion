Source register: candidate `CARB-01` (ws3 side)
Related: `ws4-carbon-account.md`

## Problem statement

ws3 already has a working CBM linkage (`to_cbm_sit`, CBM site classifiers,
disturbance types, inventory, yield, events, and transitions) and notebook-level
avoided-fire and avoided-harvest decision-support examples. What it does not
have is a **reusable carbon-account contract** that another repo can emit and
compare against.

## Proposed solution

Expose the CBM path as a versioned carbon-account contract:

- stand biomass and carbon stock;
- harvested biomass and product pools;
- disturbance emissions (fire, harvest, decomposition) where the CBM path
  supports them;
- decay and storage assumptions;
- provenance for every factor and boundary.

Add a small API or CLI that returns the account for a scenario, plus a boundary
note. Do not add a second carbon model.

## Scope

- Define the account fields and their units.
- Wrap the existing CBM setup in a callable path with a stable input/output
  contract.
- Document the system boundary: stand, product, and soil pools; what is in and
  what is out.
- Add a regression case that reproduces the existing avoided-fire or
  avoided-harvest example.
- Publish the contract so ws4 can emit the same account.

## Out of scope

- A new CBM implementation or a new carbon model.
- A ws4 account implementation. That is the linked ws4 issue.
- Soil-carbon dynamics.
- A carbon market, credit, or policy model.
- A full life-cycle assessment.

## Acceptance criteria

- The account has named fields, units, and a schema version.
- The existing avoided-fire or avoided-harvest example reproduces through the
  new contract.
- The boundary note names what is excluded and why.
- Every conversion factor has a source and a version.
- The output is deterministic for the same inputs and CBM configuration.
- A test fails if a field or unit is dropped.

## Verification

```bash
python -m pytest
ruff check .
mypy .
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in the repo changelog.

## Alternatives considered

- **Put the contract only in ws4.** Rejected: ws3 already owns the CBM path and
  the avoided-emissions examples. A ws4-only contract would duplicate the
  boundary logic.
- **Build a new carbon module.** Rejected: it duplicates a working linkage and
  adds a second source of truth.
- **Use a generic tabular export.** Rejected: it loses units, boundary, and
  provenance, which are the point of the contract.

## Use case

A planner runs the same harvest scenario in ws3 and ws4 and wants to know
whether the carbon answer agrees. The contract makes the comparison possible
and makes disagreement inspectable instead of hidden.

## Additional context

- Planning source: IRSS x Silva21 expansion mine (2026-10-25).
- ws4 side: carbon account (superseded).
- IRSS carbon research:
  <https://irsslab.forestry.ubc.ca/research/carbon/>
- Tompalski et al. 2024, biomass yield curves:
  <https://doi.org/10.1016/j.foreco.2024.121894>
- FEMIC P109 log-grade value/cost accounts:
  <https://github.com/UBC-FRESH/femic>
