# Publication signals

This is a curated reading of the public record, not a citation index. It lists
the papers and projects that most directly change a FRESH design decision. The
full register has the per-candidate evidence; this note explains the pattern.

Reviewed: 2026-11-03 (P1.2). The 44 candidate references in this note all match
IDs in `registry/candidates.yaml`; no link was stale. The paper-level claims were
not re-read, and no candidate mapping changed.

## How to read the signal

- **Method** papers define an algorithm or workflow that could become an
  adapter.
- **Product** papers define a layer, index, or dataset that could be ingested.
- **Evidence** papers define a relationship (growth, mortality, risk) that
  could become a model modifier.
- **Validation** papers define a way to test a FRESH model against independent
  data.

## Inventory and LiDAR

The IRSS LiDAR programme is the most mature integration surface. The signal is
not "use LiDAR"; it is "the methods, metadata, and validation already exist, so
the remaining work is contracts and adapters."

| Year | Work | Type | Why it matters | Candidates |
| ---: | --- | --- | --- | --- |
| 2021 | Coops et al., *Modelling lidar-derived estimates of forest attributes over space and time: a review* (RSE 260, 112477) | Review | The map of what ALS can and cannot predict, and how those predictions age | `INV-01`, `INV-03` |
| 2023 | Goodbody et al., *sgsR: a structurally guided sampling toolbox for LiDAR-based forest inventories* (Forestry) | Method + tool | Ready-made sampling design and validation logic | `INV-06` |
| 2024 | Goodbody et al., *Integrating ALS into forest ecosystem management in Canada* (Forestry Chronicle) | Review | The operational adoption gap, not the sensor gap | `DEC-04`, `INV-01` |
| 2022 | Hermosilla et al., *Mapping the presence and distribution of tree species in Canada's forested ecosystems* (RSE 282, 113276) | Product | A national species layer that can drive composition | `INV-05` |
| 2023 | Queinnec et al., *Mapping dominant boreal tree species groups with ALS and Sentinel-2* (CJRS) | Method | Improves species fractions in mixedwoods | `INV-05` |
| 2022 | Riofrio et al., *Harmonizing multi-temporal ALS to derive periodic annual height increments* (CJFR) | Method | Turns repeat LiDAR into growth evidence | `INV-03`, `GRO-05` |
| 2023 | Riofrio et al., *Modelling height growth with multi-temporal ALS* (FEM 543, 121137) | Method | Age-independent growth trajectories | `GRO-05` |
| 2024 | Tompalski et al., *Developing aboveground biomass yield curves from time-series remote sensing* (FEM 561, 121894) | Product | A direct biomass/carbon curve family | `GRO-06`, `CARB-01` |
| 2022 | Tompalski et al., *Modeling site index of selected poplar clones using ALS* (CJFR) | Method | A spatial site-index route | `INV-04` |
| 2022 | du Toit et al., *Generating Douglas-fir breeding value estimates using ALS height and crown metrics* (Frontiers in Plant Science 13, 893017) | Method | Links LiDAR to realized genetic gain | `INV-10` |
| 2022 | Qi et al., *Comparing tree attributes from quantitative structure models based on drone and mobile laser scanning* (ISPRS 192) | Method | Tree-level taper and volume from point clouds | `OPS-06`, `INV-02` |
| 2024 | Irwin et al., *Prioritizing commercial thinning with high-density drone laser scanning* (Forestry) | Method | Within-stand competition and thinning priority | `OPS-01`, `INV-07` |
| 2026 | Irwin et al., *Framework for commercial thinning assessment with multitemporal lidar and spatially explicit growth simulation* (FEM 618, 124029) | Method | Connects LiDAR to a growth simulation, not just a map | `OPS-01`, `GRO-02` |
| 2025 | Olson et al., *The assessment of individual tree canopies using drone-based intra-canopy photogrammetry* (Computers and Electronics in Agriculture 234, 110200) | Method | Tree-level health and crown attributes | `INV-07` |
| 2022 | Marinelli et al., *Forest change detection in LiDAR using polar change vector analysis* (IEEE GRSL) | Method | Structural change, not just optical change | `INV-08` |
| 2022 | Roussel et al., *Correction, update, and enhancement of vectorial forestry road maps using ALS* (IJAEOG 114, 103020) | Method | Road status and access from remote sensing | `INV-09`, `OPS-05` |
| 2022 | Kuiper et al., *Characterizing stream morphological features using ALS* (RSE 272, 112948) | Method | Riparian and aquatic habitat metrics | `BIO-04` |

## Monitoring and disturbance

This is the second-most mature surface. The signal is a shift from **annual
land-cover change** to **continuous forest condition**, which is exactly the
state layer FRESH lacks.

| Year | Work | Type | Why it matters | Candidates |
| ---: | --- | --- | --- | --- |
| 2022 | Coops et al., *Framework for near real-time forest inventory using multi-source remote sensing* (Forestry) | Framework | The blueprint for a continuous inventory loop | `INV-01`, `DIS-03` |
| 2024 | Mulverhill et al., *Evaluating the potential for continuous update of EFI attributes using optical satellite data* (Forestry) | Method | How to refresh EFI without a new LiDAR flight | `INV-01`, `DIS-03` |
| 2023 | Mulverhill et al., *Continuous monitoring and sub-annual change detection with HLS* (ISPRS 197, 309-319) | Method | Sub-annual change, not annual snapshots | `DIS-02` |
| 2025 | Brown et al., *Detection of non-stand-replacing disturbances using HLS* (ISPRS 220, 264-279) | Method | Partial mortality and stress become visible | `DIS-02`, `DIS-06` |
| 2026 | Mulverhill et al., *Characterizing changes in forest condition associated with NSR* (Remote Sensing Letters 17(9)) | Method | Condition, not just cover change | `DIS-02`, `DIS-03` |
| 2024 | Trotto et al., *Characterizing forest structural changes from bitemporal ALS* (Science of Remote Sensing 10, 100160) | Method | Structural evidence for NSR | `INV-08`, `DIS-02` |
| 2022 | White et al., *Mapping, validating, and interpreting post-disturbance recovery* (RSE 271, 112904) | Product + validation | Recovery is a trajectory, not a class | `DIS-04` |
| 2024 | Smith-Tripp et al., *Landsat assessment of variable spectral recovery linked to post-fire structure* (ISPRS 208, 121-135) | Method | Links spectral recovery to structure | `DIS-04` |
| 2024 | Smith-Tripp et al., *Early spectral dynamics are indicative of distinct growth patterns in post-wildfire forests* (RSE2) | Evidence | Early signal predicts later trajectory | `DIS-04` |
| 2025 | Smith-Tripp et al., *Post-fire structural recovery associated with climate extremes* (Landscape Ecology) | Evidence | Climate modulates recovery | `DIS-04`, `DIS-06` |
| 2022 | Keay et al., *Automated forest harvest detection with a normalized PlanetScope time series* (CJRS) | Method | Plan-versus-actual monitoring | `OPS-04` |

## Growth, climate, and mortality

The signal is a move from static yield tables to **climate-sensitive,
mortality-aware, mixed-species dynamics**. This is the largest gap between the
current FRESH engines and the science.

| Year | Work | Type | Why it matters | Candidates |
| ---: | --- | --- | --- | --- |
| 2022 | Chagnon et al., *Deciphering the black spruce response to climate variation* (FEM 520, 120375) | Evidence | A species-level climate response | `GRO-02` |
| 2023 | Chagnon et al., *Strong latitudinal gradient in temperature-growth coupling near the treeline* (Frontiers) | Evidence | Response is not stationary across latitude | `GRO-02` |
| 2023 | Wotherspoon et al., *Assessing future climate trends and implications for managed forests across Canadian ecozones* (CJFR) | Product | A consistent climate scenario base | `GRO-01`, `GRO-08` |
| 2024 | Fortin et al., *Climate-sensitive models of tree mortality based on lifetime analysis* (CJFR) | Model | A mortality transition, not just a growth modifier | `GRO-03` |
| 2026 | Johnson et al., *Modifying stand-level growth under a changing climate using a model fusion approach* (Forest Science) | Model | A principled blend of empirical and process evidence | `GRO-04` |
| 2023 | Morin-Bernard et al., *Predicting net growth rates in boreal forests using Landsat time series and PSP data* (Forestry) | Method | Links remote sensing to growth | `GRO-03`, `DIS-03` |
| 2024 | Morin-Bernard et al., *Integration of tree-ring data, Landsat, and ALS to quantify growth declines* (FEM 557, 121765) | Method | A validation and attribution path | `GRO-07` |
| 2025 | Leduc et al., *A review of dendrochronology and remote sensing integration* (Current Forestry Reports 11, 25) | Review | The evidence base for decline attribution | `GRO-07` |
| 2026 | de Liz et al., *Fine-scale drivers of sugar maple habitat suitability at its northern range limit* (Forestry 99(4)) | Evidence | Fine-scale suitability, not just climate envelopes | `GRO-08` |

## Risk, resilience, and habitat

The signal is that **resilience is becoming operational**: thinning effects,
pest dynamics, caribou forage, and landscape configuration are being quantified
in forms that can become modifiers or constraints.

| Year | Work | Type | Why it matters | Candidates |
| ---: | --- | --- | --- | --- |
| 2025 | Chagnon et al., *Potential of thinning to increase forest resilience and resistance: a meta-analysis* (FEM 590, 122788) | Evidence | A treatment effect that can become a modifier | `DIS-06`, `OPS-01` |
| 2025 | Trotto et al., *Spectral remote sensing reveals forest structural characteristics resilient to spruce budworm* (Ecological Indicators 181, 114382) | Evidence | Resilience is measurable | `DIS-07` |
| 2025 | Trotto et al., *Characterizing landscape configuration effects on spruce budworm dynamics* (Landscape Ecology 40, 183) | Evidence | Configuration matters, not just host abundance | `DIS-07`, `PLAN-03` |
| 2026 | Beaulieu et al., *Quantifying changes in annual lichen volume for woodland caribou* (IJAEOG 152, 105444) | Product | A forage layer for caribou planning | `BIO-05`, `PLAN-04` |
| 2026 | Moreau et al., *Forest management must shift from profit to prevention* (Communications Sustainability; doi:10.1038/s44458-026-00087-x) | Argument | The policy case for risk-aware planning | `PLAN-01`, `PLAN-02` |

## Carbon and wood

The signal is that carbon is a **product-and-disturbance accounting problem**,
not only a biomass-map problem. FRESH already has the product flows; it lacks
the boundaries and factors.

| Year | Work | Type | Why it matters | Candidates |
| ---: | --- | --- | --- | --- |
| 2024 | Tompalski et al., *Biomass yield curves from time-series remote sensing* (FEM 561, 121894) | Product | A curve family, not a one-off map | `GRO-06`, `CARB-01` |
| 2022 | Chagnon et al., *Broad-scale wood degradation dynamics in the face of climate change* (GCB Bioenergy 14(8), 941-958) | Evidence | Salvage value decays | `CARB-03`, `OPS-03` |
| 2026 | Liu et al., *Wildfire fuel-reduction biomass for remote energy* (Journal of Cleaner Production 549, 147892) | Evidence | Fuel treatment can produce a product | `OPS-02` |

## Data, software, and validation

The signal is that IRSS has a habit of shipping **open tools**, not only papers.
These are the cheapest integration wins because the algorithm already has a
reference implementation.

| Year | Work | Type | Why it matters | Candidates |
| ---: | --- | --- | --- | --- |
| 2023 | Goodbody et al., *sgsR* (Forestry) | Tool | Sampling design and validation | `INV-06` |
| 2022 | Miraglio & Coops, *SUREHYP: an open-source Python package for Hyperion preprocessing* (Sensors 22, 9205) | Tool | A pattern for open, reproducible preprocessing | `DEC-03` |
| 2022 | Laurin et al., *SnowWarp: an open science and open data tool for daily snow monitoring* (EMS 156, 105477) | Tool | A pattern for open data products | `BIO-04` (future water) |
| 2022 | Wotherspoon et al., *Climate Scenarios for Canadian Forests* (Silva21 report) | Product | A climate package, not a paper | `GRO-01` |
| 2026 | Silva21 Extension Note Vol 14, *Lessons learned from 5 years of Silva21 data management* | Practice | The data-management failure modes to avoid | `DEC-03`, `DEC-04` |
| 2026 | Silva21 data portal (Globus) | Infrastructure | Access is a dependency, not a given | `DEC-05` |

## What the signal does not say

- It does not say the published relationships transfer everywhere. Most are
  calibrated in specific hubs, BEC zones, or disturbance regimes.
- It does not say the data are open. The Silva21 portal is access-controlled;
  several LiDAR products are partner-owned.
- It does not say the methods are ready for production. A paper that reports a
  model is not a validated software component.
- It does not say the ecosystem should adopt every tool. The register rejects
  more than it queues.

## Selected older IRSS signals

The 2004-2023 publication list also contains foundational work that is not
cited in the table above but shapes the candidates:

- **LiDAR sampling for large-area forest characterization** and the
  **best-practices guide for ALS inventory attributes** — the methodological
  base for `INV-01` and `DEC-04`.
- **A forest structure habitat index based on ALS** and the **Dynamic Habitat
  Indices** — the base for `BIO-01` and `BIO-02`.
- **Three decades of forest structural dynamics over Canada** and
  **large-area mapping of cover, height, and biomass** — the base for
  `DIS-02` and `CARB-01`.
- **Road visibility and grizzly bear habitat selection** — the base for
  `PLAN-05` and `OPS-05`.
- **Predicting large wildfires from soil water balance** and **burn severity
  from dNBR/RdNBR** — the base for `DIS-05` and `DIS-06`.

These are listed on the IRSS publications page and are worth a deeper read
before any of the related candidates is accepted.

## 2026-11-03 review (P1.2)

- Extracted the 44 backticked candidate IDs from the signal tables and compared them with
  the registry. All 44 exist, and none was renamed or removed.
- Confirmed the supporting IRSS and Silva21 pages return HTTP 200. The inventory review in
  `notes/00-source-inventory.md` records the page counts.
- Left the signal classifications, paper list, and candidate mappings unchanged.
- Did not re-read the papers or resolve every DOI; the review checks identifiers and links,
  not the truth of each published claim. That limit stays explicit before any candidate is
  accepted.
