# DIS-03 readiness: near-real-time condition and early alert

## Candidate

`DIS-03` — near-real-time forest condition and early alert, target `ws4`, wave
3, status `candidate`.

Source: Silva21 OB 3b, *Early alert system for forest management*.
<https://www.silva21.com/projects/early-alert-system-for-forest-management>

## What exists

- WS4 can ingest a single DHI composite (2003-2022) as a static productivity
  surrogate.
- WS4 can ingest the NTEMS post-fire recovery layer as a static recovery class.
- `DEC-02` now has a report-card schema, account-derived CLI, read-only API, and
  Reports-tab viewer.
- `DIS-02` (NSR detection) is implemented as the exploratory `fresh-beast`
  package, but its TSA 23 case-control test failed operational thresholds:
  sensitivity 25.8%, specificity 66.0%, precision 33.3%, and 0/31 same-year
  detections.

## What is missing

A real-time or annual condition series with a defensible baseline, alert rules,
and review workflow. The current DHI and recovery products are static overlays;
neither is a current-condition monitoring loop.

No public feed, refresh contract, alert threshold, or review owner is present in
the current WS4/FEMIC surfaces. Reusing the static layers as an alert would
misstate their meaning.

## Decision

Keep `DIS-03` **deferred**, not queued. The DEC-02 cards may display the static
DHI/recovery/account indicators as context, but they are not early alerts.

Unblock requires:

- an annual or near-real-time condition product with provenance and refresh
  cadence;
- a baseline and alert-rule definition;
- a reviewed response path for alerts;
- a validation case showing the alert is better than a static report.

## What not to do

- Do not turn DHI or recovery into an alert threshold.
- Do not use the failed NSR case-control result as an operational detector.
- Do not add a UI alert without a real source and review owner.
