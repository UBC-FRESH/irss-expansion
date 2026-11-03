# Phase close-out report: P3 Build

Phase: P3 Build
Parent issue: #19
Pull request: [#24](https://github.com/UBC-FRESH/irss-expansion/pull/24),
`feature/p3-build` into `main`
Evidence head: `bc27c5b` (P3.4), plus the PR-record commit
Date: 2026-11-03
Status: PR queued for maintainer review; not merged, no target-repository action
taken

## Recommendation

Approve these actions after reviewing the pull request:

1. Merge the P3 pull request into `main` and delete `feature/p3-build` when the
   phase close-out is approved.
2. Close parent issue #19 and child issues #20-#23 with closeout comments that
   cite the P3 commits and the gate evidence.
3. Keep the `femic` P117.2 handoff queued. Updating issue #376, creating a target
   branch or pull request, or implementing the biomass curve family needs a
   **separate** maintainer approval.

Settings changes, each with its exact command. None run in P3.

- None. P3 changes no repository setting, visibility, tag, release, or external
  account, and creates no target-repository issue, branch, or pull request.

## 1. Objectives and acceptance

| Criterion | Evidence | Status |
| --- | --- | --- |
| The model-integration candidates are re-scored against current evidence | `notes/20-p3-model-integration-rescore.md`: 26 rows, six score changes, live target URLs and states | met |
| The first candidate has a reviewed handoff body and a named target repository | `handoffs/femic-child-biomass-curves-p3.md`; target `UBC-FRESH/femic` P117.2 (#376) | met |
| The candidate's provenance, validation boundary, and limits are explicit | Handoff sections "Provenance", "Validation boundary", and "Limits"; source DOI and target issue links | met |
| The target repository, phase number, and acceptance test are confirmed | Note 20 "Target confirmation" and "Confirmation record"; `femic` P117 is active, #376 is open, branch `feature/p117-efi-attributes` at `67cba53` | met |
| No new general model is proposed as integration work | `GRO-06` consumes Tompalski et al. (2024) and declares one pilot species/BEC; no refit, no belowground addition, no new remote-sensing study | met |
| `python scripts/check_workflow.py`, `check_registry.py`, and `dashboard.py` pass | Section 3 | met |

## 2. Workflow compliance

- Parent issue #19 and child issues #20-#23 existed before `feature/p3-build`
  was created from `main` at `e37ac5c`.
- Commit messages start with the task ID: `635cb82` P3.1, `b4794e6` P3.2,
  `6a81086` P3.3, and the report commit P3.4.
- `ROADMAP.md`, `CHANGE_LOG.md`, `notes/`, the handoff, and the issue bodies are
  in step. P3 is `pr-open` after the pull request opens.
- No target-repository issue, branch, or pull request was created or edited. The
  handoff body is written for the existing `femic` #376; it is not a new issue.
- No candidate was queued for implementation in a target repository. `GRO-06`
  remains `queued` in this registry.

## 3. Gate evidence

| Commit | Gate run | Result |
| --- | --- | --- |
| `635cb82` P3.1 | `python scripts/check_registry.py`; `python scripts/render_registry.py`; `git diff --exit-code docs/candidates.md`; `python scripts/dashboard.py` | 62 valid candidates; renderer idempotent; all six gates GREEN |
| `b4794e6` P3.2 | `python scripts/check_workflow.py`; `python scripts/dashboard.py` | 0 errors, 0 warnings; all six gates GREEN |
| `6a81086` P3.3 | `python scripts/check_workflow.py`; `python scripts/dashboard.py` | 0 errors, 0 warnings; all six gates GREEN |
| Report commit P3.4 | `python scripts/check_registry.py`; `python -m pytest -q`; `python scripts/dashboard.py` | recorded in the changelog; CI on the pull request is the public evidence |

## 4. Decision summary

| Field | Value |
| --- | --- |
| Selected candidate | `GRO-06` Biomass yield curves from time-series remote sensing |
| Carried score | 5.00 (M / impact 5 / readiness 4 / risk 2), unchanged |
| Target repository | [`UBC-FRESH/femic`](https://github.com/UBC-FRESH/femic) |
| Target phase | P117 EFI Inventory Attributes and Biomass Curves, [#374](https://github.com/UBC-FRESH/femic/issues/374), active |
| Target task | P117.2, [#376](https://github.com/UBC-FRESH/femic/issues/376), open |
| Branch | `feature/p117-efi-attributes` at `67cba53` |
| Handoff | [`handoffs/femic-child-biomass-curves-p3.md`](../../handoffs/femic-child-biomass-curves-p3.md) |
| Re-score note | [`notes/20-p3-model-integration-rescore.md`](../20-p3-model-integration-rescore.md) |
| Acceptance command | `python -m pytest tests/test_biomass_curves.py -q` in `femic` |

The selection prefers an existing target phase and acceptance path over opening
a new target phase, as the P2 close-out recommended. It also avoids the open
FHOPS P44 salvage work, the incomplete `INV-09` route graph, and the unmet
wave-3 dependencies of `OPS-01`.

## 5. Re-score result

26 rows were checked: the 25 wave-2 candidates plus `GRO-06`. Six readiness
values changed; no impact, effort, risk, or wave value changed.

| ID | Change | Reason |
| --- | --- | --- |
| `INV-09` | readiness 3 -> 4 | `fresh-road` status contract and two ALS pilots exist; the remaining gap is the WS4 consumer |
| `GRO-02` | readiness 3 -> 4 | Climate and curve-uncertainty contracts are merged |
| `GRO-03` | readiness 3 -> 4 | Climate and disturbance contracts are merged |
| `PLAN-05` | readiness 3 -> 2 | `fresh-road` TSA 23 graph still has 779 components and 2,793 unrouted blocks |
| `OPS-05` | readiness 3 -> 2 | Depends on `INV-09`, whose WS4 join is not complete |
| `DATA-05` | readiness 3 -> 4 | `DATA-01` and `INV-01` are complete |

## 6. Deviations and drift

| Item | Evidence | Treatment |
| --- | --- | --- |
| `CARB-03` is adopted but not merged | FHOPS P44 #380 and PR #383 are open with CI green | Kept `adopted` as "taken up", corrected the resolution to say the PR is open |
| `OPS-01` has wave-3 dependencies | `INV-02` and `INV-07` remain wave-3 candidates | Recorded as not selectable; did not change its wave |
| `DIS-09`, `OPS-03`, `OPS-05` overlap or depend on open work | FHOPS P44 and `INV-09` are in flight | Not selected; no parallel handoff |
| WS4 roadmap statuses lag merged evidence | Some closed issues still say `pr-open` in the live roadmap | Recorded as target drift; not changed here |
| `GRO-06` target issue already exists | `femic` #376 is open | The handoff body is for that issue; no new issue was created |

## 7. What remains unverified

- The target repository's tests were not run. The acceptance test file
  `tests/test_biomass_curves.py` does not exist yet and is a deliverable, so the
  command is expected to fail until implementation.
- The published biomass curve family was not selected or encoded. The handoff
  names the source and the boundary, not the final species/BEC choice.
- The live state is a 2026-11-03 snapshot. The target roadmap must be re-read
  before any implementation starts.
- The re-score is a screening judgement. It did not re-run target test suites or
  independently re-validate target science.

## 8. Next action

Wait for the maintainer to review the P3 pull request. After approval:

1. Merge the pull request and close #19-#23 with the closeout evidence.
2. Decide separately whether to update `femic` #376 with the reviewed handoff
   body and start P117.2. That decision is the target-repository approval gate,
   not part of P3.
