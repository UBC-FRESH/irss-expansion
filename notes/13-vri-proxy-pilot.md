# VRI-proxy pilot for P117.1

Date: 2026-10-26.

**Decision: parked.** P117.1 is not an integration task. A defensible new
general height/site-index model is research-scale. The EFI application and
backtest engine remains as generic infrastructure; no further model derivation
is queued here.

This pilot tests whether **VRI `SITE_INDEX`** can stand in for ground-truth site
index when building an ALS model. It uses real LidarBC point clouds and the
TSA46 VRI polygon layer.

The answer is a qualified no: VRI `SITE_INDEX` is an inventory estimate derived
from height and age, so a model that predicts it from CHM is partly circular.
The pilot is useful as a screening exercise, not as a validated site-index
model.

## Data

- VRI: `external/femic-tsa46-instance/data/vri_vclr1p_checkpoint5.feather`
  (171,826 polygons with `SITE_INDEX`).
- LidarBC: four 2019 point-cloud tiles around the TSA46 site `1389961` area,
  downloaded with FEMIC:
  - `bc_093d038_4_3_4_xyes_8_utm09_2019.laz`
  - `bc_093d038_4_4_3_xyes_8_utm09_2019.laz`
  - `bc_093d048_2_1_2_xyes_8_utm09_2019.laz`
  - `bc_093d048_2_2_1_xyes_8_utm09_2019.laz`
  - total 1.2 GiB, all verified by FEMIC materialization.
- Sample: 32 VRI polygons with `SITE_INDEX`, inside the actual point extent of
  at least one tile, with at least 100 valid 2 m CHM cells in a 20 m buffer.

## Method

For each tile:

1. Read the LAZ with `laspy`.
2. Build a 2 m DSM from the maximum z per cell and a DTM from the minimum z of
   ground-class (class 2) points; fill missing DTM cells by nearest ground cell.
3. CHM = DSM - DTM.
4. Sample CHM in a 20 m radius around each VRI label centroid.
5. Keep polygons with `SITE_INDEX`, at least 100 cells, and at least one tile
   overlap.
6. Deduplicate a polygon that appears in two tiles by keeping the sample with
   the most valid cells.

The target is VRI `SITE_INDEX` in metres. Predictors tested:

- CHM p95 alone.
- CHM mean alone.
- CHM p95 + VRI age.
- CHM p95 + VRI height.

## Sample

32 polygons, five species groups, age 34-269 years, VRI `SITE_INDEX` 9.9-29.8 m,
CHM p95 0.16-47.65 m.

A few representative rows:

| Feature | Species | Age | VRI height | VRI SI | CHM p95 |
| --- | --- | ---: | ---: | ---: | ---: |
| 10008422 | HW | 219 | 23.9 | 10.3 | 20.55 |
| 10008524 | EP | 74 | 22.9 | 19.6 | 35.19 |
| 10008321 | AC | 34 | 15.8 | 22.0 | 25.86 |
| 10008044 | AC | 69 | 33.6 | 29.8 | 30.55 |
| 10008349 | AC | 129 | 38.5 | 27.5 | 41.70 |
| 10004574 | AC | 59 | 24.4 | 23.2 | 17.52 |
| 10008474 | AC | 39 | 17.5 | 22.0 | 0.16 |

`10008474` is a clear tile/point-coverage failure: CHM p95 0.16 m for a 17.5 m
VRI stand. It was retained in the table to show that point coverage inside the
tile index is not guaranteed.

## Model results

Ordinary least squares, with leave-one-out (LOO) RMSE:

| Predictors | R² | RMSE (m) | LOO RMSE (m) |
| --- | ---: | ---: | ---: |
| CHM p95 | 0.109 | 5.91 | 6.37 |
| CHM mean | 0.169 | 5.71 | 6.11 |
| CHM p95 + age | 0.576 | 4.08 | 4.56 |
| CHM p95 + VRI height | 0.333 | 5.11 | 5.79 |

CHM alone is a weak proxy. Adding age raises R², but VRI `SITE_INDEX` is itself
derived from height and age, so this is not independent evidence that ALS can
predict site index. Adding VRI height is even more circular.

## Interpretation

- The 32-polygon sample is small, from one 2 km area, and unbalanced by species
  and age.
- VRI `SITE_INDEX` is an inventory estimate, not a measured site index.
- The point-cloud coverage is patchy: one tile has a near-zero canopy sample in
  an otherwise stocked polygon, and two VRI polygons in the earlier single-tile
  sample had no points.
- A production SI model needs ground plots with exact coordinates and ALS
  coverage, or a partner trial dataset.

## Decision

Do not train, tune, or ship a VRI-proxy site-index model from this pilot. Keep
it as screening evidence and as a reusable method for when better targets
arrive.

## Reproducibility

The downloaded tiles and the sample CSV (`vri_proxy_samples.csv`) are in
`$WORKDIR/lidar-pilot/`, which is working storage, not a tracked dataset.
The VRI and LidarBC sources are OGL-BC; any promoted derivative needs the same
licence and provenance treatment.
