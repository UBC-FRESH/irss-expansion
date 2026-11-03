# P4 candidate reconciliation

Date: 2026-11-03
Phase: P4 Verify
Parent issue: #25
Task: P4.2
Scope: every candidate in `registry/candidates.yaml` whose status is `complete`,
`adopted`, or `queued`

## Purpose and method

This note reconciles each completion, adoption, or queue claim against the live
target repositories. It is a read-only audit of the targets: no target issue,
branch, pull request, setting, tag, or release was created or changed. The
registry remains the source of truth and `docs/candidates.md` remains generated.

Evidence was read on 2026-11-03 with:

```bash
gh issue view <number> --repo UBC-FRESH/<repo> --json state,title,url,updatedAt
gh pr view <number> --repo UBC-FRESH/<repo> --json state,mergedAt,mergeCommit,url
gh api repos/UBC-FRESH/<repo>/pulls/<number>
git ls-remote https://github.com/UBC-FRESH/<repo>.git refs/heads/main
```

Live `main` heads:

| Repository | Head |
| --- | --- |
| `UBC-FRESH/femic` | `faf00af` |
| `UBC-FRESH/ws4` | `a86f884` |
| `UBC-FRESH/fhops` | `296e2cf` |
| `UBC-FRESH/ws3` | `b84a0ae` |
| `UBC-FRESH/nemora` | `060c688` |
| `UBC-FRESH/fresh-road` | `df8ad2d` |

These are the same heads recorded by the P3 re-score, so the P3 readiness values
remain the current screening values. P4 did not re-mine sources, change a score,
or retire a candidate.

## 1. Completed candidates

Seventeen candidates claim `complete`. Each has a closed target issue and at
least one merged pull request, except where the row names a live target record
that is the completion evidence.

| ID | Live target evidence on 2026-11-03 | Result |
| --- | --- | --- |
| `INV-01` | `femic` [#536](https://github.com/UBC-FRESH/femic/issues/536), [#539](https://github.com/UBC-FRESH/femic/issues/539), [#542](https://github.com/UBC-FRESH/femic/issues/542) closed; PRs [#538](https://github.com/UBC-FRESH/femic/pull/538) `98fe2c6`, [#541](https://github.com/UBC-FRESH/femic/pull/541) `736c24d`, [#544](https://github.com/UBC-FRESH/femic/pull/544) `c34181b` merged | merged |
| `INV-05` | `ws4` PRs [#490](https://github.com/UBC-FRESH/ws4/pull/490) `d6cda2b` and [#492](https://github.com/UBC-FRESH/ws4/pull/492) `a58b791` merged | merged |
| `INV-06` | `nemora` [#10](https://github.com/UBC-FRESH/nemora/issues/10) closed; PR [#14](https://github.com/UBC-FRESH/nemora/pull/14) `2e8776c` merged; parent [#7](https://github.com/UBC-FRESH/nemora/issues/7) closed | merged |
| `GRO-01` | `femic` [#370](https://github.com/UBC-FRESH/femic/issues/370) closed; PR [#378](https://github.com/UBC-FRESH/femic/pull/378) `9e16be9` merged | merged |
| `DIS-01` | `femic` [#371](https://github.com/UBC-FRESH/femic/issues/371) closed; PRs [#379](https://github.com/UBC-FRESH/femic/pull/379) `ef4cff2` and `ws4` [#398](https://github.com/UBC-FRESH/ws4/pull/398) `5ea4a05` merged | merged |
| `DIS-04` | `ws4` PRs [#499](https://github.com/UBC-FRESH/ws4/pull/499) `9e32210`, [#502](https://github.com/UBC-FRESH/ws4/pull/502) `7558235`, [#503](https://github.com/UBC-FRESH/ws4/pull/503) `e2f980f`, [#509](https://github.com/UBC-FRESH/ws4/pull/509) `476c720` merged | merged |
| `PLAN-03` | `ws4` [#378](https://github.com/UBC-FRESH/ws4/issues/378) closed; PR [#475](https://github.com/UBC-FRESH/ws4/pull/475) `865bef6` merged; parent [#375](https://github.com/UBC-FRESH/ws4/issues/375) closed | merged |
| `PLAN-07` | `ws4` [#696](https://github.com/UBC-FRESH/ws4/issues/696) closed; PR [#698](https://github.com/UBC-FRESH/ws4/pull/698) `91b985c` merged | merged |
| `PLAN-08` | `ws4` [#749](https://github.com/UBC-FRESH/ws4/issues/749) closed; PR [#760](https://github.com/UBC-FRESH/ws4/pull/760) `0dbc01a` merged | merged |
| `BIO-01` | `ws4` [#376](https://github.com/UBC-FRESH/ws4/issues/376) closed; PR [#463](https://github.com/UBC-FRESH/ws4/pull/463) `b0438de` merged; parent [#375](https://github.com/UBC-FRESH/ws4/issues/375) closed | merged |
| `BIO-02` | `ws4` [#377](https://github.com/UBC-FRESH/ws4/issues/377) closed; PRs [#471](https://github.com/UBC-FRESH/ws4/pull/471) `b4f7caa` and [#484](https://github.com/UBC-FRESH/ws4/pull/484) `84fb562` merged; parent [#375](https://github.com/UBC-FRESH/ws4/issues/375) closed | merged |
| `DATA-01` | `nemora` [#6](https://github.com/UBC-FRESH/nemora/issues/6) closed; PR [#11](https://github.com/UBC-FRESH/nemora/pull/11) `cbf504d` merged; parent [#7](https://github.com/UBC-FRESH/nemora/issues/7) closed | merged |
| `DATA-02` | `nemora` [#8](https://github.com/UBC-FRESH/nemora/issues/8) closed; PR [#13](https://github.com/UBC-FRESH/nemora/pull/13) `d094c01` merged; parent [#7](https://github.com/UBC-FRESH/nemora/issues/7) closed | merged |
| `DATA-04` | `nemora` [#9](https://github.com/UBC-FRESH/nemora/issues/9) closed; PR [#12](https://github.com/UBC-FRESH/nemora/pull/12) `9e7ea9e` merged; parent [#7](https://github.com/UBC-FRESH/nemora/issues/7) closed | merged |
| `DEC-02` | `ws4` P90-P93 issues [#650](https://github.com/UBC-FRESH/ws4/issues/650), [#655](https://github.com/UBC-FRESH/ws4/issues/655), [#659](https://github.com/UBC-FRESH/ws4/issues/659), [#662](https://github.com/UBC-FRESH/ws4/issues/662) closed; PRs [#653](https://github.com/UBC-FRESH/ws4/pull/653) `6aecccb`, [#657](https://github.com/UBC-FRESH/ws4/pull/657) `a0f395a`, [#661](https://github.com/UBC-FRESH/ws4/pull/661) `4ce820c`, [#669](https://github.com/UBC-FRESH/ws4/pull/669) `5cf5444` merged | merged |
| `DEC-03` | `ws4` [#734](https://github.com/UBC-FRESH/ws4/issues/734) and [#670](https://github.com/UBC-FRESH/ws4/issues/670) closed; PRs [#741](https://github.com/UBC-FRESH/ws4/pull/741) `00c0b6c` and [#690](https://github.com/UBC-FRESH/ws4/pull/690) `d14f4ff` merged | merged |
| `DEC-04` | `femic` [#372](https://github.com/UBC-FRESH/femic/issues/372) closed; PRs [#380](https://github.com/UBC-FRESH/femic/pull/380) `f833ed9` and [#418](https://github.com/UBC-FRESH/femic/pull/418) `69af694` merged; parent [#369](https://github.com/UBC-FRESH/femic/issues/369) closed | merged |

No completion claim lacks a live target record.

## 2. Adopted candidates

| ID | Live target evidence on 2026-11-03 | Result |
| --- | --- | --- |
| `CARB-01` | `femic` [#361](https://github.com/UBC-FRESH/femic/issues/361) closed; PR [#394](https://github.com/UBC-FRESH/femic/pull/394) `30b1444` merged. `ws4` [#357](https://github.com/UBC-FRESH/ws4/issues/357) closed; PR [#408](https://github.com/UBC-FRESH/ws4/pull/408) `ddf4ed8` merged | adopted and merged |
| `CARB-03` | `fhops` P44 [#380](https://github.com/UBC-FRESH/fhops/issues/380) and P44.1 [#381](https://github.com/UBC-FRESH/fhops/issues/381) open; PR [#383](https://github.com/UBC-FRESH/fhops/pull/383) open, not merged | adopted and in flight; not merged |

`CARB-03` was checked rather than assumed. On 2026-11-03 the live pull request
[#383](https://github.com/UBC-FRESH/fhops/pull/383) has one commit
`554d177`, 17 changed files, 1,649 additions, no deletions, CI green, and
`mergeable_state: clean`. It has no merge commit and the parent and child issues
are open. `adopted` means "taken up by live work", not "merged"; the carried
status and resolution remain accurate. If the pull request closes without
merging, or remains idle beyond the next review, the status should be revisited.

## 3. Queued candidate

`GRO-06` remains `queued`, not implemented:

| Field | Live state on 2026-11-03 |
| --- | --- |
| Parent issue | `femic` P117 [#374](https://github.com/UBC-FRESH/femic/issues/374), open |
| Child issue | `femic` P117.2 [#376](https://github.com/UBC-FRESH/femic/issues/376), open, no assignee |
| Branch | `feature/p117-efi-attributes` exists at `67cba53` |
| Acceptance test | `tests/test_biomass_curves.py` is absent on the branch, as expected before implementation |
| Handoff | [`handoffs/femic-child-biomass-curves-p3.md`](../handoffs/femic-child-biomass-curves-p3.md), unchanged |

No target issue was edited and no implementation was started. The candidate
stays queued behind the separate target-repository approval gate.

## 4. Roadmap and record drift

| Item | Evidence | Treatment |
| --- | --- | --- |
| `CARB-03` is adopted but not merged | FHOPS #380, #381, and PR #383 are open; PR CI is green and mergeable | Kept `adopted` as "taken up"; recorded the open state and the revisit trigger |
| FHOPS P44 has no roadmap section | Issue #380 says `Roadmap entry: ROADMAP.md Phase 44`, but the live `fhops` `ROADMAP.md` has no Phase 44 section | Target drift recorded; not changed from this repository |
| `ws4` PR #408 title says P57, while the issue and roadmap say P58 | Live issue #357 and the ws4 roadmap use P58; the pull request title uses P57 | The P2 correction to P58 still holds; recorded again, not changed |
| `femic` P117 is active while P117.2 is open | Live P117 roadmap status and issue #374 | This is the expected queued state, not a contradiction |
| `DEC-02` resolution lacked PR and commit citations | Live issues #650/#655/#659/#662 and PRs #653/#657/#661/#669 | Added a `provenance` field with the live records; no status or score changed |
| The P3 note recorded stale `ws4` roadmap statuses | The live `ws4` P54 and P58 entries now say `complete` | No lag was found for the checked phases; the P3 drift is not repeated here |

## 5. Candidate and status decisions

- **Score changes: none.** The live target heads match the P3 snapshot and no
  candidate-specific evidence changed. The P3 readiness values remain current.
- **Status changes: none.** All seventeen `complete` rows have merged evidence;
  `CARB-01` is adopted and merged; `CARB-03` is adopted and in flight;
  `GRO-06` remains queued and unimplemented.
- **Retirements: none.** No candidate failed contact with live evidence in this
  pass. `INV-04` remains rejected and `DIS-03` remains deferred on their earlier
  evidence; P4 does not re-mine those decisions.
- **Registry metadata:** `meta.audit_note` now names this note, and `DEC-02`
  carries the PR and merge-commit provenance above. `docs/candidates.md` was
  regenerated from the registry.

## 6. Limits

- The audit checked issue and pull-request state, merge commits, pull-request
  mergeability, and repository heads. It did not re-run target test suites or
  re-read every merged diff.
- "Complete" and "adopted" mean the cited record exists and is live. They are not
  an independent re-validation of target science.
- The live state is a 2026-11-03 snapshot. Re-check the targets before any later
  handoff or status change.
