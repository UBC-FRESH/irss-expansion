# P2 contract-wave audit

Audit date: 2026-11-03
Phase: P2 Contracts and prototype
Parent issue: #13
Task: P2.1
Scope: the twelve contract-wave candidates in `registry/candidates.yaml`

## Purpose and method

This note checks the carried contract-wave records against the live target
repositories. It is a read-only audit: no target issue, branch, pull request, or
setting was changed. The registry remains the source of truth, and
`docs/candidates.md` remains generated from it.

The audited set is the twelve candidates named in the carried programme history:
`GRO-01`, `DIS-01`, `DEC-04`, `DATA-01`, `CARB-01`, `BIO-01`, `BIO-02`,
`PLAN-03`, `DATA-02`, `DATA-04`, `INV-06`, and `GRO-06`.

Evidence was read with GitHub CLI and the live target roadmaps:

```bash
gh issue view <number> --repo UBC-FRESH/<repo> --json state,title,assignees
gh pr view <number> --repo UBC-FRESH/<repo> --json state,mergedAt,mergeCommit
gh pr checks <number> --repo UBC-FRESH/<repo>
```

The live `main` branches of `femic`, `ws4`, and `ws3` were also checked locally
for phase-number drift. The audit did not re-mine IRSS or Silva21 sources, change
a score, retire a candidate, or reopen an accepted decision.

## Audit table

| Candidate | Register status | Live target record | Live state on 2026-11-03 | Audit result |
| --- | --- | --- | --- | --- |
| `GRO-01` | complete | [`femic#370`](https://github.com/UBC-FRESH/femic/issues/370); [PR #378](https://github.com/UBC-FRESH/femic/pull/378) | Issue closed; PR merged as `9e16be9` | merged |
| `DIS-01` | complete | [`femic#371`](https://github.com/UBC-FRESH/femic/issues/371); [PR #379](https://github.com/UBC-FRESH/femic/pull/379); [`ws4#398`](https://github.com/UBC-FRESH/ws4/pull/398) | Issue closed; PRs merged as `ef4cff2` and `5ea4a05` | merged |
| `DEC-04` | complete | [`femic#372`](https://github.com/UBC-FRESH/femic/issues/372); [PR #380](https://github.com/UBC-FRESH/femic/pull/380); [PR #418](https://github.com/UBC-FRESH/femic/pull/418) | Issue closed; PRs merged as `f833ed9` and `69af694` | merged; the carried note that `#372` remained open is stale |
| `DATA-01` | complete | [`nemora#6`](https://github.com/UBC-FRESH/nemora/issues/6); [PR #11](https://github.com/UBC-FRESH/nemora/pull/11) | Issue closed; PR merged as `cbf504d` | merged |
| `CARB-01` | adopted | [`femic#361`](https://github.com/UBC-FRESH/femic/issues/361); [PR #394](https://github.com/UBC-FRESH/femic/pull/394); [`ws4#357`](https://github.com/UBC-FRESH/ws4/issues/357); [PR #408](https://github.com/UBC-FRESH/ws4/pull/408) | Both issues closed; PRs merged as `30b1444` and `ddf4ed8` | adopted and merged; ws4 phase label drift recorded below |
| `BIO-01` | complete | [`ws4#376`](https://github.com/UBC-FRESH/ws4/issues/376); [PR #463](https://github.com/UBC-FRESH/ws4/pull/463) | Issue closed; PR merged as `b0438de` | merged |
| `BIO-02` | complete | [`ws4#377`](https://github.com/UBC-FRESH/ws4/issues/377); [PR #471](https://github.com/UBC-FRESH/ws4/pull/471); [PR #484](https://github.com/UBC-FRESH/ws4/pull/484) | Issue closed; PRs merged as `b4f7caa` and `84fb562` | merged, with a real-data follow-up |
| `PLAN-03` | complete | [`ws4#378`](https://github.com/UBC-FRESH/ws4/issues/378); [PR #475](https://github.com/UBC-FRESH/ws4/pull/475) | Issue closed; PR merged as `865bef6` | merged |
| `DATA-02` | complete | [`nemora#8`](https://github.com/UBC-FRESH/nemora/issues/8); [PR #13](https://github.com/UBC-FRESH/nemora/pull/13) | Issue closed; PR merged as `d094c01` | merged |
| `DATA-04` | complete | [`nemora#9`](https://github.com/UBC-FRESH/nemora/issues/9); [PR #12](https://github.com/UBC-FRESH/nemora/pull/12) | Issue closed; PR merged as `9e7ea9e` | merged |
| `INV-06` | complete | [`nemora#10`](https://github.com/UBC-FRESH/nemora/issues/10); [PR #14](https://github.com/UBC-FRESH/nemora/pull/14) | Issue closed; PR merged as `2e8776c` | merged |
| `GRO-06` | queued | [`femic#376`](https://github.com/UBC-FRESH/femic/issues/376); parent [`femic#374`](https://github.com/UBC-FRESH/femic/issues/374) | Both issues open | open; no implementation exists |

Summary: eleven candidates are complete or adopted with merged target evidence,
and one candidate remains open. No contract-wave candidate has a missing target
record.

## Drift recorded

1. **`CARB-01` ws4 phase label.** The carried record calls the ws4 carbon phase
   `P51`. The live issue is titled `P58` and the ws4 roadmap has `P51` as the
   separate release-candidate verification phase. The carbon phase's own PR
   #408 title says `P57`, but the issue body and roadmap use `P58`. The audit
   cites the live issue and roadmap, keeps the adoption decision, and corrects
   the register to `P58`.
2. **`DEC-04` close state.** The carried resolution said `femic#372` remained
   open for real model cards and pipeline wiring. Follow-up PR #418 merged the
   published cards and annotation seam and closed the issue. The register now
   cites both merges.
3. **`BIO-02` follow-up.** The carried resolution cited PR #471 only. PR #484
   added the real TFL 6 first-return run and reported the missing exact metrics;
   it is part of the completion evidence, not a new candidate.
4. **`BIO-01` handoff status.** `handoffs/README.md` still described P54.1 as
   active in PR #463. P54.1 and its parent are closed; the live merge is cited
   here and in the registry.
5. **Provenance gaps.** `DATA-02`, `DATA-04`, and `INV-06` had resolution text
   that was truncated before their issue and merge commit. The audit restores
   the issue, PR, and commit citations without changing their status or score.
6. **README handoff state.** `README.md` described `femic#371` and `femic#372`
   as open. Both are closed and merged; the README text is updated to the live
   state.

## Open candidate record

`GRO-06` is the only open contract-wave candidate. It is queued, not active, and
no target branch or implementation exists.

| Field | Recorded value |
| --- | --- |
| Owner | `UBC-FRESH/femic` P117 ([#374](https://github.com/UBC-FRESH/femic/issues/374)); no individual GitHub assignee is recorded on the live issue |
| First step | Add a biomass curve table and a carbon conversion report to one FEMIC instance |
| Registry dependencies | None (`dependencies: []`); no candidate blocks it |
| Unresolved dependency | Parent `femic#374` and child `femic#376` remain open. The candidate still needs a biomass curve source and a declared carbon-fraction boundary before integration |

The live issue has no assignee. The owner is therefore recorded at the phase
level, not invented as a person.

## Metadata applied

The eleven complete or adopted contract-wave rows now carry a `provenance`
field that names the live issue, pull request, and merge commit. `GRO-06` carries
`owner`, `first_step`, `dependencies`, and `unresolved_dependency`; its
dependency list stays empty because no candidate blocks it. The owner is recorded
at the phase level because the live issue has no individual assignee.

`scripts/render_registry.py` displays provenance, owner, and unresolved
dependency when present. `scripts/check_registry.py` rejects an empty value in
any of those optional fields. No status, score, wave, source, or risk changed.

The remaining open candidates outside the twelve-row contract wave were not
re-scored or given an invented owner. Their metadata is outside this audit's
scope.

## Limits

- The audit checked issue and pull-request state, merge commits, and cited
  roadmaps. It did not re-run the target repositories' test suites or re-read
  every changed file in each merge.
- "Merged evidence" means the cited pull request is merged and its issue is
  closed. It is not an independent re-validation of the target-repository
  science.
- The registry's readiness values remain integration judgements, not
  author-confirmed estimates.
- The live state is a snapshot from 2026-11-03. Re-check before any later
  handoff.
