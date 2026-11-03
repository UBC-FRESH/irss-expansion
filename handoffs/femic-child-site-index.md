Task identifier: P117.1
Parent phase issue: #374
Status: active
Branch: `feature/p117-efi-attributes`
Related planning: `ROADMAP.md` (Phase 117)
Source register: candidate `INV-04`

## Goal

Produce a spatially explicit site-index or potential-height layer from FEMIC's
LiDAR bundle and use it to select or adjust yield curves at fragment resolution.

## Scope

- Apply a published, species-specific SI/potential-height relationship to FEMIC
  LiDAR metrics.
- Add an optional `si_als` attribute with a model id, species, and applicability
  note.
- Backtest against the current TSA 48 or K3Z SI assignment and the ws4 P48/P49
  ground-plot validation surfaces where they apply.
- Report bias, RMSE, and the fragments whose curve assignment changes.

## Related live issue

- `UBC-FRESH/femic` #343 is a bug about the TSA 46 checkpoint SI understating
  managed-stand SI. That is a curve/checkpoint fix, not an ALS site-index layer.
  This task should not duplicate it; it should use the corrected checkpoint as a
  comparison if the fix lands first.

## Out of scope

- A new LiDAR pipeline. FEMIC P79 owns it.
- A universal SI equation for all species.
- A curve refit. This task selects or adjusts; it does not refit the curve.
- Carbon. It is owned by P115.

## Subtasks

- [x] Add the coefficients contract, linear application engine, domain checks,
  and backtest harness with a synthetic pilot card.
- [ ] Select a published or project site-index relationship and document its domain.
- [ ] Map FEMIC LiDAR metrics to the selected predictors.
- [ ] Add the `si_als` attribute to the fragment pipeline.
- [ ] Backtest on one instance with the P48/P49 ground-plot surfaces.
- [ ] Record the curve-selection changes.
- [x] Add tests for domain rejection, provenance, and backtest reproducibility.
- [x] Document the method and limits.

## Acceptance criteria

- The layer covers the pilot AOI, or the report names the gaps.
- The backtest reports a quantified difference from the current SI.
- A species outside the calibrated set is rejected or flagged, not silently
  predicted.
- The curve-selection changes are listed, not just counted.
- The tests fail if the model id or applicability note is dropped.

## Verification

```bash
python -m pytest
python -m ruff check .
python -m mypy src
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- SI adapter and provenance.
- Backtest report.
- Docs page and changelog entry.

## Risks

- **Species-specific equations.** Do not generalize without evidence.
- **Young-stand bias.** ALS height is not site height.
- **Temporal mismatch.** The LiDAR acquisition and inventory vintage differ.
- **Curve-selection churn.** A small SI change can move many fragments; report
  the distribution, not just the mean.

## Public sources

- Tompalski et al. 2022, site index of poplar clones from ALS:
  <https://doi.org/10.1139/cjfr-2021-0257>
- Gavilan-Acuna et al. 2022, potential height in radiata pine:
  <https://doi.org/10.1139/cjfr-2022-0121>
- FEMIC LiDAR product bundle:
  <https://github.com/UBC-FRESH/femic>
