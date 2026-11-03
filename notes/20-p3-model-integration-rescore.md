# P3 model-integration re-score and handoff decision

Date: 2026-11-03
Phase: P3 Build
Parent issue: #19
Tasks: P3.1-P3.3
Scope: the 25 wave-2 candidates in `registry/candidates.yaml`, plus `GRO-06`
because it is the one contract-wave candidate that is neither complete nor
adopted.

## Purpose and method

This note re-scores the model-integration queue against the live target
repositories. It is a read-only audit of the targets: no target issue, branch,
pull request, or setting was changed. The registry stays the source of truth and
`docs/candidates.md` stays generated from it.

Evidence was read on 2026-11-03 from:

```bash
gh issue view <number> --repo UBC-FRESH/<repo> --json state,title
gh pr view <number> --repo UBC-FRESH/<repo> --json state,mergedAt,mergeCommit
git -C <repo> rev-parse --short origin/main
```

Heads checked:

| Repository | Live `main` head |
| --- | --- |
| `UBC-FRESH/femic` | `faf00af` (P131) |
| `UBC-FRESH/ws4` | `a86f884` (P126) |
| `UBC-FRESH/fhops` | `296e2cf6` (P46) |
| `UBC-FRESH/ws3` | `b84a0ae` |
| `UBC-FRESH/nemora` | `060c688` |
| `UBC-FRESH/fresh-road` | `df8ad2d` |
| `UBC-FRESH/fresh-beast` | `5eb5097` |

The score formula is unchanged:
`priority = (impact * readiness) / (effort_points * risk)`, with S = 1, M = 2,
L = 3, XL = 5. A wave remains a dependency and sequencing judgement, not a score
threshold. Readiness remains an integration judgement, not an author-confirmed
science claim.

## Re-score table

Carried score is the value before this audit. The live state column cites the
target record that was checked. "No live issue" means the target repository was
searched and no candidate-specific issue or pull request exists; the repository
head is the live state.

| ID | Carried status / score | Live target state | Result |
| --- | --- | --- | --- |
| `INV-01` | complete / 3.33 | `femic` P120-P122 closed ([#536](https://github.com/UBC-FRESH/femic/issues/536), [#539](https://github.com/UBC-FRESH/femic/issues/539), [#542](https://github.com/UBC-FRESH/femic/issues/542)); PRs [#538](https://github.com/UBC-FRESH/femic/pull/538), [#541](https://github.com/UBC-FRESH/femic/pull/541), [#544](https://github.com/UBC-FRESH/femic/pull/544) merged | unchanged; complete |
| `INV-05` | complete / 4.00 | `ws4` [#490](https://github.com/UBC-FRESH/ws4/pull/490) and [#492](https://github.com/UBC-FRESH/ws4/pull/492) merged | unchanged; complete |
| `INV-09` | shortlisted / 3.00 | `fresh-road` package `0.1.0a1` at `df8ad2d`; two ALS pilots and route fixtures; no WS4 handoff issue | readiness 3 -> 4; score 4.00 |
| `GRO-02` | shortlisted / 1.67 | `femic` P116 [#369](https://github.com/UBC-FRESH/femic/issues/369) closed; `ws4` P56 [#393](https://github.com/UBC-FRESH/ws4/issues/393) consumed the disturbance contract; no climate-modifier issue | readiness 3 -> 4; score 2.22 |
| `GRO-03` | shortlisted / 1.67 | `femic` P116 climate and disturbance contracts closed ([#369](https://github.com/UBC-FRESH/femic/issues/369), [#371](https://github.com/UBC-FRESH/femic/issues/371)); no mortality issue | readiness 3 -> 4; score 2.22 |
| `GRO-05` | candidate / 1.50 | `femic` main `faf00af`; no age-independent trajectory issue; dependency `INV-03` remains wave 3 | unchanged; not ready |
| `DIS-02` | deferred / 4.00 | `fresh-beast` `0.1.0a1` at `5eb5097`; 2019 AOS case-control failed (sensitivity 25.8%, precision 33.3%); operational use deferred | unchanged; deferred |
| `DIS-04` | complete / 3.75 | `ws4` PRs [#499](https://github.com/UBC-FRESH/ws4/pull/499), [#502](https://github.com/UBC-FRESH/ws4/pull/502), [#503](https://github.com/UBC-FRESH/ws4/pull/503), [#509](https://github.com/UBC-FRESH/ws4/pull/509) merged | unchanged; complete |
| `DIS-06` | shortlisted / 0.83 | `ws4` P15 [#138](https://github.com/UBC-FRESH/ws4/issues/138) and `fhops` P16 [#236](https://github.com/UBC-FRESH/fhops/issues/236) closed; no composable hazard library | unchanged; not ready |
| `DIS-09` | shortlisted / 3.00 | `fhops` P44 [#380](https://github.com/UBC-FRESH/fhops/issues/380) open; PR [#383](https://github.com/UBC-FRESH/fhops/pull/383) open with CI green | unchanged; overlaps in-flight P44 |
| `PLAN-01` | shortlisted / 1.67 | `ws4` P15 [#138](https://github.com/UBC-FRESH/ws4/issues/138) and P24 [#207](https://github.com/UBC-FRESH/ws4/issues/207) closed; no risk objective issue; dependencies `DIS-06` and `DATA-06` remain open | unchanged; not ready |
| `PLAN-02` | shortlisted / 3.00 | `ws4` P24 portfolio search [#207](https://github.com/UBC-FRESH/ws4/issues/207) closed; no resilience-portfolio issue | unchanged; depends on `PLAN-01` |
| `PLAN-05` | shortlisted / 3.00 | `ws4` P15 spread account [#138](https://github.com/UBC-FRESH/ws4/issues/138) closed; `fresh-road` TSA 23 graph still has 779 components and 2,793 unrouted blocks | readiness 3 -> 2; score 2.00 |
| `PLAN-07` | complete / 6.00 | `ws4` P101 [#696](https://github.com/UBC-FRESH/ws4/issues/696); PR [#698](https://github.com/UBC-FRESH/ws4/pull/698) merged as `91b985c` | unchanged; complete |
| `PLAN-08` | complete / 6.00 | `ws4` P114 [#749](https://github.com/UBC-FRESH/ws4/issues/749); PR [#760](https://github.com/UBC-FRESH/ws4/pull/760) merged as `0dbc01a` | unchanged; complete |
| `CARB-02` | candidate / 2.00 | `ws3` `main` `b84a0ae` holds the avoided-emissions examples; no reusable emissions account; dependency `DIS-06` open | unchanged; not ready |
| `CARB-03` | adopted / 6.00 | `fhops` P44 [#380](https://github.com/UBC-FRESH/fhops/issues/380) open; PR [#383](https://github.com/UBC-FRESH/fhops/pull/383) open, CI green, not merged | unchanged; adoption is in-flight |
| `OPS-01` | shortlisted / 4.00 | `femic` P109 [#304](https://github.com/UBC-FRESH/femic/issues/304) closed; `fhops` has thinning productivity models but no priority issue; dependencies `INV-02` and `INV-07` remain wave 3 | unchanged score; not selectable because dependencies are unmet |
| `OPS-03` | shortlisted / 3.00 | `fhops` P44 [#380](https://github.com/UBC-FRESH/fhops/issues/380) is a read-only report; no salvage-scheduling issue; dependencies `DIS-09`, `CARB-03`, `OPS-05` open | unchanged; not ready |
| `OPS-05` | shortlisted / 3.00 | `fresh-road` at `df8ad2d`; `fhops` P16 hazard windows [#236](https://github.com/UBC-FRESH/fhops/issues/236) closed; no road-status constraint issue; dependency `INV-09` not complete | readiness 3 -> 2; score 2.00 |
| `DATA-03` | candidate / 2.00 | `nemora` `main` `060c688`; synthesis and sampling exist, no measurement-campaign issue; dependencies `DATA-02` and `INV-06` complete | unchanged; no target phase |
| `DATA-05` | shortlisted / 3.00 | `nemora` P5 [#7](https://github.com/UBC-FRESH/nemora/issues/7) closed; `DATA-01` and `INV-01` complete; no imputation issue | readiness 3 -> 4; score 4.00 |
| `DEC-01` | shortlisted / 4.00 | `ws4` web phases P59 [#417](https://github.com/UBC-FRESH/ws4/issues/417), P61 [#430](https://github.com/UBC-FRESH/ws4/issues/430), P65 [#464](https://github.com/UBC-FRESH/ws4/issues/464) closed; `fhops` P12 complete; no shared layer contract | unchanged; no target phase |
| `DEC-02` | complete / 12.00 | `ws4` P90-P93 closed ([#650](https://github.com/UBC-FRESH/ws4/issues/650), [#655](https://github.com/UBC-FRESH/ws4/issues/655), [#659](https://github.com/UBC-FRESH/ws4/issues/659), [#662](https://github.com/UBC-FRESH/ws4/issues/662)) | unchanged; complete |
| `DEC-03` | complete / 8.00 | `ws4` P108/P109; PR [#741](https://github.com/UBC-FRESH/ws4/pull/741) merged as `00c0b6c` | unchanged; complete |
| `GRO-06` | queued / 5.00 | `femic` P117 [#374](https://github.com/UBC-FRESH/femic/issues/374) active and P117.2 [#376](https://github.com/UBC-FRESH/femic/issues/376) open; branch `feature/p117-efi-attributes` at `67cba53`; no biomass implementation | unchanged score; selected |

Summary: 26 rows, 25 wave-2 plus `GRO-06`. Six scores changed; the other twenty
are unchanged. Five completed or adopted rows keep their status. No completed or
adopted contract-wave record was rewritten.

## Score changes

| ID | Field | Before | After | Evidence |
| --- | --- | ---: | ---: | --- |
| `INV-09` | readiness | 3 | 4 | `fresh-road` now has both a published status contract and two ALS pilots; the remaining gap is the WS4 consumer, not the data path |
| `GRO-02` | readiness | 3 | 4 | The climate contract (`femic` P116) and curve-uncertainty lane (`nemora` P5) are merged, so the adapter path is clearer |
| `GRO-03` | readiness | 3 | 4 | The climate and disturbance contracts are merged; a mortality transition can consume them directly |
| `PLAN-05` | readiness | 3 | 2 | The `fresh-road` TSA 23 graph still has 779 components and 2,793 unrouted blocks; a connectivity account would inherit those gaps |
| `OPS-05` | readiness | 3 | 2 | It depends on `INV-09`, whose WS4 join is not complete and is pilot-scale |
| `DATA-05` | readiness | 3 | 4 | `DATA-01` and `INV-01` are complete, so a kNN pilot has both an uncertainty lane and a published inventory product to test against |

No impact, effort, or risk value changed. No wave changed. A wave change would
be a sequencing decision, not a re-score, and none is proposed here.

## Drift recorded

1. **`CARB-03` is adopted but not merged.** FHOPS P44 and PR #383 are open with
   CI green. The registry says "adopted", which means taken up by live work, not
   merged. The resolution now says so explicitly.
2. **`OPS-01` has wave-3 dependencies.** Its dependencies `INV-02` and `INV-07`
   are still wave-3 candidates, even though its carried wave is 2. It is not
   selectable until those dependencies exist. The wave field was not changed.
3. **`DIS-09`, `OPS-03`, and `OPS-05` are entangled with open work.** `DIS-09`
   overlaps FHOPS P44; `OPS-03` depends on `DIS-09`, `CARB-03`, and `OPS-05`;
   `OPS-05` depends on `INV-09`. Selecting any of them now would create parallel
   work.
4. **The WS4 roadmap statuses lag merged evidence.** Several phases whose issues
   are closed still say `pr-open` in the live roadmap. The completed rows in this
   table follow the closed issue and merged pull request, not the stale status
   line. This is a target-repository drift to report, not a change to make here.
5. **`GRO-06` is the one open contract-wave candidate.** It is included because
   P3.1 excludes only the completed or adopted contract-wave rows. It is a
   model-integration candidate (biomass curve family and carbon conversion), not
   a new contract.

## Selection decision (P3.2)

Selected candidate: **`GRO-06` Biomass yield curves from time-series remote
sensing**.

Target repository and phase: **`UBC-FRESH/femic`, P117 EFI Inventory Attributes
and Biomass Curves ([#374](https://github.com/UBC-FRESH/femic/issues/374)),
child P117.2 ([#376](https://github.com/UBC-FRESH/femic/issues/376))** on branch
`feature/p117-efi-attributes`.

Why this candidate:

- It has the highest carried score (5.00) among candidates that are not
  complete, adopted, deferred, or blocked by an in-flight target phase.
- It is the only eligible candidate whose target phase, child issue, branch, and
  acceptance test already exist. The P2 close-out recommended this shape to
  avoid opening a new target phase.
- The consumer is named and live: the FEMIC curve/export stage and the existing
  volume-curve path, with the carbon package (`femic` P115) explicitly kept out
  of scope.
- The handoff is bounded to one published biomass curve family for one pilot
  species/BEC, an independent selection path, and a declared carbon conversion.
  It does not refit a model or add belowground biomass.
- No implementation exists on the branch, so the handoff does not duplicate
  merged work.

Rejected alternatives:

| Candidate | Reason not selected |
| --- | --- |
| `INV-09` | No WS4 handoff phase exists; the full TSA 23 route graph is still incomplete, so the consumer would be pilot-scale only |
| `GRO-02` | Highest-impact dynamics candidate, but no target phase exists and the response-function choice needs a separate pilot; L effort |
| `GRO-03` | No target phase and no agreed held-out PSP validation design |
| `DATA-05` | No Nemora phase exists; donor and spatial-holdout design need agreement |
| `DEC-01` | No shared layer contract or target phase; FHOPS P12 is complete |
| `OPS-01` | Its dependencies `INV-02` and `INV-07` are wave-3 candidates |
| `DIS-09`, `OPS-03`, `OPS-05` | They overlap or depend on open FHOPS P44 and `INV-09` work |
| `CARB-02`, `DIS-06`, `PLAN-01`, `PLAN-02` | Dependencies `DIS-06`/`DATA-06`/`PLAN-01` are not delivered |
| `PLAN-05` | Blocked by the `fresh-road` graph gaps; the carried readiness dropped |
| `CARB-03` | Already adopted and in flight in FHOPS P44; not a new handoff |

## Target confirmation (P3.3)

| Field | Confirmed value |
| --- | --- |
| Repository | [`UBC-FRESH/femic`](https://github.com/UBC-FRESH/femic) |
| Phase | P117 EFI Inventory Attributes and Biomass Curves, [#374](https://github.com/UBC-FRESH/femic/issues/374), status `active` |
| Task | P117.2 Add a biomass curve family and carbon conversion, [#376](https://github.com/UBC-FRESH/femic/issues/376), status open |
| Branch | `feature/p117-efi-attributes` at `67cba53` |
| Roadmap | `femic/ROADMAP.md`, section "Phase 117: EFI Inventory Attributes and Biomass Curves" |
| Duplicate check | No biomass curve family exists on `main` or the P117 branch; the INV-01 high-biomass files are inventory-calibration evidence, not a biomass curve family |
| Acceptance test | New `tests/test_biomass_curves.py` plus a config/CLI fixture run; see the handoff body |

The phase number is not drifted. P117.1 is active on the shared branch; P117.2 is
planned and has no implementation. The live issue has no individual assignee, so
the owner remains the phase-level owner, not an invented person.

### Confirmation record (P3.3)

Checked again on 2026-11-03 before writing the handoff:

- `femic` `origin/main` head `faf00af`; P117 is `active` in `ROADMAP.md` and
  P117.2 is still an open child issue.
- Branch `feature/p117-efi-attributes` exists at `67cba53`.
- An all-state search for `biomass` in `femic` issues and pull requests returns
  the P117 parent, P117.2, P115.2, and the INV-01 high-biomass calibration
  history. None is a biomass curve family. No duplicate implementation exists.
- The acceptance command is executable in the target repository:
  `python -m pytest tests/test_biomass_curves.py -q`. That file does not exist
  yet and is a deliverable, so the test is expected to fail until the work is
  implemented.
- No phase-number drift. The only drift is the P117.1 active state on the shared
  branch, which does not block P117.2 because the two lanes add different files.

## Handoff artifact

[`handoffs/femic-child-biomass-curves-p3.md`](../handoffs/femic-child-biomass-curves-p3.md)
is the reviewed issue body. It is written for the existing P117.2 issue, not a
new issue. No target issue, branch, or pull request was created or edited.

## Limits

- The audit checked issue and pull-request state and repository heads. It did not
  re-run the target repositories' test suites or re-read every merged diff.
- "Complete" and "adopted" mean the cited record exists; they are not an
  independent re-validation of the target science.
- Readiness values remain integration judgements. The score is a screening aid,
  not an approval.
- The live state is a 2026-11-03 snapshot. Re-check the target roadmap before any
  later handoff.
