# LidarBC pilot for P117.1

Date: 2026-10-26.

The new FEMIC P79 and ws4 P52/P59 modules were pulled from `origin/main` and
read before this pilot. The question was whether open LidarBC tiles can support
the real P117.1 site-index backtest.

## What was available

- FEMIC `origin/main` at `b71ea1a`, including P79 discovery, materialization,
  terrain, canopy, stream, tree, and bundle modules.
- ws4 `origin/main` at `f8117e5`, including P52 FEMIC bundle consumption and
  P59 LiDAR web UI.
- TSA46 ground-plot validation: 20 rows at 17 sites with `observed_si`,
  species, age, and height.
- Ground-plot coordinates: the non-PSP GBR header has generalized BC Albers
  coordinates; the VRI `FEATURE_ID` join gives a better label centroid for 11
  of 20 rows.

## What was downloaded

The site `1389961` (VRI centre 970085, 821042 in EPSG:3005) was the only site
with LidarBC point-cloud coverage in a 500 m search.

Command path:

```bash
femic lidar discover \
  --bbox 969800,820700,970200,821000 \
  --product point_cloud \
  --manifest-path $WORKDIR/lidar-pilot/sel_site1389961_pc.json

femic lidar materialize \
  --selection-manifest $WORKDIR/lidar-pilot/sel_site1389961_pc.json \
  --output-root $WORKDIR/lidar-pilot/site1389961
```

Result:

- tile `bc_093d038_4_4_3_xyes_8_utm09_2019.laz`
- 64.1 MiB, verified
- native CRS: UTM zone 9N (`EPSG:32609`)
- acquisition year: 2019
- actual point extent: 673479-674017 E, 5807419-5808607 N
- operator: NDMP Floodplains 2019 (`OP20BMC012`)

The selection tile bbox is larger than the actual point extent. The VRI
centroid at 970085,821042 is about 112 m east of the actual point extent.

## CHM sample

Using `laspy`, ground class 2 as the DTM, and a 20 m buffer around each VRI
label centroid:

| FEATURE_ID | Species | Age | VRI height (m) | VRI SI (m) | CHM mean (m) | CHM p95 (m) | CHM max (m) | Points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13572510 | FDC | 139 | 14.8 | 9.9 | 8.9 | 16.6 | 22.1 | 28,787 |
| 10008422 | HW | 219 | 23.9 | 10.3 | 14.8 | 29.3 | 39.8 | 41,777 |
| 10004451 | EP | 74 | 27.8 | 24.6 | 16.4 | 24.4 | 32.3 | 40,204 |
| 10004240 | DR | 54 | 16.2 | 16.1 | n/a | n/a | n/a | 0 |
| 10004917 | HW | 99 | 24.2 | 16.0 | n/a | n/a | n/a | 0 |

Two polygons have no points in the downloaded tile; the point coverage is
patchy inside the selection bbox.

## Coverage audit

A 500 m search around each of the 17 ground-plot sites found:

- point cloud: **1 site** (`1389961`);
- DEM: **2 sites** (`1341756`, `1389961`);
- DSM: **0 sites**.

A 5 km search found point clouds only at `1389961`. The open LidarBC coverage is
not a multi-site sample over these TSA46 plots.

## Implication

The download/materialization path works, but the open coverage and generalized
plot coordinates do not support a 17-site site-index backtest. A three-polygon
VRI comparison is not a model. The real P117.1 backtest remains blocked by data,
not by the FEMIC/ws4 modules.

## What would unblock it

1. A LidarBC-covered SI plot network with exact coordinates.
2. ALS coverage over the TSA46 ground plots, including point clouds or DSM.
3. A partner dataset for the published poplar top-height model.
4. Explicit approval to use VRI `SITE_INDEX` as a proxy target on a much larger
   polygon sample, with the circularity and inventory-estimate caveats stated.

## Not done

- No model coefficients were fit or fabricated.
- No VRI `SITE_INDEX` proxy model was trained.
- No tile beyond the one 64.1 MiB point cloud was downloaded.
- No production dataset, tag, or release was changed.
