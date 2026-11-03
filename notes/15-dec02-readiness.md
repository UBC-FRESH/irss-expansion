# DEC-02 readiness: forest condition report cards

## Candidate

`DEC-02` — forest condition report cards, target `ws4`, wave 2, status
`shortlisted`.

Source: Silva21 OB 3b, *Early alert system for forest management*.
<https://www.silva21.com/projects/early-alert-system-for-forest-management>

## What exists now

WS4 already has the reporting ingredients from P54:

- dynamic habitat indices (`BIO-01`);
- structure habitat index (`BIO-02`);
- spatial resilience metrics (`PLAN-03`);
- report blocks and DHI web-layer work.

FEMIC also has a BA-only inventory pilot, and WS4 has the NTEMS fire-recovery
overlay.  None of these is a recurring condition report card.

## Dependency

`DEC-02` depends on `DIS-03` (near-real-time forest condition and early alert),
which is still a wave-3 candidate.  A report-card schema can be designed now, but
a real alerting product cannot be claimed until `DIS-03` has a condition source
and review path.

## Proposed schema

Working name: `ws4.forest_condition.report.v1`.

| Field | Meaning |
| --- | --- |
| `report_id` | Stable report identifier |
| `scenario_id` | WS4 run/scenario identifier |
| `block_id` | Block or fragment identifier |
| `period` | Reporting period |
| `indicators` | List of indicator records |
| `trend` | Comparable-to-baseline direction, or `not_available` |
| `alerts` | Advisory alerts with severity and reason |
| `provenance` | Source product, model card, version, and SHA |
| `review_status` | `draft`, `provisional`, or `reviewed` |

Each indicator record should carry:

- `name`, `value`, `unit`;
- `source` and `source_version`;
- `uncertainty` (RMSE or interval) where available;
- `applicability` or abstention reason;
- `status` (`ok`, `outside_domain`, `missing`, `review_required`).

## Pilot shape

A bounded pilot can use an existing WS4 run and P54 outputs:

1. Select one run and a small block set.
2. Emit a JSON report with DHI, structure-habitat availability, fire-recovery
   status, and the BA-only inventory applicability.
3. Emit a one-page Markdown/HTML card.
4. Mark all alerts advisory and all unreviewed sources `draft`.
5. Compare two existing schedules, without changing the objective or solver.

This is a report-only pilot.  It does not create a new condition model.

## Blocker and recommendation

WS4 has active phases P82 and P83.  Do not open a competing `DEC-02` phase in
that repository until those close or the maintainer explicitly reprioritizes.
The correct next step is a **schema and pilot design** in this planning project;
implementation waits for a free target phase.

Recommendation: keep `DEC-02` shortlisted, write the schema into a target issue
draft, and queue it after the current WS4 phase closeout.  Do not claim early
alerting, operational condition monitoring, or a new model.
