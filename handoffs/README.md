# Handoff issue drafts

This directory holds the issue bodies for the IRSS x Silva21 expansion mine.

- Source register: `../registry/candidates.yaml`
- Issue-tree rationale: `../notes/08-handoff-issue-tree.md`
- Live-repo overlap check: `../notes/10-repo-state-check.md`

## Created issues

All wave-1 issues were created on 2026-10-25 with the maintainer's approval.
The parent/child links below are GitHub sub-issues.

| Repo | Issue | Candidate | Parent |
| --- | --- | --- | --- |
| `UBC-FRESH/femic` | [#369 P116: Shared environmental contracts](https://github.com/UBC-FRESH/femic/issues/369) | `GRO-01`, `DIS-01`, `DEC-04` | — |
| `UBC-FRESH/femic` | [#370 P116.1: climate.v1 + ClimateNA/SilvR21](https://github.com/UBC-FRESH/femic/issues/370) | `GRO-01` | #369 |
| `UBC-FRESH/femic` | [#371 P116.2: disturbance.v1 + ws4 consumer](https://github.com/UBC-FRESH/femic/issues/371) | `DIS-01` | #369 |
| `UBC-FRESH/femic` | [#372 P116.3: efi.model.v1 model cards](https://github.com/UBC-FRESH/femic/issues/372) | `DEC-04` | #369 |
| `UBC-FRESH/femic` | [#374 P117: EFI inventory attributes and biomass curves](https://github.com/UBC-FRESH/femic/issues/374) | `INV-04`, `GRO-06` | — |
| `UBC-FRESH/femic` | [#375 P117.1: ALS site-index layer](https://github.com/UBC-FRESH/femic/issues/375) | `INV-04` | #374 |
| `UBC-FRESH/femic` | [#376 P117.2: biomass curve family](https://github.com/UBC-FRESH/femic/issues/376) | `GRO-06` | #374 |
| `UBC-FRESH/nemora` | [#6 Curve uncertainty and 90% band](https://github.com/UBC-FRESH/nemora/issues/6) | `DATA-01` | #7 |
| `UBC-FRESH/nemora` | [#7 P5: Uncertainty, sampling, and synthetic validation](https://github.com/UBC-FRESH/nemora/issues/7) | `DATA-01`, `DATA-02`, `DATA-04`, `INV-06` | — |
| `UBC-FRESH/nemora` | [#8 P5.2: synthetic landscape fixture](https://github.com/UBC-FRESH/nemora/issues/8) | `DATA-02` | #7 |
| `UBC-FRESH/nemora` | [#9 P5.3: shared inventory ingest schema](https://github.com/UBC-FRESH/nemora/issues/9) | `DATA-04` | #7 |
| `UBC-FRESH/nemora` | [#10 P5.4: sgsR sampling](https://github.com/UBC-FRESH/nemora/issues/10) | `INV-06` | #7 |
| `UBC-FRESH/ws4` | [#375 P54: Environmental accounts (habitat and resilience)](https://github.com/UBC-FRESH/ws4/issues/375) | `BIO-01`, `BIO-02`, `PLAN-03` | — |
| `UBC-FRESH/ws4` | [#376 P54.1: DHI biodiversity account](https://github.com/UBC-FRESH/ws4/issues/376) | `BIO-01` | #375 |
| `UBC-FRESH/ws4` | [#377 P54.2: structure habitat index](https://github.com/UBC-FRESH/ws4/issues/377) | `BIO-02` | #375 |
| `UBC-FRESH/ws4` | [#378 P54.3: spatial resilience metrics](https://github.com/UBC-FRESH/ws4/issues/378) | `PLAN-03` | #375 |

P116 is complete: P116.1 merged #378, P116.2 merged #379 (ws4 #398), and P116.3
merged #380 for the contract plus #418 for two published cards and the
attribute annotation seam. Parent #369 is closed.

P5.2 (`DATA-02`, nemora #8) is complete: merged as nemora #13 (`d094c01`)
with the deterministic WS4 synthetic fixture and local build/simulate smoke
test. P5.3 (`DATA-04`, nemora #9) is complete: merged as nemora #12
(`9e7ea9e`) with the `nemora.inventory.v1` schema and HPS migration. P5.4
(`INV-06`, nemora #10) is complete: merged as nemora #14 (`2e8776c`) with the
optional sgsR R bridge. Parent #7 is closed.

## Additional integration follow-ons

These issues are derived from the live programme rather than a new candidate
row. They are recorded here so the handoff is not silent about adjacent
software work.

| Repo | Issue | Scope | Parent |
| --- | --- | --- | --- |
| `UBC-FRESH/femic` | [#392 P119: Site-index provenance and reconciliation](https://github.com/UBC-FRESH/femic/issues/392) | Consume VRI, VDYP, and SIBEC SI; report coverage, deltas, and conflicts; no new model | — |
| `UBC-FRESH/femic` | [#393 P119.1: reconcile VRI, VDYP, and SIBEC on TSA46](https://github.com/UBC-FRESH/femic/issues/393) | First implementation and pilot; merged #396 (`2a02fac`) | #392 |
| `UBC-FRESH/femic` | [#399 P119.2: SIBEC addendum and AU-level TSA SI](https://github.com/UBC-FRESH/femic/issues/399) | Follow-up gaps from the pilot; merged #415 (`b664025`) | #392 |

P119 is the software response to the `INV-04` rejection: site index is already a
provincial data product, so the useful work is provenance, reconciliation, and
deployment, not a new ALS model.

P54.1 (`BIO-01`, ws4 #376) is complete: the DHI
ingest/account/report/web-layer change merged as
[PR #463](https://github.com/UBC-FRESH/ws4/pull/463) (`b0438de`) on
`feature/p54.1-dhi-account`. The pilot uses a real SILVIS MODIS 6.1 Terra NDVI
2003-2022 500 m subset and synthetic test blocks; the account is reported, not
optimised.

P54.2 (`BIO-02`, ws4 #377) merged as #471 (`b4f7caa`) and was followed by a real
data run: the public LidarBC OP24BMRS001 2024 LAZ tiles were downloaded for the
TFL 6 1 km AOI, first returns were normalized with the FEMIC DEM, and the exact
Coops et al. (2016) index was computed for seven VRI blocks. The FEMIC bundle
still exposes CHM products only; that is a materialization gap, not a data
access blocker. See ws4 `examples/structure_habitat_tfl6` and PR #484.

P54 is complete: P54.1 #463 (`b0438de`), P54.2 #471 (`b4f7caa`), and P54.3
#475 (`865bef6`) are merged; parent #375 and children #376-#378 are closed. The
phase adds DHI, structure habitat, and resilience accounts, report blocks, the
DHI web layer, and the P54 close-out report. No objective or constraint change.

Phase numbers: FEMIC **P116** and **P117**; Nemora **P5**; ws4 **P54**. The ws4
number is P54 because P53 was taken by a release-preparation phase while this
handoff was in progress.

## P3 selected handoff

P3 selected `GRO-06` biomass yield curves as the first model-integration
handoff. The target is `UBC-FRESH/femic` P117 (#374), child P117.2 (#376), on
`feature/p117-efi-attributes`. The reviewed body is
[`femic-child-biomass-curves-p3.md`](femic-child-biomass-curves-p3.md). It is
written for the existing P117.2 issue, not a new issue, and it does not create or
edit a target issue, branch, or pull request.

The selection re-score is in
[`../notes/20-p3-model-integration-rescore.md`](../notes/20-p3-model-integration-rescore.md).
The earlier wave-1 draft remains at
[`femic-child-biomass-curves.md`](femic-child-biomass-curves.md) as the
historical issue text.

## Superseded by live carbon phases

`CARB-01` is **already covered** by work created before this handoff:

- `UBC-FRESH/femic` [#361 P115: Forest carbon domain, CBM packages, and GCBM export](https://github.com/UBC-FRESH/femic/issues/361)
- `UBC-FRESH/ws4` [#357 P58: Forest carbon accounting and carbon-aware planning](https://github.com/UBC-FRESH/ws4/issues/357) (carried as P51)

The carbon drafts are in `superseded/`. Do not create them. `CARB-01` is marked
`adopted` in the register with those links.

## Phase setup is done

Each parent's branch, roadmap entry, and progress comment are in place:

| Phase | Branch | Commit | Progress |
| --- | --- | --- | --- |
| FEMIC P116 | `feature/p116-shared-contracts` | `0bc6cf8` | [#369 comment](https://github.com/UBC-FRESH/femic/issues/369#issuecomment-6404475191) |
| FEMIC P117 | `feature/p117-efi-attributes` | `a0a7cbd` | [#374 comment](https://github.com/UBC-FRESH/femic/issues/374#issuecomment-6404475359) |
| Nemora P5 | `feature/p5-uncertainty-sampling` | `54604dc` | [#7 comment](https://github.com/UBC-FRESH/nemora/issues/7#issuecomment-6404475574) |
| ws4 P54 | `feature/p54-environmental-accounts` | `9b9b9bf` | [#375 comment](https://github.com/UBC-FRESH/ws4/issues/375#issuecomment-6404475795) |

The branches are pushed. No implementation, pull request, tag, or release was
created.

## Re-check before starting work

- **Re-read the live roadmap** in the target repo. The carbon and release
  phases appeared while this handoff was being written.
- **Confirm the phase number** still matches the roadmap. If a number is taken,
  renumber before creating the branch.
- **Do not duplicate P79, P109, P114, P115, P58, P52, or P53.**

## Draft files

The Markdown bodies in this directory match the created issues. They are kept
as the reviewable source of the issue text, not as a second queue.

- `femic-parent-shared-contracts.md` and its three children.
- `femic-parent-efi-attributes.md` and its two children.
- `nemora-parent-uncertainty-sampling.md`, `nemora-curve-uncertainty.md`, and
  its three children.
- `ws4-parent-environmental-accounts.md` and its three children.
- `superseded/` for the carbon drafts.

A post-merge P54 adoption run on the real North Island estate is recorded in
ws4 `notes/reports/p54-adoption-northisland.md`: DHI covered all 51,289 blocks,
baseline and retain-low diverged in retention/connectivity, and the structure
habitat index remains unavailable without the exact first-return metrics. This
is validation, not a new phase or objective change.

INV-05 is implemented in ws4 PR #490 (`d6cda2b`): the NTEMS 2022 dominant
species layer is ingested into a block/class fraction table with provenance and
compared with VRI. The TFL 6 pilot agrees on 4/6 comparable blocks; the public
layer is dominant-only, so mixedwood fractions remain a separate source need.

INV-05 is complete: ws4 PR #490 added the NTEMS dominant-species contract and
PR #492 added VRI species fractions and the mixedwood summary. The TFL 6 pilot
has 4/6 comparable leading-species matches and six mixed VRI blocks with
non-leading fractions 0.40-0.60. The public dominant layer is not used to invent
fractions.

The TFL6 species/AU check is also complete: 6/6 comparable VRI blocks have a
species combo matching the existing AU mapping; block 23339462 has neither VRI
species nor an AU row. See `femic-tfl6-instance` planning
`inv05_tfl6_au_consistency.md`. The AU/curve assignment was not changed.

The TSA 23 planned WS4 road network is now built in `UBC-FRESH/fresh-road`
(`df8ad2d`, example `tsa23_c5_network`). It uses paved DRA roads, active/pending
FTEN resource roads, three operating 100 Mile House mills, and a c5-style 600 m potential
grid with one diagonal per cell and four class variants. Existing segments have build cost 0; all 102,128
blocks are linked and routed. A report-only WS4 run loads the route
configuration and routes those blocks to the three mills (median 44.5 km). An
actual 5-year WS4 simulation on the 2,000-block baseline schedule routes all
volume with 0 unrouted blocks; product accounts are unchanged. The c5 network is
a single mill-connected component. The route config is promoted into
`femic-tsa23-instance` as `config/ws4/route_c5.yaml` (commit `d0d6cfa`); a
five-iteration optimizer smoke run scheduled 2,003 blocks with 0 unrouted route
rows and no objective/constraint change. Applying the route config to the
existing risk-optimized schedule produced 0 unrouted rows and identical common
product accounts; route costs are 11.23 M build, 60.89 M haul, 4.56 M
maintenance for 714 blocks (commit `1ca63b1`). The consolidated handoff is
`reports/ws4-c5-network-handoff.md` (commit `01cc53b`). A road-aware scenario with a
10 M build bound was added (commit `80abd88`); 100 iterations scheduled 2,031
blocks with 0 unrouted rows, but build remained 27.41 M, so the bound is a
benchmark, not a met policy. The c5-style grid is a 600 m lattice with
one diagonal per cell; the earlier 4 km grid was not the c5 pattern. The DRA-only graph remains an exploratory access
test. No WS4 objective, constraint, growth, solver, or compiled dataset was
changed.

DIS-04 is implemented in ws4 (PRs #499, #502, #503, #509): the public NTEMS fire
recovery layer is applied to all 102,128 TSA23 blocks. 1,497 blocks are not
recovered (21,948 ha), 58 are slower (745 ha). The 20-year deferral window moves
volume by only 0.069% (5 years) or 0.093% (10 years), so recovery remains an
informational overlay, not a hard constraint. No objective change was made.

DIS-02 now has a public implementation rather than only a data gate. The new
package is [UBC-FRESH/fresh-beast](https://github.com/UBC-FRESH/fresh-beast)
(`0.1.0a1`), which reads public HLS L30/S30 through Earthdata, masks the HLS
Fmask, builds 16-day NBR composites, runs the reference `Rbeast` BEAST
implementation with harmonic annual seasonality, and emits
`femic.disturbance.v1` block events. The package is separate from FEMIC and WS4;
WS4 remains the consumer.

The first real-data pilot is TSA 23 block 33140: 636 HLS granules, 183
composites, 840/840 pixels processed with Rbeast 1.0.2, valid finite composite
fraction 0.444, and **zero** events at the 0.5 negative-changepoint threshold.
The maximum in-block probability was 0.348 (2017), so this is a negative
control, not a positive NSR detection. The example and exact commands are in
`fresh-beast/examples/tsa23_block33140/`. No AOS validation, agent attribution,
severity mapping, or objective change is claimed.

A second `fresh-beast` pilot uses the archived all-years BC AOS layer, not just
the 2025 current layer. The 2024 polygon `154262024` is `IDW`, Western Spruce
Budworm, Severe, 28,888.56 ha, and covers all 20 TSA 23 blocks in a 1.1 km HLS
window (275.89 ha). HLS 2013-2025 produced 1,174 granules and 297 composites;
Rbeast 1.0.2 processed 1,444/1,444 pixels. The package emitted 60 events across
**19 of 20 blocks** (95% block-level sensitivity); 18 blocks had a 2023 event
and 7 a 2024 event. Block 1356 has events in 2018, 2020, and 2023; its latest
event is one year before the 2024 AOS capture. Block 98831 had no event at the
0.5 threshold. This is a positive-label cluster, not a case-control sample: all
20 blocks are inside the AOS polygon, so it does **not** estimate false
positives. `validation_cluster.json` records the metrics and caveats.

The 60-event table was consumed by the existing WS4 command and FEMIC validator:

```text
ws4 disturbance --events examples/tsa23_block1356_aos2024/events_all.json --block-id 1356
events: 3  years: 2018-2023  blocks: 1
femic.contracts.disturbance.validate_disturbance_event: 60/60 valid
```

No WS4 objective, growth, constraint, or solver code was changed; this is a
consumer test only.

The first case-control validation is negative. A 2019 AOS Aspen Leaf Miner
(`ID6`, Moderate) polygon in TSA 23, with 31 fully positive blocks and 47
controls (12 boundary blocks excluded), was processed with HLS 2013-2020
(924 granules, 183 composites, 3,876/3,876 pixels). The 0.5 threshold produced
37 events. At 2018-2020 the result is 8 true positives, 16 false positives,
23 false negatives, and 31 true negatives: sensitivity 25.8%, specificity
66.0%, precision 33.3%, accuracy 50.0%. Same-year 2019 detection is 0/31.

`fresh-beast` was therefore **not** promoted to operational use at the 0.5
threshold, and these events were not attached to any WS4/FEMIC objective,
growth, constraint, or solver. This is a validation result, not a new model
decision. The example and full metrics are in
`fresh-beast/examples/tsa23_id6_2019_case_control/validation_case_control.json`.

Decision after the case-control: **DIS-02 is deferred for operational use**.
The package and negative result remain public and reproducible, but its events
must not be attached to growth, scheduling, objective, or constraint logic.
Reopening it requires a new held-out validation design, not threshold tuning on
the 2019 case-control labels.

INV-09 has started as a separate public package:
[UBC-FRESH/fresh-road](https://github.com/UBC-FRESH/fresh-road) (`0.1.0a1`).
It wraps the published ALSroads implementation and emits the proposed
`fresh.road.status.v1` record, preserving the ALSroads state class instead of
inventing an open/closed label.

The first pilot uses LidarBC OP24BMRS001 2023 tile
`bc_092l055_3_4_3`, its 1 m DEM, and four unique DRA segments in TFL 6. Results:
`1820758` class 1 / 7.0 m; `1781964` class 4 / no traversable path / 100% cover;
`387113` class 1 / 7.8 m; `460555` class 1 / 11.5 m. The 1.7 GB LAZ and DEM
remain under `runtime/` and are not committed. The package is not yet a WS4
consumer and did not change routing, cost, objective, constraints, or solver.

Next: a second tile/independent status observation, then a report-only WS4 join
from `segment_id` to the existing road graph.

The INV-09 pilot now has a 2019 repeat acquisition of the same TFL 6 tile.
ALSroads class is stable for 4/4 segments between 2019 and 2023, but width and
score are not: segment `1820758` changes from 14.3 m to 7.0 m and segment
`460555` from 8.2 m to 11.5 m. This is repeat-acquisition consistency, not
ground-truth accuracy. The 2019 and 2023 raw point clouds/DEMs remain under
`runtime/`; only the small GPKG, JSON, CSV, and source manifest are versioned.

The WS4 report-only join is **not yet done**: the TFL 6 instance has DRA road
vectors but no WS4 route-edge graph with matching segment ids. The next concrete
step is to build or obtain that graph and map `dra:<id>` to the WS4 edge ids;
without that mapping a join would be a fabricated association. No WS4 files
were changed.

The INV-09 WS4 crosswalk fixture now exists in
`fresh-road/examples/tfl6_ledges/route_fixture/`: 18 vertices, 16 node-split
route edges, a one-to-many `dra_segment_id -> ws4_segment_id` crosswalk, and a
road-status-by-edge report. `destinations.csv` and `linkages.csv` are empty and
cost columns are zero. It validates the id mapping and loads through
`ws4.roads.network.RouteNetwork`, but it is explicitly **not** a complete TFL 6
route model and must not be used in an optimization. A real TFL 6 WS4 graph
with destinations and block linkages is still required.

The route test has moved to TSA 23, where public DRA vectors and the existing
block layer are sufficient. A 5 km AOI around block 33140 returned 450 DRA
lines and 356 TSA 23 blocks. The report-only fixture has 6,881 vertices, 6,921
route edges, a one-to-many DRA-to-edge crosswalk, nearest-vertex linkages, and
no destinations or costs. It loads through `RouteNetwork.from_tables`
(`segments=6921 vertices=6881 blocks=356 destinations=0`).

Access diagnostics: median block-to-vertex distance 109.1 m, p90 343.9 m, max
1,020.2 m. The graph has 10 connected components; the largest contains 6,566
vertices and 323/356 blocks. This is a topology/access test, not a route-cost or
harvest-feasibility result. Cost columns are zero and no destinations are
invented. The TFL 6 ALS road-status pilot remains a separate status test.

The TSA 23 route test now has a real mill destination. `fresh-road/examples/
tsa23_mill_route/` uses 1,414 DRA lines, 729 blocks, 18,314 route edges, and
West Fraser 100 Mile House (`MILL_ID 95`, LBR, Op) as the single destination.
`RouteNetwork` loads with one destination; **727/729** blocks route to the mill.
Median route length is 6,550 m (p90 9,542 m, max 11,265 m); blocks `20222` and
`67577` are in small disconnected components. Cost columns are zero: this is a
route-length test, not a cost or optimization result. No WS4 objective,
constraint, growth, or solver code was changed.

The two unrouted TSA 23 blocks (`20222`, `67577`) are now classified in
`block_access_status.csv` as `no_route_in_dra_graph`; both share nearest route
vertex 671 and are 777.9 m from the nearest DRA line. No connector or zero-length
access link was invented. Cost columns remain zero; the mill route test is
route-length only.

A partial TR-28 build-cost scenario is now in the TSA 23 mill route example.
The `Caterpillar 235 hydraulic backhoe` 2024 unit cost (28.7654 CAD/m) from
FERIC TR-28 via FHOPS is applied as subgrade reconstruction cost to every route
edge (`segments_tr28.csv`). Shortest-length route build costs are in
`route_build_costs_tr28.csv`: median 188,422 CAD, p90 235,962 CAD, maximum
324,034 CAD. This is **not** current existing-road maintenance or haul cost,
does not include total delivered cost, and is not an optimization input.

A WS4 report-only join is now built for the TSA 23 route test:
`fresh-road/examples/tsa23_mill_route/ws4_route_report.csv`. It joins the route
length and TR-28 partial build cost to the TSA 23 compiled WS4 block table:
729 blocks, 6,807.75 ha, 727 routed blocks / 6,801.06 ha. The two unrouted
blocks remain explicit. This is report-only; no WS4 objective, constraint,
solver, growth, or compiled dataset was changed.

A partial FHOPS haul scenario is now joined into the TSA 23 route report. It
uses the public `examples/hauling` highway truck (45 m3, 1.20 CAD/min), a
37 km/h scenario speed derived from that example's travel-time/distance pairs,
and round-trip variable travel only. Median haul variable cost is 0.567 CAD/m3
(p90 0.825, max 0.974). It excludes fixed truck day, loading/unloading,
overtime, maintenance, and profit; it is not a delivered-cost model. No WS4
objective, constraint, solver, growth, or compiled dataset was changed.

The full TSA 23 route graph is now built at
`fresh-road/examples/tsa23_full_route/`: 90,198 DRA edges, 80,733 vertices,
102,128 blocks, and the 100 Mile House mill destination. 99,335 blocks route
(median 59.5 km, p90 93.5 km, max 153.9 km); 2,793 blocks are explicitly
`no_route_in_dra_graph`. The graph has 779 components and uses zero costs.
`ws4_route_report_full.csv` covers 988,816 ha of WS4 block area. No WS4
objective, constraint, solver, growth, or compiled dataset was changed.

TSA 23 route topology cleanup was attempted with `unary_union` + `linemerge`:
90,198 DRA features became 83,187 merged parts, but connected components fell
only 779 -> 778 and routed blocks 99,335 -> 99,289 (unrouted 2,793 -> 2,839).
The remaining gaps are DRA source connectivity, not duplicate vertices. No
snap tolerance or invented connectors were applied. Do not add full-graph
costs or start PLAN-05 until those gaps are resolved or explicitly classified.

INV-01 now has a first contract implementation in `UBC-FRESH/femic` branch
`feature/inv01-inventory-als` (commit `01b5635`): `femic.inventory.als.v1`
output, `femic.inventory.als.model.v1` model-card input, `femic lidar
inventory`, optional plot/observation validation, and tests. The fixture model
is a synthetic identity model; no ABA coefficients or operational inventory
claim is made, and the P48/P49 plot tables remain external validation inputs.

INV-01 follow-up (2026-10-29): a published Wulder et al. (2012) boreal
model was transferred to the TFL 6 CWH pilot using a 25 m CHM grid. The run
produced 1,459 cells (mean Lorey height 18.14 m, basal area 18.92 m2/ha, gross
volume 85.39 m3/ha) and strongly underpredicted a conventional VRI comparison
(height 19.91 vs 28.25 m; BA 22.24 vs 66.89 m2/ha; volume 106.21 vs 397.30
m3/ha). This is rejected as an operational CWH/TSA 23 input; it is a transfer
benchmark. Evidence: `femic/notes/reports/inv01-als-transfer-tfl6.md` and
`config/inventory/models/`. Real P48/P49 field-plot validation is still absent.

INV-01 local CWH pilot (2026-10-29): fitted three local cards from 14 public
FAIB PSP plots and LidarBC 2023/2024 CHMs (9 plots held out with 4-6 year
offsets). LOOCV RMSE: height 2.14 m, basal area 9.27 m2/ha, volume 62.22
m3/ha. Applied to 1,289 TFL 6 forest cells: mean height 22.08 m, BA 37.27
m2/ha, volume 309.08 m3/ha. Against six VRI polygons: height 25.36 vs 28.25 m,
BA 39.87 vs 66.89 m2/ha, volume 379.69 vs 397.30 m3/ha. Volume is close but BA
is still materially low; this is a 14-plot CWH northern Vancouver Island pilot,
not an operational TSA 23 model. Evidence:
`femic/notes/reports/inv01-cwh-local-model-tfl6.md`; commit `9cf0ce0`.

INV-01 clean PR: `UBC-FRESH/femic#469` on branch
`feature/inv01-inventory-als-clean`, cherry-picked onto current `origin/main` from
the earlier dirty feature branch. It contains only the three INV-01 commits and
no Knife Creek/submodule history. Verification in the clean worktree: 50
LiDAR inventory/product/CLI tests passed, ruff/mypy clean, Sphinx `-W` clean.
GitHub checks: guard, package-release-checks, and build all pass; mergeable.
INV-01 merged (2026-10-30): `UBC-FRESH/femic#469` merged as `e9c0031`.
Registry status changed to `adopted`, with the resolution explicitly limiting
the local CWH model to a 14-plot pilot. CI passed (`guard`,
`package-release-checks`, `build`). Branch cleanup: clean branch deleted;
old dirty branch remains historical only and should not be used.

INV-01 TSA 23 feasibility (2026-10-30): not impossible; FAIB PSPs are usable.
In the 100 Mile House TSA there are 190 public FAIB plots, 25 measured since
2018, and 22/25 have LidarBC point-cloud coverage within +/-2 years. The
limiting layer is 1 m DEM/DSM: 14 IDF plots have it, but only 7 have a
plot-visit/CHM offset <=2 years (the other 6 are 2018/19 ground vs 2024 CHM,
offset 5-6 years; one is 5 years). So the current 1 m CHM route does not yield a
credible TSA 23 sample. The fix is to compute first-return point-cloud metrics
for the 2019 acquisitions (available for the old plots) or find additional
contemporaneous plots; do not fit a TSA 23 model from the 7-plot CHM subset.

INV-01 TSA 23 IDF pilot merged (2026-10-30): `UBC-FRESH/femic#470` merged as
`5ea8319`. Used 14 IDF plots with LidarBC 2019/2024 first-return point clouds
and exact FAIB plot support; LOOCV RMSE is 0.688 m height, 4.414 m2/ha basal
area, and 20.666 m3/ha volume. The cards are `als_tsa23_idf_*_2026.json`.
This is still a 14-plot pilot with no spatial holdout and no P48/P49
validation; no wall-to-wall TSA 23 feature grid or map exists yet.

INV-01 point-cloud grid merged (2026-10-30): `UBC-FRESH/femic#471` merged as
`71f60f0`. Adds `femic lidar inventory-pointcloud-features` and
`build_pointcloud_grid_features` for non-overlapping LAS/LAZ tiles plus a
co-registered DEM. One TSA 23 tile produced 3,857 25 m cells; 3,328 were inside
the IDF height-card range and 2,196 inside the BA/volume ranges. In-domain mean
height 18.13 m, BA 30.83 m2/ha, volume 201.50 m3/ha. This is a partial one-tile
pilot; no independent P48/P49 validation or full TSA 23 grid exists.

INV-01 five-tile mosaic (2026-10-30): `UBC-FRESH/femic#472` merged as
`3fcdf5f`. Fixed compound-CRS handling (point cloud EPSG:3157 + DEM
EPSG:6653) and combined five non-overlapping TSA 23 tiles: 19,034 cells;
17,709 height-card cells and 11,254 BA/volume cells in domain. In-domain mean
height 16.90 m, BA 26.19 m2/ha, volume 161.34 m3/ha. Map layer in
`$WORKDIR/inv01_tsa23/tsa23_idf_mosaic_5tile.geojson` (not tracked).
Still partial: five tiles, no spatial holdout, no P48/P49 validation, and the
VRI comparison is incomplete.

INV-01 ten-tile mosaic (2026-10-30): `UBC-FRESH/femic#473` merged as
`fa71896`. 36,433 cells; 33,255 height-domain and 19,891 BA/volume-domain
cells. In-domain mean height 16.59 m, BA 26.20 m2/ha, volume 159.31 m3/ha.
Leave-one-tile-out RMSE: height 0.690 m, BA 4.435 m2/ha, volume 20.694 m3/ha.
The spatial test is weak (12 tile groups, 14 plots; only one tile has >1 plot),
and VRI comparison remains incomplete. Map layer:
`$WORKDIR/inv01_tsa23/tsa23_idf_mosaic_10tile.geojson` (not tracked).

INV-01 TSA 23 large pilot (2026-10-30): `UBC-FRESH/femic#474` merged as
`cc3c8ce`. Ran 5,899 point-cloud/DEM tile pairs in 93 batches on Sockeye, using
Globus/scratch and a global 25 m grid. After boundary filtering/dedup:
9,523,476 feature cells; 6,573,196 height-domain cells; 2,942,755 BA/volume
cells. Means: height 16.09 m, BA 23.87 m2/ha, volume 139.33 m3/ha. Coverage is
64% of TSA 23 by tile footprint and 48% by modelled cell area; 907 point-cloud
tiles had no matched 1 m DEM. Raw LAZ (~2.0 TB) and parts are archived in
Chinook via Globus. S3 object reads remain blocked by policy. No independent
P48/P49 validation yet.

INV-01 full-run reproducibility (2026-10-30): `UBC-FRESH/femic#475` merged as
`6dd15f1`. Adds the tracked runbook at `examples/inv01_tsa23_full/`, the Sphinx
guide `docs/guides/inv01-tsa23-full-run.rst`, machine-readable evidence at
`notes/reports/inv01-tsa23-full-mosaic.json`, exact Globus task IDs/timings and
artifact hashes in the full-run report, and `--grid-origin-x/y` and
`--source-tile` on `femic lidar inventory-pointcloud-features`.

INV-01 validation screen (2026-10-30): `UBC-FRESH/femic#476` merged as
`882ad01`. VRI reconciliation (not independent validation) shows cell-level
height bias -2.48 m / RMSE 7.65 m, BA +4.61 / 11.49, volume +29.46 / 92.83. The
907 omitted point-cloud tiles cover 1,962 km2 inside TSA 23 (15.9%), including
1,778 km2 VRI forest and 861 km2 THLB; 2,466 km2 has no public point cloud in the
selection. Reports: `notes/reports/inv01-tsa23-vri-reconciliation.md` and
`notes/reports/inv01-tsa23-gap-priority.md`; guide:
`docs/guides/inv01-tsa23-validation.rst`. Do not use the current surface as an
operational inventory.

INV-01 PSP holdout (2026-10-30): `UBC-FRESH/femic#477` merged as `cf129af`;
applicability clarification in `#478` (`bda6099`). Full FAIB PSP archive fetched
via Nemora: 200 TSA 23 sites, 162 IDF, 455 visits; 22 recent LidarBC-matched
visits; four independent IDF plots processed with the 2019 layer-6 DEM. Holdout
RMSE: height 1.46 m, BA 8.35 m2/ha, volume 118.21 m3/ha (volume bias +89.27).
The four plots are mostly outside the published card ranges (3/4 BA/volume,
1/4 height), so this is an extrapolation stress test, not an in-domain
validation; the map would leave them unmapped. A same-18 refit did not improve
tile-level CV. Report: `notes/reports/inv01-tsa23-psp-holdout.md`. Next: add
high-biomass IDF plots with LidarBC support and widen the cards; do not just
refit the same 18 or wait.

INV-01 high-biomass increment (2026-10-30): `UBC-FRESH/femic#480` merged as
`641021a`. Fetched/processed 8 usable TSA 29 IDF high-biomass plots (177-383
m3/ha) and fitted on 14 TSA 23 + 8 TSA 29, testing on the 4 TSA 23 external
plots. Candidate vs current: height RMSE 2.032 vs 1.462; BA 7.823 vs 8.351;
volume 79.984 vs 118.207 (bias +53.4). Keep current height card; BA/volume
candidate is promising but not publishable. TSA 29 is not a TSA 23 validation
sample. Report: `notes/reports/inv01-tsa23-high-biomass-refit.md`. All project
data under `$FRESH_SCRATCH/inv01-data`, outside the repository.

TSA23 public instance (2026-10-30): `UBC-FRESH/femic#482` merged as `592086c`.
Added `external/femic-tsa23-instance` as a git submodule pointing at
`https://github.com/UBC-FRESH/femic-tsa23-instance` and documented TSA23 as the
public WS4/FEMIC demo instance home.  Future WS4 model/case artifacts should be
committed in the public instance repo, then the parent submodule pointer bumped.

INV-01 public instance artifacts (2026-10-30): `UBC-FRESH/femic-tsa23-instance#19`
merged as `b49d22c`; parent pointer bumped in `UBC-FRESH/femic#483` as
`6941bcd`. The public instance now carries the three TSA23 IDF pilot cards,
model-card README, INV-01 Sphinx page, full-mosaic/VRI/PSP-holdout/gap reports,
figures, priority GeoPackage, and high-biomass experiment evidence. The cards
remain explicitly pilot-only; raw data stays in Chinook.

INV-01 domain caveats (2026-10-30): parent `UBC-FRESH/femic#484` (`af34e08`)
adds explicit card-range caveats; public instance `#20` (`d60d934`) updates the
cards and model README; parent pointer `#485` (`4726f93`). TSA22 is Okanagan and
excluded from TSA23 training. TSA29 remains an exploratory transfer experiment.
The full PSP audit found only 4 TSA23 IDF plots with high-biomass ground data and
LidarBC support; there are no additional TSA23 high-biomass plots in the current
archive. Do not extrapolate the cards above `Lhmean` 14.1882 m or `Lhp95` 24.07 m.

INV-01 acquisition shortlist (2026-10-30): parent `UBC-FRESH/femic#486`
(`c5c7341`), public instance `#21` (`0ed0a21`), parent pointer `#487`
(`d18201c`). Nearest recent high-biomass no-lidar target: `4033798` (2022,
238.8 m3/ha). Ten older high-biomass TSA23 IDF sites need remeasurement plus
lidar before fitting. Report:
`notes/reports/inv01-tsa23-high-biomass-acquisition-targets.md`.

INV-01 model-status mask (2026-10-30): parent `UBC-FRESH/femic#488`
(`3ddb696`), public instance `#22` (`6237891`), parent pointer `#489`
(`2e90a47`). The three-band 25 m status mask is at
`$FRESH_SCRATCH/inv01-data/inv01_tsa23/tsa23_model_status_25m.tif`.
TSA-wide: no public point cloud 20.0%, omitted/no fine DEM 15.7%, processed/no
model cell 16.1%, height only 33.3%, BA/volume valid 14.9%. Acquisition request:
`notes/reports/inv01-tsa23-acquisition-request.md`.

INV-01 acquisition bundle (2026-10-31): parent `UBC-FRESH/femic#490`
(`a7803a8`), public instance `#23` (`e634b5c`), parent pointer `#491`
(`ee9d0d5`). Sender-ready package at
`notes/reports/inv01-tsa23-acquisition-bundle/`: request letter, targets CSV,
GeoJSON, map, JSON request, and SHA256 manifest. Priority `4033798` plus ten
historical high-biomass sites; target 20-30 current TSA23 IDF field+lidar plots.

INV-01 regional open-data calibration (2026-10-31): parent
`UBC-FRESH/femic#492` (`2b3f626`), public instance `#24` (`7cf2753`), parent
pointer `#493` (`c93be4a`). Used 46 BC high-biomass IDF PSP/LidarBC candidates,
24 usable features; trained on 14 TSA23 + 19 non-TSA23 high plots and tested on
the four TSA23 external plots. Volume RMSE 118.207 -> 42.484 and bias +89.267 ->
-3.370. BA refinement (`UBC-FRESH/femic#494`, `77b274a`) improves BA RMSE
8.351 -> 6.670 and bias +0.931 -> -3.807; height keeps current card. Public
instance `#25` (`750d508`), parent pointer `#495` (`bf04888`). Candidate
cards are under `experiments/inv01-regional-calibration/`, experimental only.
Report: `notes/reports/inv01-tsa23-regional-calibration.md`.

INV-01 full-grid regional coverage (2026-10-31): parent `UBC-FRESH/femic#496`
(`ed1b966`), public instance `#26` (`ed4fe72`), parent pointer `#497`
(`9db5c5e`), status figure `#498` (`cd1c1ff`). Applied regional BA/volume
candidates to all 9,523,476 feature cells. Joint BA/volume coverage 14.9% ->
23.6% (1,839 -> 2,913 km2); height stays 33.3%. Current status: no point 20.0%,
omitted/no DEM 15.7%, processed/no model 29.5%, height-only 20.0%, BA/vol 14.9%.
Candidate status: processed/no model 26.0%, height-only 14.8%, BA/vol 23.6%.
Report: `notes/reports/inv01-tsa23-regional-inventory.md`.

INV-01 regional model bundle (2026-10-31): parent `UBC-FRESH/femic#499`
(`37ee6a4`), public instance `#27` (`a07a5e1`), parent pointer `#500`
(`d8c0ba7`). Loadable BA/volume cards, manifest/checksums, and leave-one-TSA-out
CV are under `experiments/inv01-regional-calibration/model_bundle/`. Cross-region
volume RMSE is 16-101 m3/ha (TSA2/18 weak, TSA29 moderate), so the cards remain
experimental. Reports: `notes/reports/inv01-tsa23-regional-calibration.md` and
`notes/reports/inv01-tsa23-regional-inventory.md`.

INV-01 wording cleanup (2026-10-31): parent `UBC-FRESH/femic#501` (`8cab5c1`),
public instance `#28` (`6aebf49`), parent pointer `#502` (`7a64fc1`). Removed
stale acquisition-gate phrasing from the regional evidence.

INV-01 nonlinear volume candidate (2026-10-31): parent `UBC-FRESH/femic#503`
(`f0ec373`), public instance `#29` (`83f101d`), parent pointer `#504`
(`2dc7270`). Polynomial log-volume model improves cross-region average RMSE to
~35.5-40.3 m3/ha; TSA23 external RMSE remains ~42.1. Full-grid volume cells
4,745,557; mean 170.84 m3/ha; status unchanged. Experimental spec at
`experiments/inv01-regional-calibration/nonlinear_volume/`.

INV-01 hybrid bundle (2026-10-31): parent `UBC-FRESH/femic#505` (`b33d71a`),
public instance `#30` (`c8b1241`), parent pointer `#506` (`777fb9d`). Paired
linear BA + nonlinear volume + current height. External BA RMSE 6.670, volume
42.092; cross-region volume RMSE 3.6-67.1 m3/ha. Full-grid 23.6% joint
BA/volume, mean volume 170.84 m3/ha. Path:
`experiments/inv01-regional-calibration/hybrid_bundle/`.

INV-01 term-based model path (2026-10-31): parent `UBC-FRESH/femic#507`
(`fb9dd51`), public instance `#31` (`800b8f3`), parent pointer `#508`
(`e11d082`). FEMIC now supports `model_type: log_terms` with constant, log,
log-square, and log-product terms; the hybrid polynomial volume card loads
through the standard model reader. 18 inventory tests pass.

INV-01 CLI parity (2026-10-31): parent `UBC-FRESH/femic#509` (`ac8b316`),
public instance `#32` (`7b54c3c`), parent pointer `#510` (`bbef1e2`). Standard
`femic lidar inventory` produced 7,479,672 BA rows and 4,745,557 volume rows;
max absolute difference versus the script surface was 4.3e-14 (BA) and 2.2e-12
(volume). Report: `notes/reports/inv01-tsa23-cli-parity.md`.

INV-01 experimental model root (2026-10-31): parent `UBC-FRESH/femic#511`
(`e30c932`), public instance `#33` (`0ee35cb`), parent pointer `#512`
(`e6c2c56`). TSA23 instance default experimental root is
`config/inventory/models/experimental/` with `config/inventory/experimental.yaml`.
The hybrid BA + term-based volume cards run through the standard `femic lidar
inventory` path; script-only application is no longer the documented workflow.

INV-01 config-driven inventory CLI (2026-10-31): parent `UBC-FRESH/femic#513`
(`5000ef3`). `femic lidar inventory` accepts `--model-key height|ba|volume`
with optional `--model-config` (default `config/inventory/experimental.yaml`),
resolving relative model paths from the instance root. Tests: 20 passed.

INV-01 hybrid versus current (2026-10-31): parent `UBC-FRESH/femic#514`
(`95b253f`), public instance `#34` (`b112dfa`), parent pointer `#515`
(`c610203`). Joint BA/volume coverage 14.9% -> 23.6%; overlap BA RMSE 4.66,
volume RMSE 12.45. Hybrid is the default experimental inventory root; current
cards stay published and non-operational. Report:
`notes/reports/inv01-tsa23-hybrid-vs-current.md`.

INV-01 TSA23 spatial holdout (2026-10-31): parent `UBC-FRESH/femic#516`
(`86961be`), public instance `#35` (`1184191`), parent pointer `#517`
(`9c350eb`). Leave-one-TSA23-tile-out across 13 tiles and 18 plots: BA RMSE
6.188 m2/ha, volume RMSE 25.473 m3/ha. The four-plot high-biomass tile remains
hardest (BA 6.670, volume 42.092). Hybrid stays experimental; no operational
promotion. Report: `notes/reports/inv01-tsa23-spatial-holdout.md`.

INV-01 config CLI parity (2026-10-31): parent `UBC-FRESH/femic#518`
(`7f2bab1`), public instance `#37` (`10335f6`), parent pointer `#519`
(`beed670`). Full-grid `--model-key` runs over 7,479,672 BA rows and 4,745,557
volume rows are byte-identical to the explicit-path CLI outputs. Instance model
cards now carry the spatial-holdout metrics (`#36`). Report:
`notes/reports/inv01-tsa23-cli-parity.md`.

INV-01 independent BC IDF validation (2026-11-01): parent
`UBC-FRESH/femic#520` (`e8fda32`), public instance `#38` (`55a4301`), parent
pointer `#521` (`aa475ef`). The four high-biomass plots were only the external
tile. Coverage: 969 latest IDF PSP plots; 573 with LidarBC point + DEM; 111
within five years; 88 usable feature rows; 56 independent. Independent BA RMSE
8.02 m2/ha (54 in range), volume RMSE 62.93 m3/ha (44 in range). The seven
independent TSA23 plots give BA RMSE 15.02; no independent TSA23 volume plot is
in range. Hybrid remains experimental and not operational. Report:
`notes/reports/inv01-tsa23-bc-validation.md`.

INV-01 CLI parity metadata (2026-11-01): parent `UBC-FRESH/femic#522`
(`6dcd359`), public instance `#39` (`3ade12b`), parent pointer `#523`
(`b24cf65`). Config-driven prediction columns remain identical; new CSV hashes
record corrected RMSE metadata.

INV-01 default published config (2026-11-01): parent `UBC-FRESH/femic#524`
(`e504cb0`), public instance `#40` (`313d612`), pointer `#525` (`46054c9`);
research-only report alignment parent `#526` (`6848d99`), instance `#41`
(`ed01073`), pointer `#527` (`aa055df`). `femic lidar inventory` now defaults
to `config/inventory/default.yaml` (published TSA23 cards); the hybrid requires
`--model-config config/inventory/experimental.yaml` and is research-only. Tests:
21 inventory tests pass; a one-row default-config CLI run produced
`tsa23-idf-ba-2026`.

INV-01 refit and applicability (2026-11-01): parent `UBC-FRESH/femic#528`
(`32b20f5`), public instance `#42` (`9209d6c`), parent pointer `#529`
(`e613f7e`). Leave-one-TSA-out refit on 31 development plots; independent 56.
Selected BA is 8.05 all / 8.10 in-domain (fixed hybrid 7.93/8.02); selected
volume is 71.75 all / 52.06 in-domain (fixed hybrid 80.95/62.93), but no
independent TSA23 volume plot is in range. Neither promoted. Report:
`notes/reports/inv01-tsa23-refit-applicability.md`.

INV-01 strict validation/time-lag (2026-11-01): parent
`UBC-FRESH/femic#530` (`1290750`), public instance `#43` (`efd1152`), pointer
`#531` (`b05610e`). The 56-plot recent set included 18 fallback tiles at 6-11
years; strict 0-5 independent is 38 plots: hybrid BA 8.86 (36 in range), volume
67.02 (28 in range). Expanded 56: 8.02/62.93. Time-lag sensitivity over 435
independent plots: volume RMSE 67.02 at 0-5, 99.06 at 21-30, 116.44 beyond 30.
No model promoted. Reports:
`notes/reports/inv01-tsa23-bc-validation.md` and
`notes/reports/inv01-tsa23-time-lag.md`.

INV-01 time-aware refit (2026-11-01): parent `UBC-FRESH/femic#532`
(`41bbedc`), public instance `#44` (`8836dca`), parent pointer `#533`
(`1ba5d86`). Train on 431 non-strict plots with explicit lag; strict 38 test.
Time-aware BA 7.92 pooled but TSA23 11.50; time-aware volume 62.67 pooled but
TSA23 93.86. Not promoted; published cards remain default. Report:
`notes/reports/inv01-tsa23-time-aware-refit.md`.

INV-01 BA-height default (2026-11-01): parent `UBC-FRESH/femic#534`
(`f51fbac`), public instance `#45` (`3a3f451`), parent pointer `#535`
(`17b7f23`). The default config now contains height and BA only; volume is
withheld and requires the experimental config or an explicit model path.
Default CLI smoke test resolved `tsa23-idf-ba-2026`; volume key without config
raises `Inventory model config has no 'volume_model'`.

INV-01 P120 closure (2026-11-01): parent phase #536 and task #537 are closed;
P120 PR #538 merged as `98fe2c6`; instance #46 merged as `3b4f58a`; pointer
updated in main. Height failed strict validation (19 in-range, RMSE 2.54 m;
TSA23 strict 6, RMSE 4.18 m), so the default is BA-only (strict 36 in-range,
RMSE 8.86 m2/ha). Height and volume remain research-only. P120 governance
records the earlier pre-phase INV-01 history as a deviation; local ruff/mypy
baseline failures remain documented in `notes/reports/phase120-closeout.md`.

INV-01 P121 BA-only release (2026-11-01): parent phase #539 and task #540 are
closed; P121 PR #541 merged as `736c24d`; instance #47 merged as `b12b051`;
pointer in main. BA-only product: 2,942,755 rows and raster pixels, 14.9% TSA
coverage, BA mean 23.87 m2/ha. Manifest
`metadata/inv01/tsa23_ba_pilot_manifest.json`; release note
`notes/reports/inv01-tsa23-ba-pilot-release.md`. CI green; no tag/release.

INV-01 P122 BA-only acceptance (2026-11-01): parent phase #542 and task #543
closed; P122 PR #544 merged as `c34181b`; instance #48 merged as `4170451`;
pointer in main. Decision: accept as experimental, reject operational. Checks:
2,942,755 rows/pixels, 14.9% TSA coverage, strict BA RMSE 8.86 m2/ha, TSA23
independent BA RMSE 15.02. VRI/THLB coverage not computed because annex geometry
is not materialized. No tag/release.
