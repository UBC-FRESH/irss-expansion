# Phase close-out report: P4 Verify

Phase: P4 Verify
Parent issue: #25
Pull request: [#29](https://github.com/UBC-FRESH/irss-expansion/pull/29),
`feature/p4-verify` into `main`
Evidence head: `193738b` (P4.2), plus the P4.3 report and record commits
Date: 2026-11-03
Status: approved by the maintainer on 2026-11-03; squash-merged to `main` as `ee94e8e`.

## Recommendation

The maintainer approved these actions on 2026-11-03; the close-out record is section 9.

1. Squash-merge the P4 pull request into `main` and delete `feature/p4-verify`.
2. Close parent issue #25 and child issues #26-#28 with closeout comments that
   cite the P4 commits, the gate evidence, and the merge commit.
3. Keep `GRO-06` queued under `femic` P117.2 (#376) and keep `CARB-03` as an
   in-flight adoption under FHOPS P44. Either follow-up needs a separate
   maintainer approval.
4. Launch P5 only after a separate approval: create its parent issue and child
   issues, create `feature/p5-release`, and start P5.1.

Settings changes, each with its exact command. None run in P4.

- None. P4 changes no repository setting, visibility, tag, release, or external
  account, and creates no target-repository issue, branch, or pull request.

## 1. Objectives and acceptance

| Criterion | Evidence | Status |
| --- | --- | --- |
| The dashboard and CI pass on the head commit | P4.1 and P4.2 local dashboards all six gates GREEN; `main` CI run [41721924289](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41721924289) and Docs run [41721924173](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41721924173) pass on `8b23206`; the P4 pull request CI run is the final-head evidence | met |
| Every completion claim cites a commit, pull request, or issue | `notes/22-p4-candidate-reconciliation.md` section 1 gives a live issue and merged PR/commit for each of the seventeen `complete` candidates; sections 2 and 3 cover `CARB-01`, `CARB-03`, and `GRO-06` | met |
| The close-out report states what remains unverified | Sections 6 and 8 | met |
| `check_workflow.py`, `check_registry.py`, and `dashboard.py` pass | Section 3 | met |
| The carried queue and its evidence meet the acceptance criteria | P4.1 local, CI, Docs, Pages, and clean-checkout evidence; P4.2 live-target reconciliation | met |

## 2. Workflow compliance

- Parent issue #25 and child issues #26-#28 existed before
  `feature/p4-verify` was created from `main` at `8b23206`.
- Commit messages start with the task ID: `bd89a02` P4.1, `193738b` P4.2, and
  the P4.3 report and record commits.
- `ROADMAP.md`, `CHANGE_LOG.md`, the P4 notes, the report, and the issue bodies
  are in step. P4 is `pr-open` after the pull request opens.
- No target-repository issue, branch, pull request, or setting was created or
  edited. All target checks were read-only.
- No candidate was implemented, queued in a target repository, re-scored, or
  retired. `GRO-06` remains `queued`; `CARB-03` remains `adopted` and in flight.
- Approval gates: the maintainer approved P4 activation and implementation. The
  merge, branch deletion, issue closures, and P5 launch remain separate actions.

## 3. Gate evidence

| Commit | Gate run | Result |
| --- | --- | --- |
| `bd89a02` P4.1 | `check_workflow.py`; `check_registry.py`; `render_registry.py`; `git diff --exit-code docs/candidates.md`; `pytest -q`; `dashboard.py` | 0 errors/0 warnings; 62 valid candidates; renderer idempotent; 186 passed with 100% branch coverage; all six gates GREEN |
| `193738b` P4.2 | `check_registry.py`; `render_registry.py`; `git diff --exit-code docs/candidates.md`; `dashboard.py` | 62 valid candidates; renderer idempotent; all six gates GREEN |
| P4.3 report commit | `check_workflow.py`; `check_registry.py`; `render_registry.py`; `git diff --exit-code docs/candidates.md`; `pytest -q`; `dashboard.py` | recorded in `CHANGE_LOG.md`; CI run 41723466038 passes on `b53338b` |

The P4.2 first validator run caught a broken relative link in
`notes/22-p4-candidate-reconciliation.md` (`../../handoffs/` instead of
`../handoffs/`). It was corrected before the commit; no gate was weakened.

## 4. CI evidence

| Run ID | Head commit | Conclusion | Notes |
| --- | --- | --- | --- |
| [41721924289](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41721924289) | `8b23206` | success | `main` push; Quality gates, Green dashboard summary, and Pre-commit parity all succeed |
| [41721924173](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41721924173) | `8b23206` | success | `main` push; Docs build and deploy both succeed |
| [41723466038](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41723466038) | `b53338b` | success | P4 pull request; Quality gates, Green dashboard summary, and Pre-commit parity all succeed |

The public Pages site returned HTTP 200 on 2026-11-03 for the index,
`register.html`, `candidates.md`, and `llms.txt`. A clean clone of the public
repository at `8b23206` reproduced the six-gate GREEN dashboard.

## 5. Candidate reconciliation and programme status

P4.1 verified the acceptance surface. P4.2 reconciled every candidate whose
status claims completion, adoption, or queueing:

| Status | Count | Result |
| --- | ---: | --- |
| `complete` | 17 | every row has a closed target issue and merged evidence |
| `adopted` | 2 | `CARB-01` is adopted and merged; `CARB-03` is adopted and in flight in FHOPS P44 |
| `queued` | 1 | `GRO-06` remains queued under open `femic` P117.2 (#376) |

Full register status counts at close-out: 17 `complete`, 2 `adopted`, 1
`queued`, 14 `shortlisted`, 23 `candidate`, 4 `deferred`, 1 `rejected`; 62
candidates in total.

No candidate was re-scored or retired. The live target heads match the P3
snapshot, so the P3 readiness values remain current. No record contradicted a
carried status. `CARB-03` was checked rather than assumed: FHOPS #380, #381, and
PR #383 are open, with CI green and the pull request mergeable, but there is no
merge commit.

Programme status at close-out: P0-P3 are complete and merged; P4 verification is
complete on the pull request branch and waits for approval; P5 release and
deploy and P6 operate and maintain remain planned. No candidate was handed to a
target roadmap in P4.

## 6. Deviations and drift

| Deviation | Cause | Remedy |
| --- | --- | --- |
| `CARB-03` is adopted but not merged | FHOPS P44 #380/#381 and PR #383 remain open with CI green | Kept `adopted` as "taken up"; recorded the open state and a revisit trigger |
| FHOPS P44 has no roadmap section | Issue #380 names `ROADMAP.md` Phase 44, but the live FHOPS roadmap has no Phase 44 section | Recorded as target drift; not changed from this repository |
| `ws4` PR #408 title says P57, while issue and roadmap say P58 | The pull request title predates the phase renumbering | The P2 correction to P58 still holds; recorded again |
| The P4.2 note first had a broken relative link | The handoff path was written one directory too high | Corrected before the P4.2 commit; the validator then reported 0 errors |

## 7. What remains unverified

- `CARB-03` is not merged. The P4 check covers the open PR state, CI, and
  mergeability, not the target implementation or its tests.
- `GRO-06` is not implemented. P4 verified the queued issue, branch, and missing
  acceptance test, not the biomass science or a pilot species/BEC choice.
- No target repository test suite was run. "Complete" and "adopted" mean the
  cited live record exists; they are not an independent re-validation of target
  science.
- P4 did not re-mine IRSS or Silva21 sources, change a score, or retire a
  candidate. The readiness values are the P3 screening judgements.
- The Pages and live-target checks are a 2026-11-03 snapshot. A later target
  merge or site outage is outside this evidence.
- P5 release and deploy, the release notes, the clean public checkout of the
  final release, and any tag or release action have not started.

## 8. Next action

The P4 close-out is complete. The remaining decisions are separate from P4:

1. Follow up `CARB-03` in FHOPS P44 and `GRO-06` in `femic` P117.2 under those
   repositories' workflows and approval rules.
2. Approve P5 release and deploy separately before creating its parent issue,
   child issues, or `feature/p5-release`. The default next steps are to write
   the release notes and known-gaps list (P5.1), verify the public register and
   docs from a clean checkout (P5.2), and then approve the tag and publish
   action on its own (P5.3). No P5 branch, issue, tag, or release exists yet.

## 9. Close-out record

- The maintainer approved the P4 close-out on 2026-11-03.
- Pull request #29 squash-merged to `main` at `ee94e8eb935f394d5794e772c47ef55737c73957`
  (`ee94e8e`) on 2026-11-03.
- `feature/p4-verify` was deleted after the merge.
- Issues #25-#28 were closed with closeout comments citing the task commits, the
  gate evidence, and merge commit `ee94e8e`.
- Pull request CI run 41723687615 passed Quality gates, Green dashboard summary,
  and Pre-commit parity on the final P4 head.
- `main` CI run 41727688181 and Docs run 41727687763 passed on `ee94e8e`; the
  Docs deploy job succeeded and the Pages index, `register.html`,
  `candidates.md`, and `llms.txt` returned HTTP 200.
- P5 governance was not created. The P4 close-out approved the merge and issue
  closures only; `AGENTS.md` and the recommendation above require a separate
  maintainer approval before the P5 parent issue, child issues, branch, tag, or
  release are created.
- No target-repository issue, branch, or pull request was created or edited.
