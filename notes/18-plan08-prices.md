# PLAN-08 readiness: price and policy paths

## Candidate

`PLAN-08` market and policy shock scenarios: support price, cost, and policy
paths as scenario inputs with provenance, rather than static values.

## Outcome

Complete. UBC-FRESH/ws4 P114 (#749, PR #760) squash-merged to `main` as
`0dbc01a`. The change added the typed `prices.v1` reader in `ws4/prices.py`,
the `ws4 price-paths` command, a synthetic four-path fixture (`base`, `high`,
`low`, `policy_shock`), and the comparison CSV, Markdown report, and provenance
sidecar with the mandatory `not a forecast` caveat. The table is a read-only
scenario input; no objective, constraint, growth, schedule, simulator, or solver
code changed.

The rest of this note records the readiness case that led to that first step.

## State before the change

WS4 has road build/maintenance costs, product accounts, and cost ceilings, but
no general `prices.v1` scenario input. FHOPS has operational cost/revenue
surfaces, but no shared price-path contract with WS4. There was no scenario
file that names a price path, its source, vintage, currency, or region.

## Proposed first step

Add a `prices.v1` table for one WS4/FHOPS scenario:

- `path_id`, `product`, `period`, `value`, `unit`, `currency`,
  `region`, `source`, `source_version`;
- named paths such as `base`, `high`, `low`, and `policy_shock`;
- provenance and an explicit `not a forecast` caveat;
- read-only consumption by an existing report or scenario; no objective change.

The first pilot should be one named path, one product account, and a static
Markdown/CSV comparison against base. It should not add a price-forecasting
model or alter solver weights.

## Why it waited

`DEC-03` was only partially complete, and PLAN-08 depends on its provenance
contract. The active WS4 work was separate. This note started as a readiness
record, not an issue or branch.

## Follow-on

The merged table is synthetic. A real public price source with currency and
region provenance is still needed before production use, and a FHOPS consumer
of the same contract is not yet built. Those remain open follow-on work, not
part of this candidate's first step.
