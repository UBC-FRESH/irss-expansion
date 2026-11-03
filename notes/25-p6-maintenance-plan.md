# P6 maintenance plan

Date: 2026-11-03
Phase: P6 Operate and maintain
Parent issue: #35
Task: P6.1
Schedule: [`../registry/maintenance.yaml`](../registry/maintenance.yaml)
First review: [`26-p6-first-review.md`](26-p6-first-review.md)
Decision: [`adr/0001-recurring-maintenance.md`](adr/0001-recurring-maintenance.md)

## Purpose

The `0.1.0` release is a queue, not an archive. The public sources change, the
target repositories move, and a candidate can become stale without anyone
editing the registry. This plan keeps the queue honest with a named cadence, a
command that can fail for each recurring check, and a written record of what was
and was not verified.

The plan is deliberately small. It does not re-mine IRSS or Silva21 on a
schedule, re-open a target phase, or turn a screening score into an approval. It
checks the existing evidence, refreshes the source links, and records decisions.

## Cadence

| Check | Interval | Last | Next due | Command | Record |
| --- | --- | --- | --- | --- | --- |
| Registry review and re-score | 90 days | 2026-11-03 | 2027-02-01 | `python scripts/check_maintenance.py --due` | A dated review in `notes/` and the `CHANGE_LOG.md` entry |
| Source refresh | 180 days | 2026-11-03 | 2027-05-02 | `python scripts/refresh_sources.py --json` | Counts, blocked hosts, and broken rows in the review |
| Issue/registry drift | 30 days | 2026-11-03 | 2026-12-03 | `python scripts/check_issue_drift.py --json` | Live states beside the expected states |
| Register freshness | Every commit | The P6 head | The next commit | `python scripts/check_maintenance.py` | The green dashboard and CI |

The dates and intervals are in `registry/maintenance.yaml`. The checker fails
when a next date is not exactly the interval after its last date. `--due` is a
manual check: it fails after the next date has passed, but it is not part of the
dashboard, so a calendar date alone cannot turn a clean checkout red.

Run the monthly drift check and the quarterly review together when they fall in
the same month. The shorter interval wins.

## Off-cycle triggers

Run the relevant check, and record the result, when any of these happens:

- A public source returns a new status, changes publisher, or disappears.
- A target repository closes a phase that carries a `queued` or `adopted`
  candidate.
- A target pull request for an `adopted` candidate merges, closes without
  merging, or goes idle for a full review cycle.
- A new IRSS or Silva21 publication changes the evidence behind a candidate.
- The dashboard, CI, or Pages build fails on a surface that the register cites.

An off-cycle check does not reset the scheduled dates unless it covers the same
scope and the review records that fact.

## Registry review procedure

1. Run `python scripts/check_maintenance.py --due` and fix every consistency
   error before changing a status.
2. Read the active targets named in `registry/maintenance.yaml`. Record the date
   and the live state; do not infer a merge from a green check or a merged title.
3. Re-score only the candidates whose evidence changed. A score change needs the
   old value, the new value, and the evidence in the review note.
4. Decide every status group:
   - `complete`: keep when the live target record still exists; a missing record
     becomes a drift finding.
   - `adopted`: keep while the target work is live; revisit when it merges,
     closes unmerged, or stalls for a cycle.
   - `queued`: keep while the target issue is open and the handoff is current.
   - `shortlisted`, `candidate`: keep or defer on the recorded evidence. Do not
     mark a candidate `queued` without the maintainer approval that the workflow
     requires.
   - `deferred`, `rejected`: keep the reason and the revisit trigger. Retire only
     with a recorded reason.
5. If the registry changes, run `python scripts/render_registry.py`, then
   `git diff --exit-code docs/candidates.md`, `python scripts/check_registry.py`,
   and `python -m pytest`.
6. Write the review note, update `CHANGE_LOG.md`, and post a progress comment on
   the phase issue when the review closes.

## Retirement triggers

Retire a candidate to `rejected` or `deferred` when one of these holds and the
review records the evidence:

- The cited product or model no longer exists at its public URL, and no
  replacement source supports the same first step.
- The target repository has completed or rejected the same work and the
  registry row would duplicate it.
- The scope rule excludes the work because it requires new general science
  rather than integration.
- Two consecutive review cycles pass with no owner, no first step, and no
  evidence that the candidate can change a FRESH decision.

Retirement is not deletion. The row keeps its sources, gap, score, and reason,
and the generated register keeps it in the detail section.

## Source refresh

`python scripts/refresh_sources.py --json` reads every unique public URL,
follows redirects, and classifies the response:

- `ok`: HTTP 2xx.
- `blocked`: HTTP 401, 403, 405, or 429. The page may exist, but it refuses an
  automated client. Record the block; do not claim the content was read.
- `broken`: a network or redirect failure, or any other status. Investigate and
  fix the URL or retire the candidate.

The check never edits the registry and it is not a CI gate, because it needs the
public network and publisher behaviour is not stable. It is a dated snapshot.

## Issue/registry drift

`python scripts/check_issue_drift.py --json` reads each record in
`registry/maintenance.yaml` with `gh` and compares the live state:

- An issue reports `open` or `closed`.
- A pull request reports `open`, `closed`, or `merged`.
- A `complete` candidate must not have an expected-open record.
- Every `queued` or `adopted` candidate must have at least one record.

Update the expected state only after reading the live record. A mismatch is a
finding to investigate, not a reason to change the expectation silently.

## Roles and records

The UBC-FRESH maintainers own the cadence and approve any status that queues a
candidate for implementation. An agent may run the checks, write the review, and
propose a status change; it may not approve its own queueing or merge its own
phase.

The durable record is:

- `registry/maintenance.yaml` for the dates, intervals, and active records.
- `notes/` for each dated review.
- `CHANGE_LOG.md` for the task-level summary.
- `docs/maintenance.rst` for the public procedure.
- The GitHub P6 issues for the live discussion and approval.

## Limits

- The source check reports reachability, not content, correctness, or licence.
- The drift check reads issue and pull-request state, not target test suites.
- Readiness remains an integration judgement, not an author-confirmed estimate.
- A green dashboard proves the planning surfaces agree. It does not prove that a
  candidate is scientifically sound or that a target repository will accept it.
