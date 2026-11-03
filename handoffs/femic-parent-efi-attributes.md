Phase identifier: P117
Status: planned
Branch: `feature/p117-efi-attributes`
Roadmap: `ROADMAP.md`, section "Phase 117: EFI inventory attributes and biomass curves"
Pull request: not opened yet

Source register: IRSS x Silva21 expansion mine, candidates `INV-04` and `GRO-06`.

## Goal

Turn FEMIC's existing LiDAR product bundle into inventory attributes and a
biomass curve family that the estate models can consume. The first two children
are a spatially explicit site-index layer and a biomass/carbon curve family.
Area-based volume, basal area, density, and species attributes follow as
`INV-01` once the model card from P116.3 exists.

## Why now

- FEMIC P79 already discovers, materializes, derives, and packages LidarBC
  products. The missing layer is the inventory model, not the sensor pipeline.
- FEMIC P115 is building the carbon package; it samples merchantable volume
  curves. A biomass curve family and a site-index layer improve the inputs to
  that lane without duplicating it.
- ws4 P48/P49 already published ground-plot validation surfaces that can test
  the site-index backcast.

## Scope

- A spatially explicit site-index / potential-height layer from ALS (`INV-04`).
- A biomass curve family and a declared carbon conversion (`GRO-06`).
- Provenance for the model, species, and curve version.
- A backtest against the current SI assignment and the ws4 P48/P49 validation.
- A comparison with the existing volume curve.

## Out of scope

- Rebuilding the FEMIC P79 LiDAR pipeline.
- The carbon package or CBM runtime. That is P115.
- FEMIC P114 hydrology.
- A new area-based model with no validation. `INV-01` is the later, broader
  child, and it depends on the P116.3 model card.
- A change to the estate model's objective.

## Architecture notes

- The LiDAR bundle is the input contract; do not add a second discovery or
  materialization path.
- Site index is an attribute, not a curve. It should carry a model id, species,
  and an applicability note.
- The biomass curve is a parallel curve family, not a replacement for the
  volume curve. The consumer chooses which family to use.
- Every derived attribute carries the model version and the source bundle id.

## Child task checklist

- [ ] #375 `P117.1`: Add an ALS site-index / potential-height layer (`INV-04`)
- [ ] #376 `P117.2`: Add a biomass curve family and carbon conversion (`GRO-06`)

## Acceptance criteria

- The site-index layer covers the pilot AOI and reports where it does not.
- The backtest against the current SI assignment reports bias, RMSE, and the
  fragments whose assignment changes.
- A species outside the calibrated set is rejected or flagged, not silently
  predicted.
- The biomass curve is selectable independently of the volume curve and carries
  its source and species.
- The carbon conversion uses a declared fraction and records the boundary.
- No P79 or P115 code is duplicated.

## Verification

```bash
python -m pytest
python -m ruff check .
python -m mypy src
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Phase setup

- [x] Create `feature/p117-efi-attributes` from the current `main`.
- [x] Add the Phase 117 section to `ROADMAP.md` and link `#374` (commit `a0a7cbd`).
- [ ] Confirm the model-card dependency from P116.3 (`#372`).
- [x] Post a progress comment on `#374` when the branch and roadmap entry exist.

## Closeout requirements

- Merge only when both children have a test that can fail and a provenance
  record.
- Record the model ids, bundle ids, and curve versions in the changelog.
- Do not tag or release as part of this phase.

## Risks

- **Model transferability.** Site-index equations are species- and region-
  specific. State the applicability domain.
- **Young-stand height bias.** ALS height is not site height. Reject or flag
  stands outside the calibrated age range.
- **Allometry.** Biomass curves carry belowground and species assumptions.
  Record them.
- **Double counting.** A biomass curve and a volume curve must not both be
  summed into the same account.

## Source register

- Candidate `INV-04`: site index and potential height from ALS.
- Candidate `GRO-06`: biomass yield curves from time-series remote sensing.
- Live-repo overlap check performed 2026-10-25; the planning packet is not yet published.
