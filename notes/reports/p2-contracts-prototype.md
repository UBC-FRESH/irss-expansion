# Phase close-out report: P2 Contracts and prototype

Phase: P2 Contracts and prototype
Parent issue: #13
Pull request: [#18](https://github.com/UBC-FRESH/irss-expansion/pull/18), `feature/p2-contracts-prototype` into `main`
Evidence head: `2e6b25b` (P2.4), the head that the gates in section 3 cover
Report commit: the commit that adds this report. Its CI run is posted on the pull request.
Date: 2026-11-03
Status: queued for approval. Not merged.

## Recommendation

Approve these actions. The agent carries them out in this order, and reads back each result.

1. Squash-merge pull request #18, and delete `feature/p2-contracts-prototype`.
2. Close parent issue #13 and child issues #14-#17 with a closeout comment that cites the merge commit.
3. Launch P3 Build: create its branch, set the phase statuses in `ROADMAP.md`, create its child issues as sub-issues, and start its first task.

Settings changes, each with its exact command. Each one runs only after its own approval.

- None. This phase changes no repository setting, visibility, tag, release, or external account.

## 1. Objectives and acceptance

| Criterion | Evidence | Status |
| --- | --- | --- |
| Every completed contract candidate points at merged evidence in its target repository | `notes/17-p2-contract-audit.md`, audit table; eleven complete or adopted rows cite live issues, pull requests, and merge commits | met |
| Every open candidate states its owner, first step, and unresolved dependency | `GRO-06` row in the registry and audit note: phase-level owner, first step, empty candidate dependency list, unresolved `femic#374`/`#376` | met with a stated limit: the live issue has no individual assignee |
| `python scripts/check_registry.py` and `python -m pytest` pass | section 3 | met |
| `python scripts/dashboard.py` reports every gate green on the P2 head | section 3 | met |
| The register matches the registry after the change | `docs/candidates.md` regenerated; `git diff --exit-code` against the staged file reports no change | met |

## 2. Workflow compliance

- Parent issue before the branch: #13 and child issues #14-#17 existed before `feature/p2-contracts-prototype`; the branch was created from the merged `main` at `d991dea`.
- Commit messages that start with task IDs: `4098217` P2.1, `ac26748` P2.2, `13f7a27` P2.3, and the report commit P2.4.
- Roadmap and changelog in step: each task updates `CHANGE_LOG.md`; P2.1 activates the phase and each task ticks its roadmap checkbox.
- Child issues closed with closeout evidence: not yet; they close after the merge, with comments citing the merge commit.
- Approval gates: no target-repository issue, branch, or pull request was created; no candidate was queued in a target repository; no tag, release, visibility change, or settings change was made.

## 3. Gate evidence

| Commit | Gate run | Result |
| --- | --- | --- |
| `4098217` P2.1 | `python scripts/check_workflow.py`; `python scripts/check_registry.py`; `python scripts/dashboard.py` | 0 errors and 0 warnings; 62 valid candidates; all six gates GREEN |
| `ac26748` P2.2 | `python scripts/dashboard.py`; `python -m pytest -q` | all six gates GREEN; 186 passed with 100% branch coverage of `scripts/` |
| `13f7a27` P2.3 | `python scripts/render_registry.py`; `git diff --exit-code -- docs/candidates.md`; `python scripts/check_registry.py` | render idempotent; 62 valid candidates |
| Report commit | `python scripts/check_workflow.py`; `python scripts/dashboard.py`; `python -m pytest -q` | recorded after the report commit; the CI run on the pull request is the public evidence |

## 4. CI evidence

| Run ID | Head commit | Conclusion | Notes |
| --- | --- | --- | --- |
| [41717081717](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41717081717) | `2e6b25b` | success | Quality gates, Green dashboard summary, and Pre-commit parity all pass. The report-update commit triggers its own run on the same pull request. |

## 5. Deviations

| Deviation | Cause | Remedy |
| --- | --- | --- |
| The carried `CARB-01` evidence called the ws4 carbon phase P51 | The phase was renumbered; live ws4 P51 is release-candidate verification | The registry and notes now cite live P58 and the audit note preserves the carried label |
| The carried `DEC-04` resolution said `femic#372` was open | Follow-up PR #418 merged the published cards and annotation seam | The resolution now cites #380 and #418; #372 is recorded closed |
| `DATA-02`, `DATA-04`, and `INV-06` resolutions were truncated before their issue and commit | The carried strings stopped at the repository name | The audit restores the issue, PR, and merge-commit citations |
| `GRO-06` has no individual GitHub assignee | The live issue is unassigned | The owner is recorded at the `femic` P117 phase level; no person was invented |
| `README.md` and `handoffs/README.md` carried stale open/active wording | The handoff text predates the merges | Both now cite the closed issues and merges |

## 6. Next phase

P3 Build is `planned`. After the P2 merge and close-out approval:

- Re-score the model-integration candidates against current evidence (P3.1).
- Select the first candidate and write its handoff issue body (P3.2).
- Confirm the target repository, phase number, and acceptance test (P3.3).
- Record the handoff decision in `CHANGE_LOG.md` (P3.4).

Recommended default: start with a model-integration candidate whose target phase and acceptance test already exist, rather than opening a new target phase. Do not create a target-repository issue or branch until the separate approval gate is met.

## 7. Decision

- [ ] Approve as written.
- [ ] Approve with the changes stated here: <changes>.
