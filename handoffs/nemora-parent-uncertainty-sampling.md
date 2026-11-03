Phase identifier: P5
Status: planned
Branch: `feature/p5-uncertainty-sampling`
Roadmap: `ROADMAP.md`, section "Phase 5: Uncertainty, sampling, and synthetic validation"
Pull request: not opened yet

Source register: IRSS x Silva21 expansion mine, candidates `DATA-01`, `DATA-02`,
`DATA-04`, and `INV-06`.

## Goal

Make Nemora the place where FRESH tests uncertainty, sampling design, synthetic
landscapes, and inventory ingest. The first issue (`DATA-01`, #6) is already
open. This phase adds the three wave-1 pieces that make it useful at scale:
synthetic landscapes, a shared ingest schema, and structurally guided sampling.

## Why now

- Nemora already has a distribution registry, fitting, sampling, ingest, and
  synthesis. The missing pieces are the cross-repo fixtures, the shared schema,
  and the sampling-design wrapper.
- FEMIC and ws4 need a way to test scale and edge cases without hand-built
  fixtures.
- The inventory ingest paths are duplicated; a shared schema removes the
  duplication before more candidates depend on it.

## Scope

- Curve uncertainty and a 90% band for one family (`DATA-01`, #6).
- A synthetic landscape/stand fixture with known properties (`DATA-02`).
- A shared tidy inventory ingest schema and one migrated path (`DATA-04`).
- A wrapper or port of the sgsR structurally guided sampling workflow (`INV-06`).
- A small validation surface for the synthetic fixtures and sampling designs.

## Out of scope

- A full measurement-campaign simulator. That is `DATA-03`, wave 2.
- A general SDM pipeline. That is `BIO-03`, wave 3.
- A new distribution-fitting theory or a Bayesian platform.
- Changing any downstream model's objective.

## Architecture notes

- The synthetic generator uses the existing `nemora.synthesis` tessellation,
  stand, and stem modules; it does not add a second generator.
- The shared ingest schema is a tidy table contract, not a new database.
- The sgsR wrapper may be a Python port or an R bridge; record the choice and the
  maintenance cost.
- Every fixture is seeded and reproducible.

## Child task checklist

- [ ] #6 `P5.1`: Add curve uncertainty and a 90% band for one curve family (`DATA-01`)
- [ ] #8 `P5.2`: Generate a synthetic landscape fixture with known properties (`DATA-02`)
- [ ] #9 `P5.3`: Publish the shared inventory ingest schema (`DATA-04`)
- [ ] #10 `P5.4`: Wrap or port sgsR structurally guided sampling (`INV-06`)

## Acceptance criteria

- The curve band is emitted and its coverage check is recorded.
- The synthetic fixture is deterministic from a seed and runs through ws4 build
  and simulate.
- The ingest schema rejects a missing key and reproduces the existing output on
  the fixture.
- The sampling wrapper produces the same allocation for the same inputs.
- Every child has a test that can fail and a docs note.

## Verification

```bash
python -m pytest
ruff check src tests
mypy src
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Phase setup

- [x] Create `feature/p5-uncertainty-sampling` from the current `main`.
- [x] Add the Phase 5 section to `ROADMAP.md` and link `#7` (commit `54604dc`).
- [x] Link the created `DATA-01` issue `#6` as a sub-issue (done).
- [x] Post a progress comment on `#7` when the branch and roadmap entry exist.

## Closeout requirements

- Merge only when each child has a reproducible example and a test.
- Record the fixture seeds and schema version in the changelog.
- Do not tag or release as part of this phase.

## Risks

- **Synthetic realism.** A synthetic landscape is a test fixture, not evidence
  about a real forest.
- **R/Python bridge.** The sgsR wrapper may add a maintenance dependency; record
  the fallback.
- **Schema drift.** Upstream FAIB/FIA/HPS schemas change; the nightly ingest is
  the early warning.
- **Scope creep into simulation.** `DATA-03` is a separate candidate.

## Source register

- Candidate `DATA-01`: distribution fitting and uncertainty propagation.
- Candidate `DATA-02`: synthetic forest/stand generator.
- Candidate `DATA-04`: open inventory ingest harmonization.
- Candidate `INV-06`: structurally guided sampling with sgsR.
- Live-repo overlap check performed 2026-10-25; the planning packet is not yet published.
