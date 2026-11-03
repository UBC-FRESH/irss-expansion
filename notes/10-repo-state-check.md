# Repo state check

The source mine was done against the IRSS and Silva21 public record. The
candidate queue was then screened against the **live state** of the five repos.
This note records the overlaps that changed a candidate, so the handoff does
not duplicate work that already has an owner.

Checked on 2026-10-25.

## Overlaps that changed a candidate

| Repo | Existing work | Overlap | Adjustment |
| --- | --- | --- | --- |
| `femic` | **P79**, native LidarBC product pipeline (discovery, materialization, terrain, streams, canopy, trees, bundle) | The LiDAR plumbing is already owned | `INV-01`/`DEC-04` add the **inventory model** and model card on top; they do not rebuild the pipeline |
| `femic` | **P109**, CT diameter response and log-grade value/cost accounts | Product recovery, thinning response, value | `OPS-01` feeds the existing CT lane; `OPS-06` adds taper/QSM measurement on top of P109's log-grade accounts |
| `femic` | **P114**, forest hydrology and flood-risk optimization (`#351`, active) | Water, snow, stream response | Hydrology is **not** queued as a new module. `BIO-04` covers stream/riparian metrics; IRSS snow work is an input/validation option for P114 |
| `ws4` | **P48/P49**, ground-plot volume/DBH reconciliation and managed/young validation | Curve validation, site index backtesting | `INV-01`/`INV-04` use the P48/P49 validation surfaces where they apply |
| `ws4` | **P15/P16**, fire-spread experiment with a documented negative result | Fire modelling | Fire is treated as a hazard/expected-loss term (`DIS-06`, `PLAN-01`), not a new simulator |
| `fhops` | **P11/P13**, log hauling, marine/barge cycles | Road access, transport | `OPS-05` is road **status/access**; it links to the hauling contract rather than replacing it |
| `fhops` | **P12**, FHOPS web application (queued) | Scenario explorer, maps, comparison | `DEC-01` targets both ws4 and FHOPS P12 and proposes a shared layer contract |
| `femic` | **P115**, forest carbon domain, CBM packages, GCBM export (`#361`, active) | Carbon domain, package, parity | `CARB-01` is **adopted** by P115; do not open a parallel carbon contract |
| `ws4` | **P58**, forest carbon accounting and carbon-aware planning (`#357`, complete) | Carbon runtime, accounts, targets | `CARB-01` is **adopted** by P58; the ws4 environmental-accounts parent is habitat/resilience-only (`P54`) |
| `ws3` | CBM linkage and avoided-fire/avoided-harvest examples | Carbon reference lane | ws3 is the reference implementation in P115/P58; no separate ws3 carbon issue |
| `nemora` | Phase 2 synthesis and ingest | Synthetic forests, ingest | `DATA-02`/`DATA-04` build on the existing modules, not parallel ones |

## What this means for issue creation

- **All wave-1 issues are created and phase setup is done.** `femic` P116
  `#369` and P117 `#374`; `nemora` P5 `#7`; `ws4` P54 `#375`. Branches, roadmap
  entries, and progress comments are in place; see the handoff README for the
  full list.
- **Check the live roadmap immediately before starting implementation.** These repos
  move quickly; a candidate can become redundant in a week.
- **Link to the existing phase** in the issue body. A reviewer should be able to
  see why this is additive, not duplicate.
- **Keep the contract home decision explicit.** The drafts assume
  `femic/contracts` for the shared schemas, with a note that a small
  `fresh-contracts` repo is the cleaner alternative.

## Why the hydrology correction matters

The initial mine treated water resources as out of scope because it does not
change a near-term estate or operations decision. That was true in the abstract,
but **FEMIC P114 is already building the hydrology layer**. The correct
conclusion is not "water is out of scope"; it is "water already has an owner,
and IRSS/Silva21 water work should be routed to P114 rather than queued here."

This is the general rule: a candidate is only a candidate if no repo already
owns the work.
