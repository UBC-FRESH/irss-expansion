Maintenance
===========

The mine is a standing queue. This page records the operating cadence, the
commands that check it, and the decision that keeps it recurring.

The source of truth for the dates is ``registry/maintenance.yaml``. The
long-form procedure is `notes/25-p6-maintenance-plan.md
<https://github.com/UBC-FRESH/irss-expansion/blob/main/notes/25-p6-maintenance-plan.md>`_.
The recurring decision is `ADR 0001
<https://github.com/UBC-FRESH/irss-expansion/blob/main/notes/adr/0001-recurring-maintenance.md>`_.

Cadence
-------

.. list-table::
   :header-rows: 1

   * - Check
     - Interval
     - Command
   * - Registry review and re-score
     - 90 days
     - ``python scripts/check_maintenance.py --due``
   * - Source refresh
     - 180 days
     - ``python scripts/refresh_sources.py --json``
   * - Issue/registry drift
     - 30 days
     - ``python scripts/check_issue_drift.py --json``
   * - Register freshness
     - Every commit
     - ``python scripts/check_maintenance.py``

The deterministic check runs in the green dashboard. The due-date check, the
source refresh, and the live drift check are manual and dated, so a publisher
outage or a calendar date cannot break a clean checkout.

What the checks can fail on
---------------------------

``check_maintenance.py`` fails when the schedule arithmetic is wrong, the
generated register is stale, a ``complete``, ``adopted``, or ``queued``
candidate has no resolution, an active candidate has no recorded target
record, or ``--due`` is past a next date.

``refresh_sources.py`` fails when a source is broken. A publisher that returns
401, 403, 405, or 429 is reported as blocked and does not fail the run.

``check_issue_drift.py`` fails when a live issue or pull-request state differs
from its recorded expectation, or when ``gh`` cannot read the record.

What the checks do not prove
----------------------------

- A reachable URL does not prove the content, licence, or scientific claim.
- A live target record does not prove that the target test suite or science
  passes.
- Readiness remains an integration judgement, not an author-confirmed estimate.
- The checks are dated snapshots. Re-read the live record before a later
  handoff or status change.
