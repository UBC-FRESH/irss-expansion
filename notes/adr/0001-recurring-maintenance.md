# ADR 0001: The mine recurs on a maintenance cycle

Status: accepted
Date: 2026-11-03
Issues: #35, #38

## Context

The `0.1.0` release published 62 candidates in nine workstreams, a registry
validator, a generated register, and a public docs site. The queue cites public
IRSS and Silva21 pages, DOI links, and live records in five target repositories.
Those references are dated: publishers change URLs, target phases merge, and a
candidate that looks ready today can become a duplicate tomorrow.

A one-off release would be simpler to archive. It would also leave the active
`GRO-06` and `CARB-03` records without a scheduled check, and it would make the
next IRSS or Silva21 publication a reason to rebuild the process rather than
refresh it. A recurring cycle has a carrying cost, but it is small: three
commands, three intervals, and a written review.

## Decision

The mine is recurring. The maintainers keep the public repository as a standing
queue and run the cadence in [`../25-p6-maintenance-plan.md`](../25-p6-maintenance-plan.md):

- every 90 days, review and re-score the registry;
- every 180 days, refresh the public source URLs;
- every 30 days, check the active issue and registry records against GitHub;
- on every commit, keep the deterministic maintenance and dashboard gates green.

The dates and intervals live in [`../../registry/maintenance.yaml`](../../registry/maintenance.yaml).
The recurring decision is itself reviewed at each 90-day review. It becomes
one-off, and the repository moves to an archive notice, when all of these hold:

- no candidate is `queued` or `adopted`;
- two consecutive source refreshes find no new or vanished source that changes a
  candidate;
- no target repository is running a phase that consumes the queue;
- the maintainers record the archive decision and the final changelog entry.

Retiring the queue never deletes the register. The final generated register and
the notes stay public with an archive notice.

## Consequences

- The active records get a dated check instead of relying on memory.
- A stale source or a merged target record becomes a visible finding with a
  command behind it.
- The repository needs a maintainer for three small recurring tasks, and a
  missed cycle shows up as a manual `--due` failure rather than silent drift.
- The review can reverse the decision to one-off without changing the registry
  format or the published register.
- The cadence adds no network check to CI: source and live-issue checks stay
  manual and dated, so a publisher outage cannot break a clean checkout.

## Alternatives considered

- **One-off release, then archive.** Rejected because two candidates are live
  and the queue would lose its scheduled review. The archived register would
  still be readable, but a later source change would have no owner.
- **Continuous monitoring in CI.** Rejected because publisher blocks and GitHub
  rate limits would make the dashboard depend on external services. The manual
  dated check keeps the gate deterministic.
- **Re-mine both programmes every cycle.** Rejected as out of scope and too
  expensive. The cycle refreshes the existing evidence; a new mine needs its own
  approved phase.
