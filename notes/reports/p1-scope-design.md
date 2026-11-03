# Phase close-out report: P1 Scope and design

Phase: P1 Scope and design
Parent issue: #7
Pull request: #12, `feature/p1-scope-design` into `main`
Evidence head: `320809e` (P1.4), the head that the gates in section 7 cover
Report commit: the commit that adds this report. Its CI run is posted on the pull request.
Date: 2026-11-03
Status: approved by the maintainer on 2026-11-03; squash-merged to `main` as `2b4620d`.

## Recommendation

Approve these actions. The agent carries them out in this order, and reads back each result.

1. Squash-merge pull request #12, and delete the branch `feature/p1-scope-design`.
2. Close parent issue #7 and child issues #8-#11 with a closeout comment that cites the merge commit.
3. Launch P2 Contracts and prototype from the merged `main`.

Settings changes, each with its exact command. Each one runs only after its own approval.

- None. This phase changes no repository setting, visibility, tag, release, or external account.

## 1. Objectives and acceptance

| Criterion | Evidence | Status |
| --- | --- | --- |
| The scope rule and out-of-scope list are current and linked from `README.md` | P1.1 review in `notes/06-out-of-scope.md`; direct link in the `README.md` scope rule | met |
| Every new decision has an accepted or deferred ADR | No design decision changed; section 3 records why no new ADR is required | met |
| Readiness remains a documented integration judgement, not a claim about the science | `notes/04-prioritization.md` review keeps the caveat; no score or status changed | met |
| `python scripts/check_workflow.py` and `python scripts/dashboard.py` pass on the P1 head | section 5 | met |
| The source inventory and publication signals are reviewed | P1.2 sections in `notes/00-source-inventory.md` and `notes/02-publication-signals.md` | met |
| The notes index lists every carried note | `notes/README.md` now lists the readiness notes 15 and 16 | met |

## 2. Scope and out-of-scope confirmation (P1.1)

- The scope rule in `README.md` is unchanged: a candidate must consume an existing provincial
  product, published model, dataset, reference implementation, or partner coefficient set with
  clear provenance and a validation boundary. A new general growth, height, site-index, carbon,
  disturbance, or remote-sensing model remains out of scope.
- `notes/06-out-of-scope.md` still lists the two deferred register entries (`CARB-04`,
  `PLAN-06`) and the screened-out material, each with a revisit trigger. No entry was added,
  removed, or re-scored.
- The only wording change is a direct link from the README scope rule to
  `notes/06-out-of-scope.md`, so the reader no longer has to reach the list through the later
  "What is deliberately out of scope" section.

## 3. Design decision (P1.3)

No new ADR is required. P1 confirmed the existing scope rule, out-of-scope list, and scoring
rubric; it did not change a boundary, a target repository, a scoring formula, or a candidate
status. The accepted contract-wave decisions and the ADR template are unchanged.

The task instruction is explicit: an ADR records a decision, not a confirmation. This report is
the no-decision record. A future change to the scope rule, a new integration boundary, or a
changed scoring formula must add a numbered ADR under `notes/adr/` with status `accepted` or
`deferred`.

## 4. Source inventory and publication signals (P1.2)

- All 22 public source URLs in `notes/00-source-inventory.md` returned HTTP 200 on 2026-11-03.
- The current pages confirm 493 IRSS publication records (2004-2023), 47 Silva21 project pages,
  12 hubs, 65 unique DOI-linked scientific publications, and 62 registry candidates.
- The Silva21 extension-note count was corrected from 14 to 16 notes across 15 volumes. Volume 6
  is published as two issues, so the earlier figure counted volume numbers rather than notes.
- The 44 candidate references in `notes/02-publication-signals.md` all match IDs in
  `registry/candidates.yaml`; no candidate link was stale or renamed.
- `notes/README.md` now lists the carried readiness notes `15-dec02-readiness.md` and
  `16-dis03-readiness.md`.
- No source was re-mined, no candidate evidence changed, and no score changed.

## 5. Scoring rubric confirmation (P1.4)

- The formula `priority = (impact * readiness) / (effort_points * risk)` matches
  `priority_score` in `scripts/check_registry.py`, including the S/M/L/XL effort map and
  two-decimal rounding.
- The impact, readiness, effort, and risk rubrics are unchanged, and a wave remains a dependency
  and sequencing judgement rather than a score threshold.
- All 13 first-wave rows match the validator output on ID, score, and effort code. The registry
  wave counts are 2 in wave 0, 13 in wave 1, 25 in wave 2, and 22 in wave 3.
- No candidate was re-scored and no wave changed. Readiness remains an integration judgement,
  not an author-confirmed science claim.

## 6. Workflow compliance

- Parent issue before the branch: #7 and children #8-#11 were created before
  `feature/p1-scope-design`; the branch was created from the merged `main` at `aacd102`.
- Commit messages that start with task IDs: `f9cdc7d` P1.1, `8eafb8c` P1.2, `050dfd9` P1.3,
  `320809e` P1.4.
- Roadmap and changelog in step: each task updates `CHANGE_LOG.md`; the roadmap status is
  updated when the phase activates and when the pull request opens.
- Child issues closed with closeout evidence: issues #7-#11 are closed with comments that cite
  each task commit, the gate result, pull request #12, and the merge commit `2b4620d`.
- Approval gates: no target-repository issue, branch, or pull request was created; no candidate
  was queued; no tag, release, visibility change, or settings change was made.

## 7. Gate evidence

| Commit | Gate run | Result |
| --- | --- | --- |
| `f9cdc7d` P1.1 | `python scripts/check_workflow.py`; `python scripts/dashboard.py` | 0 errors and 0 warnings; all six gates GREEN |
| `8eafb8c` P1.2 | `python scripts/check_workflow.py`; `python scripts/check_registry.py`; `python scripts/dashboard.py` | 0 errors and 0 warnings; 62 valid candidates; all six gates GREEN |
| `050dfd9` P1.3 | `python scripts/check_workflow.py`; `python scripts/dashboard.py` | 0 errors and 0 warnings; all six gates GREEN |
| `320809e` P1.4 | `python scripts/check_workflow.py`; `python scripts/check_registry.py`; `python scripts/dashboard.py` | 0 errors and 0 warnings; 62 valid candidates; all six gates GREEN |

## 8. CI evidence

| Run ID | Head commit | Conclusion | Notes |
| --- | --- | --- | --- |
| 41705451883 | `2cfb2a4` | success | Quality gates, Green dashboard summary, and Pre-commit parity all pass. The report-update commit triggers its own run, visible on the same pull request. |
| 41705264296 | `320809e` | success | The P1.4 head passes the same three jobs. |

## 9. Deviations

| Deviation | Cause | Remedy |
| --- | --- | --- |
| The carried extension-note count said 14 | The source page publishes Volume 6 as two issues | P1.2 corrects the count to 16 notes across 15 volumes |
| The notes index omitted the two readiness notes | The index was carried before notes 15 and 16 were added | P1.2 adds both entries |

## 10. Next phase

P2 Contracts and prototype remains `planned`. After the P1 merge and close-out approval:

- Create `feature/p2-contracts-prototype` from the merged `main`.
- Activate P2 under parent issue #13 and start P2.1.
- Audit the contract-wave records against the live target repositories.

P2 parent issue #13 and child issues #14-#17 now exist. P2 remains `planned`; activation and branch creation await maintainer approval.

## 11. Decision

- [x] Approve as written.
- [ ] Approve with the changes stated here: <changes>.

## 12. Close-out record

- Pull request #12 squash-merged to `main` at `2b4620d` on 2026-11-03.
- `feature/p1-scope-design` was deleted after the merge.
- Issues #7-#11 were closed with closeout comments citing `2b4620d`.
- `main` CI run 41710569721 and Docs run 41710569637 pass on `2b4620d`; the Pages site returns HTTP 200.
- P2 governance was created as parent issue #13 and child issues #14-#17. P2 remains `planned`; no P2 branch or implementation exists.
