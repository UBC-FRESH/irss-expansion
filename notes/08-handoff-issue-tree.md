# Handoff issue tree

All wave-1 issues were created on 2026-10-25 with the maintainer's approval.
This note records the final tree and the reasoning.

- Issue bodies and links: [`../handoffs/README.md`](../handoffs/README.md)
- Live-repo overlap check: [`10-repo-state-check.md`](10-repo-state-check.md)

## Final issue tree

### `femic`: shared environmental contracts — P116

Parent: [#369](https://github.com/UBC-FRESH/femic/issues/369)

| Child | Candidate | Issue | Acceptance |
| --- | --- | --- | --- |
| `climate.v1` schema and adapter | `GRO-01` | [#370](https://github.com/UBC-FRESH/femic/issues/370) | Rejects bad units/scenarios; two AOIs load |
| `disturbance.v1` schema and validator | `DIS-01` | [#371](https://github.com/UBC-FRESH/femic/issues/371) | Rejects missing type/year/severity; ws4 reads two events |
| `efi.model.v1` model card | `DEC-04` | [#372](https://github.com/UBC-FRESH/femic/issues/372) | Two real model cards validate; FEMIC attaches them to attributes |

Contract home: **`femic/contracts`**, dependency-light, with a separate
`fresh-contracts` repo as the longer-term option.

### `femic`: EFI inventory attributes and biomass curves — P117

Parent: [#374](https://github.com/UBC-FRESH/femic/issues/374)

| Child | Candidate | Issue | Acceptance |
| --- | --- | --- | --- |
| ALS site-index layer | `INV-04` | [#375](https://github.com/UBC-FRESH/femic/issues/375) | Backtest against current SI; species limits enforced |
| Biomass curve family and carbon conversion | `GRO-06` | [#376](https://github.com/UBC-FRESH/femic/issues/376) | Monotonic where expected; declared carbon fraction |
| Area-based inventory model card and application | `INV-01` (wave 2) | not created | Attribute table carries model id and RMSE |

### `nemora`: uncertainty, sampling, and synthetic validation — P5

Parent: [#7](https://github.com/UBC-FRESH/nemora/issues/7)

| Child | Candidate | Issue | Acceptance |
| --- | --- | --- | --- |
| Curve uncertainty and 90% band | `DATA-01` | [#6](https://github.com/UBC-FRESH/nemora/issues/6) | Holdout coverage recorded; band emitted |
| Synthetic landscape fixture | `DATA-02` | [#8](https://github.com/UBC-FRESH/nemora/issues/8) | Known volume reproduced; ws4 build/simulate runs |
| Shared inventory ingest schema | `DATA-04` | [#9](https://github.com/UBC-FRESH/nemora/issues/9) | One path migrated; fixture byte-identical |
| sgsR sampling wrapper | `INV-06` | [#10](https://github.com/UBC-FRESH/nemora/issues/10) | Same inputs produce same allocation |

### `ws4`: environmental accounts (habitat and resilience) — P54

Parent: [#375](https://github.com/UBC-FRESH/ws4/issues/375)

| Child | Candidate | Issue | Acceptance |
| --- | --- | --- | --- |
| DHI biodiversity account | `BIO-01` | [#376](https://github.com/UBC-FRESH/ws4/issues/376) | AOI coverage; trajectory under two schedules |
| Structure habitat index | `BIO-02` | [#377](https://github.com/UBC-FRESH/ws4/issues/377) | Index computable; DHI comparison reported |
| Spatial resilience metrics | `PLAN-03` | [#378](https://github.com/UBC-FRESH/ws4/issues/378) | Identical schedules produce identical metrics |

P54 is used because P53 was taken by a release-preparation phase while this
handoff was in progress. Carbon is **not** in this parent; it is owned by FEMIC
P115 and ws4 P58.

## Carbon is adopted, not queued

`CARB-01` is covered by:

- `UBC-FRESH/femic` [#361 P115: Forest carbon domain](https://github.com/UBC-FRESH/femic/issues/361)
- `UBC-FRESH/ws4` [#357 P58: Forest carbon accounting](https://github.com/UBC-FRESH/ws4/issues/357)

The carbon drafts are in `handoffs/superseded/`. Do not create a parallel
carbon contract. The register marks `CARB-01` as `adopted`.

## Why this tree

- **One parent per repo phase.** The contracts, EFI attributes, Nemora
  validation, and ws4 environmental accounts are separable phases with
  different owners.
- **Each child has a consumer and an acceptance test.** A contract without a
  consumer is documentation, not integration.
- **Carbon stays with its live phase.** Duplicating it would create two carbon
  boundaries and two sets of accounts.
- **Phase setup is complete.** Branches `feature/p116-shared-contracts`
  (`0bc6cf8`), `feature/p117-efi-attributes` (`a0a7cbd`),
  `feature/p5-uncertainty-sampling` (`54604dc`), and
  `feature/p54-environmental-accounts` (`9b9b9bf`) are pushed; roadmap entries
  are committed; progress comments are posted. Implementation has not started.

## What not to do

- Do not create a single mega-issue across all five repos. It will not close.
- Do not create a child without a parent or a named consumer.
- Do not start wave 2 before the wave-1 contracts have a merged consumer.
- Do not copy the register into each repo. Link to it and keep one source of
  truth.
- Do not duplicate P79, P109, P114, P115, P58, P52, or P53.

## Next action

Each parent has a **Phase setup** checklist:

1. Create the phase branch from `main`.
2. Add the phase section to the target `ROADMAP.md`.
3. Link the parent issue.
4. Post a progress comment.

Then work the children in the order listed in the parent.
