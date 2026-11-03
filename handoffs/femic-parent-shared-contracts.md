Phase identifier: P116
Status: planned
Branch: `feature/p116-shared-contracts`
Roadmap: `ROADMAP.md`, section "Phase 116: Shared environmental contracts"
Pull request: not opened yet

Source register: IRSS x Silva21 expansion mine, candidates `GRO-01`, `DIS-01`, and `DEC-04`.

## Goal

Give FEMIC, ws3, ws4, FHOPS, and Nemora one shared vocabulary for the three
inputs that every environmental-intelligence feature depends on:

1. **Climate** — a canonical table and a ClimateNA/SilvR21 adapter.
2. **Disturbance** — a shared event record for fire, insect, drought, wind,
   partial mortality, and harvest.
3. **EFI model metadata** — a model card that travels with ALS-derived
   inventory attributes, so a consumer can tell what a layer predicts, how
   accurate it is, and where it applies.

The goal is interoperability, not new science. Each contract needs one real
consumer before the phase closes.

## Why now

- FEMIC already produces a versioned LiDAR product bundle (`femic.lidar.product.v1`)
  with sensor metadata, but it does not describe the inventory model that turns
  canopy metrics into attributes.
- ws4 has spatial, patch, road, and flow accounts, but no shared way to ingest a
  climate layer or a disturbance event.
- ws3 has a working CBM linkage and avoided-fire/avoided-harvest examples, but
  no shared climate or disturbance input.
- Building these three contracts separately in each repo would create three
  incompatible dialects.

## Scope

- `climate.v1`: tidied table keyed by AOI, variable, year, scenario, GCM, and
  source, with units, downscaling method, and provenance.
- `disturbance.v1`: event id, type, year, geometry or fragment ids, severity,
  attribution, confidence, source, and provenance.
- `efi.model.v1`: model id, version, target attribute, unit, predictors,
  training data, validation design, accuracy, applicability domain, and licence.
- One adapter/consumer per contract:
  - climate: a FEMIC or Nemora reader that validates units and provenance;
  - disturbance: a ws4 consumer that reads an event and reports it;
  - EFI: a FEMIC/Nemora attachment of a model card to an attribute table.

## Out of scope

- A new climate model, downscaling pipeline, or GCM ensemble selector.
- A new disturbance detection or attribution algorithm. The contract consumes
  existing detections.
- Rebuilding FEMIC P79's LiDAR source, materialization, terrain, canopy, tree,
  or bundle pipeline.
- FEMIC P114 hydrology or flood-risk work.
- A fire-spread simulator. ws4 P15/P16 already produced a documented negative
  result at the treated footprint; fire is a hazard or expected-loss input.
- A new data portal or a Silva21 data-sharing agreement.

## Child task checklist

- [ ] #370 `P116.1`: Add `climate.v1` and a ClimateNA/SilvR21 adapter (`GRO-01`)
- [ ] #371 `P116.2`: Add `disturbance.v1` and a ws4 consumer (`DIS-01`)
- [ ] #372 `P116.3`: Add `efi.model.v1` model cards (`DEC-04`)

## Contract home

**Decision (2026-10-25): `femic/contracts`.** Keep the package dependency-light
so ws3, ws4, FHOPS, and Nemora can import the schemas without FEMIC's full
modelling stack. A separate `fresh-contracts` repository remains the cleaner
long-term option, but it is not being created for this wave.

## Acceptance criteria

- Each schema has a validator that rejects a malformed record and a small
  example that round-trips.
- Each contract has at least one downstream consumer reading real data, not a
  mock.
- Provenance survives the round-trip: source, version, method, and licence are
  present in the consumer output.
- The tests can fail: a deliberately bad unit, missing scenario, missing
  disturbance type, or missing applicability domain is rejected.
- No new parallel LiDAR, hydrology, or fire-simulation lane is introduced.

## Verification

Run the repo's standard gates, including the dashboard if it exists, plus:

```bash
python -m pytest
ruff check src tests
mypy src
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Schema files and examples.
- Validator tests.
- One consumer per contract.
- A short contract page in the docs.
- A changelog entry naming the schema versions.

## Risks

- **Contract sprawl.** Three small contracts are useful; ten become a platform.
  Keep version 1 additive and minimal.
- **Repo coupling.** A shared package that imports a modelling stack will be
  rejected by at least one consumer.
- **Schema overreach.** Climate and disturbance vocabularies can grow without
  bound. Freeze a small controlled vocabulary and extend by version.
- **False confidence.** A valid schema does not make the data correct. The
  model card and provenance fields exist to keep that distinction visible.

## Phase setup

- [x] Create `feature/p116-shared-contracts` from the current `main`.
- [x] Add the Phase 116 section to `ROADMAP.md` and link `#369` (commit `0bc6cf8`).
- [x] Confirm the contract home (`femic/contracts`) and keep the package
  dependency-light.
- [x] Post a progress comment on `#369` when the branch and roadmap entry exist.

## Closeout requirements

- Squash-merge the phase pull request only after every child has a merged
  consumer and the dashboard is green.
- Record the schema versions, consumer links, and verification result in
  `CHANGE_LOG.md`.
- Close the parent only when all child issues are closed.
- Do not create a tag or release as part of this phase.

## Source register

- Candidate `GRO-01`: climate data contract and GCM ensemble.
- Candidate `DIS-01`: shared disturbance event schema.
- Candidate `DEC-04`: EFI model card and applicability metadata.
- Public sources: <https://www.silva21.com/climatedata?lang=en>,
  <https://irsslab.forestry.ubc.ca/research/disturbance-habitat-change/>,
  <https://irsslab.forestry.ubc.ca/research/lidar/>.
- Live-repo overlap check performed 2026-10-25; the planning packet is not yet published.
