# P117.1 data readiness

Checked 2026-10-26 against the local FEMIC instances. The application engine is
merged (`UBC-FRESH/femic#381`, `02aba7c`); this note records why a real
site-index backtest is not yet possible and what would unblock it.

## TSA46 ground plots

File: `external/femic-tsa46-instance/config/tsr/tipsy_ground_plot_validation.tsa46.csv`

- 20 rows.
- Fields: `species`, `age`, `observed_si`, `observed_height`, `observed_volume`,
  `observed_dbh`, `observed_stems`, `local_au`, `stratum_code`, `si_level`, and
  predicted counterparts.
- No ALS or CHM predictors. There is no CHM, canopy metric, or point-cloud
  product for these plots in the local instance.
- A site-index model cannot be applied or backtested here without acquiring ALS
  coverage and deriving the required metrics.

## TFL6 canopy pilot

Directory: `external/femic-tfl6-instance/runtime/dem/p79_7_canopy_pilot/canopy/`

- `chm.tif` and a 7-polygon `vri_canopy_comparison.csv`.
- Fields: `chm_p95_m`, `chm_mean_m`, `vri_height_m`, `vri_cover_pct`,
  `chm_cover_pct`, `valid_pixels`.
- No `observed_si`, and the area is TFL6 rather than the TSA46 ground-plot set.
- This is suitable for a **height/cover attribute model** (`INV-01`), not for a
  site-index backtest.

## What would unblock P117.1

1. **ALS coverage over the TSA46 ground plots**, with a CHM/canopy product that
   can be joined to `site_identifier` or plot coordinates.
2. **A published or project site-index coefficient set** whose predictors match
   the available ALS metrics and whose domain covers the plot species and age
   range.
3. **A join table** with plot id, species, age, observed SI, region/BEC, CHM
   metrics, and provenance.
4. **P48/P49 validation surfaces** for the comparison.

Alternative: use a SI plot network inside the TFL6 LiDAR footprint. That would
avoid acquiring new LiDAR but requires plot data the local instance does not
hold.

## What not to do

- Do not label the synthetic pilot card as a site-index result.
- Do not fit coefficients on the same plots used for the backtest without a
  pre-registered split.
- Do not join TFL6 height to TSA46 SI; they are different areas and populations.
- Do not treat VRI height as an independent observed SI.

## Candidate next actions

| Option | Cost | What it buys |
| --- | --- | --- |
| Acquire LidarBC tiles for a TSA46 plot pilot | Medium/high | A real ALS-SI backtest on existing ground plots |
| Use TFL6 CHM + VRI height for a height model | Low | A real EFI attribute demonstration, not SI |
| Obtain Domtar poplar trial data for the published Chapman-Richards model | Partner-dependent | A published-form SI model on its intended population |
| Defer P117.1 until a coefficient/data partner is available | Low | Keeps the queue honest |

The third option is the closest to the Tompalski et al. (2022) hybrid-poplar SI
model: that model is a Chapman-Richards top-height model requiring age, clone,
and fertilization status, not a simple linear CHM model.
