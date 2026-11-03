# IRSS x Silva21 Expansion Mine Roadmap

This roadmap is the plan of record and the issue tracker map for the IRSS x Silva21
Expansion Mine. Keep it in step with the GitHub issues, `CHANGE_LOG.md`, and `notes/`.
`scripts/check_workflow.py` parses the phase headers, status lines, and checkboxes below,
so keep their format.

Every phase starts as `planned` with `Parent issue: TBD`. Activate a phase only after its
parent issue exists and the maintainer approves it.

This roadmap governs this planning repository. It does **not** replace the roadmaps in
`femic`, `ws3`, `ws4`, `fhops`, or `nemora`. Once a candidate is accepted, it becomes a
parent issue in its target repository and follows that repository's workflow, quality
gates, and approval rules.

## Issue Tracker Map

| Phase | Parent issue | Branch | Status |
| --- | --- | --- | --- |
| P0 Bootstrap and publish | #1 | `feature/p0-bootstrap` | complete |
| P1 Scope and design | #7 | `feature/p1-scope-design` | complete |
| P2 Contracts and prototype | #13 | `feature/p2-contracts-prototype` | complete |
| P3 Build | #19 | `feature/p3-build` | complete |
| P4 Verify | #25 | `feature/p4-verify` | pr-open |
| P5 Release and deploy | TBD | `feature/p5-release` | planned |
| P6 Operate and maintain | TBD | `feature/p6-operate` | planned |

## Lifecycle Map

| Stage | Phases | Exit criteria |
| --- | --- | --- |
| Scope and design | P0, P1 | The carried register and notes are public-safe; the scope rule and first decisions are recorded |
| Build | P2, P3 | Each task is committed with its task ID; each commit leaves the dashboard green; docs updated in the same change set |
| Verify | P4 | The dashboard and CI pass on the head commit; each acceptance criterion has evidence in the close-out report |
| Release and deploy | P5 | The register and docs are published; a clean checkout verifies them; each release action approved on its own |
| Operate and maintain | P6 | Review cadence held; candidates re-scored and retired; recurring or one-off status decided |
| Retire | P6 (procedure) | Archive notice, final changelog entry, and issues closed |

## Programme history carried from the planning draft

The source draft recorded four programme phases before this repository was seeded. That
history is carried here as evidence. It does not create parent issues in this repository,
and it does not override the workflow phases below.

| Source phase | Scope | Outcome |
| --- | --- | --- |
| Mine and publish the register | Source inventory, theme map, candidate register, validator | Complete; 62 candidates in nine workstreams, validated registry, generated register |
| Contract wave | Shared climate, disturbance, EFI model cards, and account contracts | Complete for `GRO-01`, `DIS-01`, `DEC-04`, `DATA-01`, `CARB-01` (adopted), `BIO-01`, `BIO-02`, `PLAN-03`, `DATA-02`, `DATA-04`, and `INV-06`; `GRO-06` remains queued under `femic` P117 |
| Model integration wave | Climate/dynamics, risk, carbon, habitat, and operations | Partly delivered through target-repo phases; the remaining candidates are shortlisted in the register |
| Frontier and validation wave | Continuous inventory, assisted migration, process modelling, multi-hub validation | Planned; no new remote-sensing model is scheduled |
| Programme review | Re-score, retire, and hand accepted work to target roadmaps | Planned; the 2026-11-01 reconciliation recorded the first completed set |

## Conventions

- A phase is `P<n>`. A task is `P<n>.<m>`. A subtask is a checklist item inside the task's issue body. Three levels at most.
- Status values are `planned`, `active`, `pr-open`, `complete`, and `deferred`.
- A phase becomes `complete` only after its pull request merges to `main` and its parent issue closes.
- The registry is the source of truth. `docs/candidates.md` is generated from it.
- A candidate is queued only after maintainer approval. No candidate in this repository creates a branch or issue in a target repository by itself.

## Phase 0: Bootstrap and publish

Parent issue: #1
Branch: `feature/p0-bootstrap`
Status: complete
Child issues: #2 P0.1, #3 P0.2, #4 P0.3, #5 P0.4
Next step: Complete. P0.1-P0.4 passed close-out and pull request #6 squash-merged to `main` with maintainer approval. Phase 1 starts from the merged `main`.

Goal: adapt the seeded contract to this project, carry the public-safe planning material, and make the first public state reviewable.

- [x] P0.1 Adapt `AGENTS.md` and `README.md` to this project
- [x] P0.2 Carry over the registry, notes, handoffs, register, scripts, and tests
- [x] P0.3 Confirm the workflow validator and the full dashboard pass
- [x] P0.4 Publish the repository and verify the remote

Acceptance criteria:

- `python scripts/check_workflow.py` reports no errors.
- `python scripts/dashboard.py` reports every gate green.
- Every carried file is public-safe, with no private data, credentials, caches, or machine-specific paths.

## Phase 1: Scope and design

Parent issue: #7
Branch: `feature/p1-scope-design`
Status: complete
Child issues: #8 P1.1, #9 P1.2, #10 P1.3, #11 P1.4
Next step: Complete. P1.1-P1.4 passed close-out and pull request #12 squash-merged to `main` at `2b4620d` with maintainer approval.

Goal: confirm the question, the users, the scope rule, and the out-of-scope items that the source draft established.

- [x] P1.1 Confirm the scope rule and the out-of-scope list in `notes/06-out-of-scope.md` (#8)
- [x] P1.2 Review the source inventory and publication signals (#9)
- [x] P1.3 Record any new design decision as an ADR in `notes/adr/` (#10)
- [x] P1.4 Confirm the scoring rubric in `notes/04-prioritization.md` (#11)

Acceptance criteria:

- The scope rule and out-of-scope list are current and linked from `README.md`.
- Every new decision has an accepted or deferred ADR.
- Readiness remains a documented integration judgement, not a claim about the science.

## Phase 2: Contracts and prototype

Parent issue: #13
Branch: `feature/p2-contracts-prototype`
Status: complete
Child issues: #14 P2.1, #15 P2.2, #16 P2.3, #17 P2.4
Next step: Complete. P2.1-P2.4 passed close-out and pull request #18 squash-merged to `main` at `b2d4c25` with maintainer approval. The branch was deleted and issues #13-#17 were closed.

Goal: keep the shared contracts and their evidence in step with the target repositories, without creating parallel work.

- [x] P2.1 Audit the contract-wave records against the live target repositories
- [x] P2.2 Confirm every accepted candidate has a resolution link and a provenance record
- [x] P2.3 Regenerate the register after any registry change
- [x] P2.4 Record the audit result in `CHANGE_LOG.md`

Acceptance criteria:

- Every completed contract candidate points at merged evidence in its target repository.
- Every open candidate states its owner, first step, and unresolved dependency.
- `python scripts/check_registry.py` and `python -m pytest` pass.

## Phase 3: Build

Parent issue: #19
Branch: `feature/p3-build`
Status: complete
Child issues: #20 P3.1, #21 P3.2, #22 P3.3, #23 P3.4
Next step: Complete. P3.1-P3.4 passed close-out and pull request #24 squash-merged to `main` at `9637b46` with maintainer approval. The branch was deleted and issues #19-#23 were closed. The selected handoff remains `GRO-06` to `femic` P117.2 (#376); no candidate was implemented and no target-repository issue, branch, or pull request was created.

Goal: prioritise the model-integration wave and prepare bounded handoffs, one candidate at a time.

- [x] P3.1 Re-score the model-integration candidates against current evidence
- [x] P3.2 Select the first candidate and write its handoff issue body
- [x] P3.3 Confirm the target repository, phase number, and acceptance test
- [x] P3.4 Record the handoff decision in `CHANGE_LOG.md`

Acceptance criteria:

- The first model-integration candidate has a reviewed handoff body and a named target repository.
- The candidate's provenance, validation boundary, and limits are explicit.
- No new general model is proposed as integration work.

## Phase 4: Verify

Parent issue: #25
Branch: `feature/p4-verify`
Status: pr-open
Child issues: #26 P4.1, #27 P4.2, #28 P4.3
Next step: P4.1-P4.3 are complete and the P4 pull request is queued for maintainer review. P4.1 records the local, CI, Docs, Pages, and clean-checkout evidence; P4.2 reconciled all complete, adopted, and queued candidates; P4.3 records the close-out in `notes/reports/p4-verify.md`. No candidate was implemented and no target-repository issue, branch, or pull request was created.

Goal: show that the carried queue and its evidence meet the acceptance criteria, and record the proof.

- [x] P4.1 Run the acceptance checks and record the evidence
- [x] P4.2 Reconcile completed candidates against merged commits
- [x] P4.3 Write the phase close-out report in `notes/reports/`

Acceptance criteria:

- The dashboard and CI pass on the head commit.
- Every completion claim cites a commit, pull request, or issue.
- The close-out report states what remains unverified.

## Phase 5: Release and deploy

Parent issue: TBD
Branch: `feature/p5-release`
Status: planned

Goal: publish the register and docs, then verify them from a clean checkout.

- [ ] P5.1 Write the release notes and the known-gaps list
- [ ] P5.2 Verify the public register and docs from a clean checkout
- [ ] P5.3 Tag and publish (maintainer approval required)

Acceptance criteria:

- The public repository shows the register, the validator, and the workflow files.
- A clean checkout reproduces the dashboard result.
- Release actions are approved and recorded one at a time.

## Phase 6: Operate and maintain

Parent issue: TBD
Branch: `feature/p6-operate`
Status: planned

Goal: keep the queue honest: re-score after each wave, retire stale candidates, and decide whether the mine recurs.

- [ ] P6.1 Set a review cadence and record the first review
- [ ] P6.2 Re-score the registry and retire candidates that did not survive contact
- [ ] P6.3 Decide whether the mine is recurring or one-off

Acceptance criteria:

- Every candidate is `queued`, `adopted`, `deferred`, or `rejected`.
- No candidate is orphaned between this repository and a target roadmap.
- The recurring-or-one-off decision is recorded as an ADR.

## Detailed Next Steps Notes

1. Phase 0 is complete under parent issue #1. P0.1-P0.4 were carried on `feature/p0-bootstrap` and squash-merged in pull request #6 with maintainer approval.
2. Child issues #2-#5 are closed with closeout comments that cite the merge commit and the gate evidence.
3. Phase 1 is `complete` under parent issue #7. Pull request #12 squash-merged to `main` at `2b4620d`; `feature/p1-scope-design` was deleted, and issues #7-#11 were closed with closeout comments.
4. Phase 2 is `complete` under parent issue #13. Pull request #18 squash-merged to `main` at `b2d4c25`; `feature/p2-contracts-prototype` was deleted, and issues #13-#17 were closed with closeout comments. The audit confirmed eleven contract-wave candidates with merged evidence and `GRO-06` as the one open candidate.
5. Phase 3 is `complete` under parent issue #19. Pull request #24 squash-merged to `main` at `9637b46`; `feature/p3-build` was deleted, and issues #19-#23 were closed with closeout comments. The re-score is in `notes/20-p3-model-integration-rescore.md` and the handoff is `handoffs/femic-child-biomass-curves-p3.md`. The selected candidate is `GRO-06`, target `femic` P117.2 (#376). No target-repository issue, branch, or pull request was created; the handoff remains queued for a separate approval.
6. Phase 4 is `pr-open` under parent issue #25. P4.1-P4.3 are complete on `feature/p4-verify`; the acceptance evidence is in `notes/21-p4-acceptance-evidence.md`, the candidate reconciliation is in `notes/22-p4-candidate-reconciliation.md`, and the close-out is in `notes/reports/p4-verify.md`. The P4 pull request waits for maintainer review. P5 remains planned and needs a separate approval.
7. Keep the carried programme history in `CHANGE_LOG.md` and `notes/`; do not reopen target-repo phases from this repository.
8. Do not start a model-integration handoff until the target repository's roadmap and phase number are confirmed.
