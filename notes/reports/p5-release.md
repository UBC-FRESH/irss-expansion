# Phase close-out report: P5 Release and deploy

Phase: P5 Release and deploy
Parent issue: #30
Pull request: [#34](https://github.com/UBC-FRESH/irss-expansion/pull/34),
`feature/p5-release` into `main`
Evidence head: `fb6354d` (P5.2), plus the merge commit and this close-out commit
Date: 2026-11-03
Status: approved by the maintainer on 2026-11-03; squash-merged to `main` as
`d3d5ce2`, tagged `v0.1.0`, and released.

## Recommendation

The maintainer approved these actions on 2026-11-03; the close-out record is
section 9.

1. Squash-merge the P5 pull request into `main` and delete `feature/p5-release`.
2. Close parent issue #30 and child issues #31-#33 with closeout comments that
   cite the P5 commits, the gate evidence, the merge commit, the tag, and the
   release.
3. Create the annotated tag `v0.1.0` on the P5 merge commit, push it, and create
   the GitHub release `IRSS x Silva21 Expansion Mine 0.1.0` from
   `notes/23-p5-release-notes.md`.
4. Keep `GRO-06` queued under `femic` P117.2 (#376) and keep `CARB-03` as an
   in-flight adoption under FHOPS P44. Either follow-up needs a separate
   maintainer approval.
5. Launch P6 only after a separate approval. P6 remains `planned` with no parent
   issue, child issues, or branch.

Settings changes, each with its exact command. None ran.

- None. P5 changes no repository visibility, Pages configuration, branch
  protection, environment, external account, or package-index artifact. The tag
  and release are the only new public objects.

## 1. Objectives and acceptance

| Criterion | Evidence | Status |
| --- | --- | --- |
| The public repository shows the register, the validator, and the workflow files | Clean clone at `2f013b3` in P5.2 shows `registry/candidates.yaml`, `docs/candidates.md`, `scripts/check_workflow.py`, and both workflow files; Pages serves the register, `releases.html`, and `llms.txt` with HTTP 200 | met |
| A clean checkout reproduces the dashboard result | P5.2 fresh clone and fresh virtual environment: six gates GREEN, 186 tests passed with 100% branch coverage | met |
| Release actions are approved and recorded one at a time | The maintainer approved the merge in the P5 activation packet and approved the tag and release on 2026-11-03; sections 4 and 9 record each action with its command and result | met |
| `check_workflow.py`, `check_registry.py`, and `dashboard.py` pass | Section 3 | met |

## 2. Workflow compliance

- Parent issue #30 and child issues #31-#33 existed before `feature/p5-release`
  was created from `main` at `c05d955`.
- Commit messages start with the task ID: `2f013b3` P5.1, `7fd9465`, `c03dc78`,
  and `fb6354d` P5.2.
- `ROADMAP.md`, `CHANGE_LOG.md`, the P5 notes, this report, and the issue bodies
  are in step. P5 was `pr-open` while the pull request was open and is `complete`
  after the close-out commit.
- No target-repository issue, branch, pull request, tag, or setting was created
  or edited. All target checks were read-only.
- No candidate was implemented, queued in a target repository, re-scored, or
  retired. `GRO-06` remains `queued`; `CARB-03` remains `adopted` and in flight.
- Approval gates: the merge, branch deletion, issue closures, tag, and release
  each followed an explicit maintainer approval. P6 is not activated.

## 3. Gate evidence

| Commit | Gate run | Result |
| --- | --- | --- |
| `2f013b3` P5.1 | `check_workflow.py`; `check_registry.py`; `render_registry.py`; `git diff --exit-code docs/candidates.md`; `pytest -q`; `dashboard.py` | 0 errors/0 warnings; 62 valid candidates; renderer idempotent; 186 passed with 100% branch coverage; all six gates GREEN |
| `2f013b3` P5.1, clean clone | The same six commands in a fresh virtual environment | 0 errors/0 warnings; 62 valid candidates; renderer idempotent; 186 passed with 100% branch coverage; all six gates GREEN |
| `7fd9465`, `c03dc78`, `fb6354d` P5.2 | `check_registry.py`; `render_registry.py`; `git diff --exit-code docs/candidates.md`; `dashboard.py` | 62 valid candidates; renderer idempotent; all six gates GREEN; P5.2 note and roadmap updates |
| P5 close-out commit | The same six-command sequence | recorded in `CHANGE_LOG.md`; `main` CI and Docs runs pass on the merge commit |

## 4. Merge, tag, and release evidence

| Action | Command | Result |
| --- | --- | --- |
| Squash merge | `gh pr merge 34 --squash --delete-branch` | Pull request #34 merged 2026-11-03T22:25:11Z as `d3d5ce2311adc3e32b7b78535b04dc4acea12a9b` (`d3d5ce2`) |
| Branch deletion | included in the merge command | `origin/feature/p5-release` and the local branch deleted; `git branch -a` lists only `main` |
| Annotated tag | `git tag -a v0.1.0 -m "IRSS x Silva21 Expansion Mine 0.1.0" d3d5ce2` | tag object `999a85e459b57afe27deba03db223afeb00ef37b` points at commit `d3d5ce2` |
| Tag push | `git push origin v0.1.0` | pushed to `origin`; `git ls-remote --tags origin` reports `refs/tags/v0.1.0` |
| GitHub release | `gh release create v0.1.0 --title "IRSS x Silva21 Expansion Mine 0.1.0" --notes-file notes/23-p5-release-notes.md` | <https://github.com/UBC-FRESH/irss-expansion/releases/tag/v0.1.0> |

The tag targets the P5 merge commit on `main`, not the branch head or the
close-out commit. `CITATION.cff` already named version `0.1.0` with
`date-released: 2026-11-03`, so no citation metadata changed.

## 5. CI and Pages evidence

| Run ID | Head commit | Conclusion | Notes |
| --- | --- | --- | --- |
| [41729716594](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41729716594) | `fb6354d` | success | P5 pull request; Quality gates, Green dashboard summary, and Pre-commit parity all succeed |
| [41730635925](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41730635925) | `d3d5ce2` | success | `main` push; Quality gates, Green dashboard summary, and Pre-commit parity all succeed |
| [41730636142](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41730636142) | `d3d5ce2` | success | `main` push; Docs build and deploy both succeed |

The public Pages site returned HTTP 200 on 2026-11-03 for the index,
`releases.html`, `register.html`, `candidates.md`, and `llms.txt` after the
`d3d5ce2` deployment. P5.2 recorded `releases.html` as 404 before the merge; the
page exists after the docs deploy, which closes that boundary.

## 6. Release contents and programme status

The release is a public-safe planning artefact. It carries the register (62
candidates in nine workstreams), the validators and tests that protect it, the
dashboard, the docs site, the roadmap and changelog, the notes, and the handoff
drafts. It is not a forest model, a simulator, or a Python package: there is no
`[project]` table, no package-index artifact, and no DOI.

Register status at close-out: 17 `complete`, 2 `adopted`, 1 `queued`, 14
`shortlisted`, 23 `candidate`, 4 `deferred`, 1 `rejected`; 62 candidates in
total. No candidate was re-scored or retired in P5.

Programme status at close-out: P0-P5 are complete and merged. P6 operate and
maintain is `planned` with no parent issue, child issues, or branch, and needs a
separate approval to activate.

## 7. Deviations and drift

| Deviation | Cause | Remedy |
| --- | --- | --- |
| `releases.html` returned 404 before the merge | The page was on the unmerged P5 branch | P5.2 recorded the boundary; the post-merge docs deploy now serves it with HTTP 200 |
| `notes/23-p5-release-notes.md` described an untagged candidate at P5.1 | P5.3 had not run when the note was written | P5.3 updated the release-status block, the citation line, the first known gap, and section 7 before publishing; the other nine gaps are intact |
| `CARB-03` is adopted but not merged | FHOPS P44 #380/#381 and PR #383 remain open with CI green | Kept `adopted` as "taken up"; recorded the open state and a revisit trigger |
| `GRO-06` is queued, not implemented | `femic` P117.2 (#376) is open | Kept `queued`; no target-repository object was created from this repository |

## 8. What remains unverified

- No package-index artifact exists and no DOI is minted. The release is the tag
  and the GitHub release page.
- `CARB-03` is not merged, and `GRO-06` is not implemented. Their target
  repositories own the next step.
- No target-repository test suite was run. "Complete" and "adopted" mean the
  cited live record exists; they are not an independent re-validation of target
  science.
- The mine remains metadata and abstract level. Readiness scores are screening
  judgements, not author-confirmed estimates.
- CI, Docs, Pages, and live-target checks are a 2026-11-03 snapshot. A later
  target merge, outage, or workflow change is outside this evidence.
- P6 operate and maintain has not started: no review cadence, re-score, or
  recurring-or-one-off decision is recorded.

## 9. Close-out record

- The maintainer approved the P5 merge, the `v0.1.0` tag, and the
  `IRSS x Silva21 Expansion Mine 0.1.0` release on 2026-11-03.
- Pull request #34 squash-merged to `main` at
  `d3d5ce2311adc3e32b7b78535b04dc4acea12a9b` (`d3d5ce2`) on 2026-11-03.
- `feature/p5-release` was deleted after the merge, locally and on `origin`.
- Issues #30-#33 were closed with closeout comments citing the task commits, the
  gate evidence, the merge commit, the tag object, and the release URL.
- The annotated tag `v0.1.0` (object `999a85e`) points at `d3d5ce2` and is pushed
  to `origin`.
- The GitHub release is
  <https://github.com/UBC-FRESH/irss-expansion/releases/tag/v0.1.0>.
- `main` CI run 41730635925 and Docs run 41730636142 passed on `d3d5ce2`; the
  Docs deploy job succeeded and the Pages index, `releases.html`, `register.html`,
  `candidates.md`, and `llms.txt` returned HTTP 200.
- P6 was not activated. `AGENTS.md` requires a separate maintainer approval
  before its parent issue, child issues, or `feature/p6-operate`.
- No target-repository issue, branch, or pull request was created or edited, and
  no repository setting changed.
