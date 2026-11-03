# Phase close-out report: P6 Operate and maintain

Phase: P6 Operate and maintain
Parent issue: #35
Pull request: [#39](https://github.com/UBC-FRESH/irss-expansion/pull/39),
`feature/p6-operate` into `main`
Evidence head: `f1feba9` (P6 pull request head), plus the merge commit and this
close-out commit
Date: 2026-11-03
Status: approved by the maintainer on 2026-11-03; squash-merged to `main` as
`625e354`, and issues #35-#38 closed.

## Recommendation

The maintainer approved these actions on 2026-11-03; the close-out record is
section 9.

1. Squash-merge pull request #39 into `main` and delete `feature/p6-operate`.
2. Close parent issue #35 and child issues #36-#38 with closeout comments that
   cite the P6 commits, the gate evidence, and the merge commit.
3. Keep the recurring maintenance decision and its schedule in force: the next
   registry review is due 2027-02-01, the next source refresh 2027-05-02, and the
   next issue/registry drift check 2026-12-03.
4. Do not tag or release. P6 produces no new version, package artifact, or DOI.

Settings changes, each with its exact command. None ran.

- None. P6 changes no repository visibility, Pages configuration, branch
  protection, environment, external account, or package-index artifact. No
  tag or release was created.

## 1. Objectives and acceptance

| Criterion | Evidence | Status |
| --- | --- | --- |
| The cadence, the source-refresh interval, and the issue/registry drift interval are recorded and enforced by a command that can fail | `registry/maintenance.yaml` records the 90-day, 180-day, and 30-day intervals; `scripts/check_maintenance.py` runs in the dashboard and fails on bad arithmetic, stale register, missing resolutions, or missing active records; the dated `--due` check passes | met |
| Every active candidate has a live target record, and the register matches its generated document | `python scripts/check_issue_drift.py --json` matched all five recorded records on 2026-11-03; `python scripts/check_maintenance.py` passes and the renderer is idempotent | met |
| The re-score records a decision for every status group and names any retirement or change | `notes/26-p6-first-review.md` records the decisions for all seven status groups: no score change, no status change, no retirement | met |
| The recurring-or-one-off decision is recorded as an ADR | `notes/adr/0001-recurring-maintenance.md` decides that the mine recurs, names the cadence, and records the archive condition | met |
| `check_workflow.py`, `check_registry.py`, `pytest`, and `dashboard.py` pass on the P6 head | Section 3: 0 errors and 0 warnings; 62 valid candidates; 255 tests pass with 99.49% branch coverage; all seven dashboard gates GREEN | met |

## 2. Workflow compliance

- Parent issue #35 and child issues #36-#38 existed before the P6 work started;
  P6 moved from `planned` to `active` and then to `pr-open`.
- `feature/p6-operate` was created from `main` at `073d804`.
- Commit messages start with the task ID: `eb7288c` P6.1-P6.3, `f1feba9` P6
  phase status and pull request record.
- `ROADMAP.md`, `CHANGE_LOG.md`, the P6 notes, this report, and the issue bodies
  are in step. P6 is `complete` after this close-out commit.
- No target-repository issue, branch, pull request, tag, release, or setting was
  created or edited. All target checks were read-only.
- No candidate was implemented, queued in a target repository, re-scored, or
  retired. `GRO-06` remains `queued`; `CARB-01` and `CARB-03` remain `adopted`.
- Approval gates: the merge, branch deletion, and issue closures followed the
  maintainer's explicit approval. No tag or release was requested or run.

## 3. Gate evidence

| Commit | Gate run | Result |
| --- | --- | --- |
| `f1feba9` P6 pull request head | `check_workflow.py`; `check_registry.py`; `render_registry.py`; `git diff --exit-code docs/candidates.md`; `check_maintenance.py --due`; `check_issue_drift.py --json`; `refresh_sources.py --json`; `pytest -q`; `dashboard.py` | 0 errors/0 warnings; 62 valid candidates; renderer idempotent; due and live drift checks pass; 84 URLs with 0 broken; 255 passed with 99.49% branch coverage; all seven gates GREEN |
| P6 close-out commit (`ROADMAP.md`, `README.md`, `CHANGE_LOG.md`, this report) | `check_workflow.py`; `check_registry.py`; `render_registry.py`; `git diff --exit-code docs/candidates.md`; `check_maintenance.py`; `pytest -q`; `dashboard.py` | 0 errors/0 warnings; 62 valid candidates; renderer idempotent; maintenance check passes; 255 passed with 99.49% branch coverage; all seven gates GREEN |

## 4. Merge and branch evidence

| Action | Command | Result |
| --- | --- | --- |
| Squash merge | `gh pr merge 39 --squash --delete-branch` | Pull request #39 merged 2026-11-03T23:27:17Z as `625e354dc6d8e3d9538189bb8b984346f258cbeb` (`625e354`) |
| Branch deletion | included in the merge command | `origin/feature/p6-operate` and the local branch deleted; `git branch -a` lists only `main` |

The squash commit is `P6: operate and maintain the queue (#39)`. No tag points
at it, and no GitHub release was created from it.

## 5. CI and Pages evidence

| Run ID | Head commit | Conclusion | Notes |
| --- | --- | --- | --- |
| [41739271892](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41739271892) | `625e354` | success | `main` push; Quality gates, Green dashboard summary, and Pre-commit parity all succeed |
| [41739271917](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41739271917) | `625e354` | success | `main` push; Docs build and deploy both succeed |
| [41737838429](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41737838429) | `f1feba9` | success | Pull request #39; Quality gates, Green dashboard summary, and Pre-commit parity all succeed |

The public Pages site returned HTTP 200 on 2026-11-03 for the index,
`maintenance.html`, `register.html`, `releases.html`, `candidates.md`, and
`llms.txt` after the `625e354` deployment. `maintenance.html` was briefly 404
while the deploy propagated and returned 200 once the deploy job completed.

## 6. Programme status and next cycle

Register status at close-out: 17 `complete`, 2 `adopted`, 1 `queued`, 14
`shortlisted`, 23 `candidate`, 4 `deferred`, 1 `rejected`; 62 candidates in
total. No candidate was re-scored or retired in P6.

Programme status at close-out: P0-P6 are complete and merged. The mine recurs.
The next scheduled actions are the 2026-12-03 issue/registry drift check, the
2027-02-01 registry review and re-score, and the 2027-05-02 source refresh. The
ADR's archive condition can reverse the recurring decision at a later review.

## 7. Deviations and drift

| Deviation | Cause | Remedy |
| --- | --- | --- |
| `maintenance.html` returned 404 immediately after the merge | The docs deploy had not finished propagating | Rechecked after the deploy job completed; the page returns HTTP 200 and is linked from the index |
| 21 DOI sources report `blocked` | Publisher pages refuse automated clients with HTTP 403 | Recorded as blocked, not broken or verified; the first review names the hosts |
| `CARB-03` remains adopted but unmerged | FHOPS pull #383 is open with CI success | Recorded as an open target record; no target object was changed |

## 8. What remains unverified

- A reachable source URL does not prove the content, licence, or scientific
  claim. The refresh is reachability evidence only.
- A live target record does not prove that the target test suite or science
  passes. `complete`, `adopted`, and `queued` describe the live record, not an
  independent re-validation.
- Readiness scores remain screening judgements, not author-confirmed estimates.
- CI, Pages, and live-target checks are a 2026-11-03 snapshot. A later target
  merge, outage, or workflow change is outside this evidence.
- No tag, release, package-index artifact, or DOI was created in P6.

## 9. Close-out record

- The maintainer approved the P6 merge, branch deletion, and issue closures on
  2026-11-03.
- Pull request #39 squash-merged to `main` at
  `625e354dc6d8e3d9538189bb8b984346f258cbeb` (`625e354`) on 2026-11-03.
- `feature/p6-operate` was deleted after the merge, locally and on `origin`.
- Issues #35-#38 were closed with closeout comments citing the task commits, the
  gate evidence, and the merge commit.
- `main` CI run 41739271892 and Docs run 41739271917 passed on `625e354`; the
  Docs deploy job succeeded and the Pages index, `maintenance.html`,
  `register.html`, `releases.html`, `candidates.md`, and `llms.txt` returned
  HTTP 200.
- P6 is `complete` in `ROADMAP.md`, `README.md`, and `CHANGE_LOG.md`.
- No tag was created, no release was published, and no repository setting
  changed. No target-repository issue, branch, or pull request was created or
  edited.
