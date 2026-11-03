# Candidate register

_IRSS x Silva21 Expansion Mine for the FRESH forest modelling ecosystem_

Generated: 2026-10-25. Last audited: 2026-11-03. Candidates: 62. Scoring: `priority = (impact * readiness) / (effort_points * risk)`.

This file is generated from `registry/candidates.yaml`. Edit the registry, then run `python scripts/render_registry.py`.

## Top of the queue

| Rank | ID | Wave | Score | Effort | Impact | Readiness | Risk | Candidate |
| ---: | --- | ---: | ---: | --- | ---: | ---: | ---: | --- |
| 1 | `CARB-03` | 2 | 6.00 | S | 3 | 4 | 2 | Wood degradation and storage value loss |
| 2 | `CARB-01` | 1 | 5.00 | M | 5 | 4 | 2 | Carbon account v0 across ws3 and ws4 |
| 3 | `GRO-06` | 1 | 5.00 | M | 5 | 4 | 2 | Biomass yield curves from time-series remote sensing |
| 4 | `DATA-05` | 2 | 4.00 | M | 4 | 4 | 2 | Imputation and data fusion toolkit |
| 5 | `DEC-01` | 2 | 4.00 | M | 4 | 4 | 2 | Scenario explorer with climate and risk layers |
| 6 | `INV-09` | 2 | 4.00 | M | 4 | 4 | 2 | Road extraction and status from ALS |
| 7 | `OPS-01` | 2 | 4.00 | M | 4 | 4 | 2 | Commercial thinning prioritization from drone LiDAR |
| 8 | `DIS-09` | 2 | 3.00 | M | 4 | 3 | 2 | Salvage shelf-life and value-decay model |
| 9 | `OPS-03` | 2 | 3.00 | M | 4 | 3 | 2 | Salvage harvest scheduling with shelf-life |
| 10 | `PLAN-02` | 2 | 3.00 | M | 4 | 3 | 2 | Resilience-productivity trade-off portfolio |
| 11 | `DIS-05` | 3 | 3.00 | M | 4 | 3 | 2 | Burn severity and post-fire mortality inputs |
| 12 | `BIO-04` | 3 | 2.25 | M | 3 | 3 | 2 | Stream and riparian habitat metrics from ALS |
| 13 | `GRO-07` | 3 | 2.25 | M | 3 | 3 | 2 | Tree-ring, Landsat, and ALS integration for growth decline |
| 14 | `INV-08` | 3 | 2.25 | M | 3 | 3 | 2 | LiDAR structural change detection |
| 15 | `GRO-02` | 2 | 2.22 | L | 5 | 4 | 3 | Climate-adjusted yield curve modifiers |

## By workstream

### Biodiversity and habitat (`BIO`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `BIO-01` | 1 | 20.00 | S | `ws4`, `ws3` | Dynamic Habitat Indices as biodiversity layers | Ingest one DHI product and report its trajectory under two existing ws4 schedules. |
| `BIO-02` | 1 | 4.00 | M | `ws4` | Forest structure habitat index from ALS | Implement the published index on one ALS-covered landscape and compare with DHI. |
| `BIO-04` | 3 | 2.25 | M | `ws4`, `fhops` | Stream and riparian habitat metrics from ALS | Derive morphology metrics for one watershed on top of the existing stream candidates and compare with field or regional data. |
| `BIO-05` | 3 | 1.50 | M | `ws4` | Lichen volume and caribou forage | Ingest one lichen layer and report its trend under a harvest scenario. |
| `BIO-03` | 3 | 1.00 | L | `nemora`, `ws4` | Species distribution modelling pipeline | Prototype one SDM with open occurrence data and publish a reproducible example. |

### Carbon and biomass accounting (`CARB`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `CARB-04` | 0 | 1.00 | M | `femic` | Soil carbon and site-productivity layer | Ingest the layer as a read-only fragment attribute and defer dynamic modelling. |
| `CARB-01` | 1 | 5.00 | M | `ws3`, `ws4`, `femic` | Carbon account v0 across ws3 and ws4 | No new work. Track FEMIC P115 (#361) and ws4 P58 (#357) to closeout, and record the parity result and the account boundary in this register. |
| `CARB-03` | 2 | 6.00 | S | `fhops`, `ws4` | Wood degradation and storage value loss | Add a decay module shared by FHOPS salvage and ws4 carbon valuation. |
| `CARB-02` | 2 | 2.00 | M | `ws3`, `ws4` | Disturbance emissions and avoided emissions | Add a post-hoc emissions report for one fire scenario before changing the objective. |

### Data engineering, uncertainty, and synthetic forests (`DATA`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `DATA-01` | 1 | 12.50 | M | `nemora`, `femic` | Distribution fitting and uncertainty propagation for curves | Fit a distribution to one curve family and emit a 90% band into a ws4 report. |
| `DATA-02` | 1 | 8.00 | M | `nemora`, `ws4` | Synthetic forest and stand generator for tests and scenarios | Generate one synthetic landscape with known volume and run it through ws4 build and simulate. |
| `DATA-04` | 1 | 7.50 | M | `nemora`, `femic` | Open inventory ingest harmonization | Publish the shared schema and migrate one ingest path, keeping byte-level regression fixtures. |
| `DATA-05` | 2 | 4.00 | M | `nemora`, `femic` | Imputation and data fusion toolkit | Implement kNN imputation for one missing attribute and report out-of-sample error. |
| `DATA-03` | 2 | 2.00 | L | `nemora` | Measurement campaign simulation | Implement a plot-sampling simulator and reproduce a known inventory variance result. |
| `DATA-06` | 3 | 0.83 | L | `ws4` | Uncertainty-aware optimization | Run a small robust reformulation on an existing instance and compare the cost of robustness. |

### Decision support, provenance, and validation (`DEC`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `DEC-04` | 1 | 16.00 | S | `cross` | EFI model card and applicability metadata | Publish `efi.model.v1` with two model cards and validate them against FEMIC's existing bundle metadata. |
| `DEC-02` | 2 | 12.00 | S | `ws4` | Forest condition report cards | Design the report-card schema and generate one from a pilot dataset. |
| `DEC-03` | 2 | 8.00 | M | `cross` | Provenance and uncertainty communication | Add a provenance block and uncertainty band to one existing ws4 report. |
| `DEC-01` | 2 | 4.00 | M | `ws4`, `fhops` | Scenario explorer with climate and risk layers | Add one climate layer and one disturbance layer to the existing map, with provenance popovers. |
| `DEC-05` | 3 | 0.83 | L | `cross` | Silva21 hub validation network and data access | Identify two hubs with the most relevant data and draft a one-page validation protocol and data request. |

### Disturbance, risk, and recovery (`DIS`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `DIS-01` | 1 | 25.00 | S | `cross` | Shared disturbance event schema | Publish `disturbance.v1` with a JSON schema, examples, and a validator, then wire one consumer in ws4. |
| `DIS-02` | 2 | 4.00 | M | `femic`, `ws4` | NSR detection and attribution adapter | Run the published NSR workflow on one AOI and emit `disturbance.v1` records for ws4 consumption. |
| `DIS-04` | 2 | 3.75 | M | `femic`, `ws4` | Post-fire recovery and regeneration-failure layer | Ingest one published recovery/failure layer and add `regen_status` to a pilot FEMIC instance. |
| `DIS-09` | 2 | 3.00 | M | `fhops`, `ws4` | Salvage shelf-life and value-decay model | Add a `shelf_life` field and a linear or exponential value-decay term to the FHOPS salvage scenario. |
| `DIS-06` | 2 | 0.83 | L | `ws4`, `femic` | Hazard library for drought, pest, wind, and fire | Publish the interface and implement one hazard end-to-end as a reference implementation. |
| `DIS-05` | 3 | 3.00 | M | `femic`, `fhops` | Burn severity and post-fire mortality inputs | Build a severity-to-mortality lookup for one fire and attach it to FHOPS salvage blocks. |
| `DIS-03` | 3 | 2.00 | L | `ws4`, `femic` | Near-real-time forest condition and early alert | Define a report-card schema and prototype it for one Silva21 hub or TSA. |
| `DIS-08` | 3 | 1.50 | M | `ws4`, `fhops` | Bark beetle and mountain pine beetle hazard | Build a BC pilot that drives a beetle hazard layer into ws4 and a salvage prescription into FHOPS. |
| `DIS-07` | 3 | 1.00 | M | `ws4`, `femic` | Spruce budworm defoliation risk | Encode one published susceptibility relationship and test it on an eastern pilot landscape. |

### Growth, yield, climate response, and productivity (`GRO`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `GRO-01` | 1 | 25.00 | S | `cross` | Climate data contract and GCM ensemble | Publish `climate.v1` with a JSON schema, a small sample for one AOI, and a reader in FEMIC or Nemora. |
| `GRO-06` | 1 | 5.00 | M | `femic`, `ws4` | Biomass yield curves from time-series remote sensing | Add a biomass curve table and a carbon conversion report to one FEMIC instance. |
| `GRO-02` | 2 | 2.22 | L | `femic`, `ws4` | Climate-adjusted yield curve modifiers | Implement one published response function for one species/BEC and compare scenario output against the unmodified curve. |
| `GRO-03` | 2 | 2.22 | L | `femic`, `ws4` | Climate-sensitive mortality transitions | Implement a published mortality function as a transition and validate predicted losses against a held-out PSP set. |
| `GRO-05` | 2 | 1.50 | M | `femic` | Age-independent height-growth trajectories | Derive trajectories for a pilot and test whether they select a different curve family than the current age-based rule. |
| `GRO-07` | 3 | 2.25 | M | `femic`, `nemora` | Tree-ring, Landsat, and ALS integration for growth decline | Define a tree-ring series schema and test it on one Silva21 hub. |
| `GRO-08` | 3 | 1.67 | L | `femic`, `ws4` | Species suitability and assisted-migration layers | Ingest one published suitability layer for a pilot AOI and add it as a fragment attribute with provenance. |
| `GRO-04` | 3 | 0.67 | L | `femic`, `nemora` | Stand-level model fusion | Reimplement the published fusion method on one species and compare against each component model. |
| `GRO-09` | 3 | 0.40 | XL | `femic`, `nemora` | 3-PG process-model adapter | Write an adapter specification and run 3-PG on one existing FEMIC instance for comparison, without committing to integration. |

### Inventory, LiDAR, and enhanced forest inventory (`INV`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `INV-06` | 1 | 15.00 | S | `nemora`, `femic` | Structurally guided sampling with sgsR | Wrap or port the sgsR sampling workflow into `nemora.sampling` with a CLI and a small worked example. |
| `INV-04` | 1 | 4.00 | M | `femic` | Site index and potential height from ALS | Add an optional `si_als` field with provenance and backtest it against the current TSA 48 or K3Z SI assignment, using the ws4 P48/P49 ground-plot validation surfaces where they apply. |
| `INV-05` | 2 | 4.00 | M | `femic`, `ws4` | Species composition and mixedwood fraction layers | Define a species-fraction schema and ingest one public Canada-wide layer into a pilot FEMIC instance. |
| `INV-09` | 2 | 4.00 | M | `ws4`, `fhops` | Road extraction and status from ALS | Define `road.status` (segment_id, status, surface, passability, source, date) and import one ALS-derived centerline set into ws4. |
| `INV-01` | 2 | 3.33 | M | `femic`, `nemora` | ALS area-based inventory imputation contract | Define an `inventory.als` model-card table (fragment_id, attribute, value, model_id, rmse) and a reader that applies a fitted ABA model to one FEMIC LiDAR bundle; use the ws4 P48/P49 plot reconciliation as the validation lane. |
| `INV-08` | 3 | 2.25 | M | `femic`, `ws4` | LiDAR structural change detection | Run the polar change-vector method on one two-epoch pilot and compare with HLS NSR detections. |
| `INV-10` | 3 | 1.50 | M | `femic`, `ws4` | Genetic gain and seedlot performance from ALS | Reproduce a published breeding-value or gain estimate on one trial and compare it with the default TIPSY gain assumption. |
| `INV-03` | 3 | 1.33 | L | `femic`, `ws4` | Multi-temporal ALS harmonization and periodic annual increment | Run a two-epoch pilot in one TSA and compare height increment with VDYP/TIPSY predictions at the same locations. |
| `INV-07` | 3 | 1.00 | L | `femic`, `fhops` | Drone and mobile LiDAR pilot ingestion | Publish a minimal plot-product contract and test it on one existing Silva21 drone acquisition. |
| `INV-02` | 3 | 0.89 | L | `femic`, `nemora` | Tree-list and stem-distribution metrics from high-density LiDAR | Prototype a DBH-distribution export on one dense stand and compare predicted volume against the current TIPSY/VDYP curve. |

### Harvesting operations, thinning, and salvage (`OPS`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `OPS-01` | 2 | 4.00 | M | `fhops`, `femic` | Commercial thinning prioritization from drone LiDAR | Build a `thinning_priority` input table and a prescription generator for one pilot stand. |
| `OPS-03` | 2 | 3.00 | M | `fhops` | Salvage harvest scheduling with shelf-life | Build one end-to-end salvage example from a burned landscape and report value under two access scenarios. |
| `OPS-05` | 2 | 2.00 | M | `fhops`, `ws4` | Road access and status-aware scheduling | Define `road.status` and add an access constraint to one FHOPS scenario. |
| `OPS-04` | 3 | 1.50 | M | `fhops`, `femic` | Harvest detection and plan-versus-actual monitoring | Prototype a plan-versus-actual report for one operating area. |
| `OPS-02` | 3 | 1.33 | L | `fhops`, `ws4` | Fuel-reduction treatment and biomass recovery planning | Add a fuel-treatment scenario and a biomass product to FHOPS for one wildland- urban-interface pilot. |
| `OPS-06` | 3 | 0.67 | L | `fhops`, `femic` | Taper and product recovery from LiDAR and photogrammetry | Prototype taper curves for one species from a plot and compare the predicted product mix with the FHOPS default. |

### Landscape planning and resilience (`PLAN`)

| ID | Wave | Score | Effort | Targets | Candidate | First step |
| --- | ---: | ---: | --- | --- | --- | --- |
| `PLAN-06` | 0 | 0.67 | L | `ws4` | Deliberative-analytic and serious-game engagement | Write a concept note and user journey; do not build until the scenario engine and web UI are stable. |
| `PLAN-03` | 1 | 4.00 | M | `ws4` | Spatial resilience metrics for estate models | Implement three metrics as report accounts and compare two existing ws4 schedules. |
| `PLAN-07` | 2 | 6.00 | M | `ws4` | Scenario storytelling and visualisation | Design a one-page scenario storyboard template and generate it from an existing run. |
| `PLAN-08` | 2 | 6.00 | S | `ws4`, `fhops` | Market and policy shock scenarios | Add a `prices.v1` table and a small set of named price paths to one ws4/FHOPS scenario. |
| `PLAN-02` | 2 | 3.00 | M | `ws4` | Resilience-productivity trade-off portfolio | Define three archetype strategies (productivity, resilience, balanced) and run them through the existing portfolio search. |
| `PLAN-05` | 2 | 2.00 | M | `ws4` | Habitat connectivity account over the road and patch network | Implement a least-cost or circuit-style connectivity metric on one ws4 dataset and compare two road strategies. |
| `PLAN-01` | 2 | 1.67 | L | `ws4`, `ws3` | Risk-aware forest estate planning | Add a scenario-level expected-loss report before adding it to the objective, so the risk signal can be inspected without changing optimisation. |
| `PLAN-04` | 3 | 1.33 | L | `ws4` | Caribou habitat and dynamic mitigation | Ingest one lichen/habitat layer and add a habitat account before adding a constraint. |

## Candidate detail

### `BIO-01` — Dynamic Habitat Indices as biodiversity layers

- **Workstream:** Biodiversity and habitat
- **Status / wave:** complete / 1
- **FRESH targets:** `ws4`, `ws3`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** S / 4 / 5 / 1
- **Screening score:** 20.00

**What.** Ingest annual Dynamic Habitat Indices and expose them as landscape accounts or constraints in ws4/ws3.

**Gap.** There is no biodiversity layer or account; habitat is outside the estate model.

**First step.** Ingest one DHI product and report its trajectory under two existing ws4 schedules.

**Risks.** DHI is a coarse productivity surrogate; scale mismatch; not a species-specific habitat model.

**Resolution.** Implemented in UBC-FRESH/ws4#376, child of P54 (#375); PR #463 adds the DHI ingest, account, report block, and web layer.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/ws4#376 is closed, PR #463 is merged as `b0438de`, and parent P54 (#375) is closed. See notes/17-p2-contract-audit.md.

**Sources.**

- [IRSS biodiversity research and Dynamic Habitat Indices](https://irsslab.forestry.ubc.ca/research/biodiversity/)
- [Coops et al. DHI publications](https://irsslab.forestry.ubc.ca/publications/)

### `BIO-02` — Forest structure habitat index from ALS

- **Workstream:** Biodiversity and habitat
- **Status / wave:** complete / 1
- **FRESH targets:** `ws4`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Implement a structural habitat index from ALS metrics and report it as a stand- and landscape-level account.

**Gap.** Habitat is not linked to the structural attributes that forest management actually changes.

**First step.** Implement the published index on one ALS-covered landscape and compare with DHI.

**Risks.** Index validity; weight selection; structural metrics not available everywhere.

**Resolution.** Implemented in UBC-FRESH/ws4#377, child of P54 (#375); PR #471 adds the exact Coops et al. (2016) index, coverage diagnostics, accounts, report, and DHI comparison. The real TFL 6 point-cloud run is PR #484; it reports missing exact first-return metrics.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/ws4#377 is closed, PRs #471 and #484 are merged as `b4f7caa` and `84fb562`, and parent P54 (#375) is closed. See notes/17-p2-contract-audit.md.

**Sources.**

- [IRSS forest structure habitat index publications](https://irsslab.forestry.ubc.ca/publications/)
- [Silva21 OB 5b, Metrics for silvicultural prescription: composition and structure](https://www.silva21.com/projects/metrics-for-silvicultural-prescription%3A-composition-and-structure)

### `BIO-03` — Species distribution modelling pipeline

- **Workstream:** Biodiversity and habitat
- **Status / wave:** candidate / 3
- **FRESH targets:** `nemora`, `ws4`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** L / 3 / 3 / 3
- **Screening score:** 1.00

**What.** Add a lightweight SDM pipeline to Nemora that combines climate, terrain, and remotely sensed predictors for species and habitat suitability.

**Gap.** Species suitability is external and ad hoc; there is no reproducible SDM workflow in the ecosystem.

**First step.** Prototype one SDM with open occurrence data and publish a reproducible example.

**Risks.** Occurrence bias; extrapolation; overfitting; ecological interpretation.

**Sources.**

- [IRSS biodiversity and species distribution research](https://irsslab.forestry.ubc.ca/research/biodiversity/)
- [de Liz et al. 2026, Fine-scale sugar maple habitat suitability](https://doi.org/10.1093/forestry/cpag054)

### `BIO-04` — Stream and riparian habitat metrics from ALS

- **Workstream:** Biodiversity and habitat
- **Status / wave:** candidate / 3
- **FRESH targets:** `ws4`, `fhops`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 3 / 3 / 2
- **Screening score:** 2.25

**What.** Extend FEMIC's D8 stream-candidate layer with ALS-derived stream morphology and riparian metrics (bankfull width, depth, shade, valley confinement) for buffers, aquatic habitat, and operations constraints.

**Gap.** FEMIC has terrain-derived stream candidates, but they are a screening aid, not a morphology or habitat layer. ws4 and FHOPS still use coarse riparian buffers.

**First step.** Derive morphology metrics for one watershed on top of the existing stream candidates and compare with field or regional data.

**Risks.** Stream detection under canopy; bankfull width ambiguity; regulatory acceptance.

**Sources.**

- [Kuiper et al. 2022, Stream morphological features from ALS](https://doi.org/10.1016/j.rse.2022.112948)

### `BIO-05` — Lichen volume and caribou forage

- **Workstream:** Biodiversity and habitat
- **Status / wave:** candidate / 3
- **FRESH targets:** `ws4`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** M / 3 / 3 / 3
- **Screening score:** 1.50

**What.** Ingest a lichen-volume model and use it as a caribou forage layer in habitat accounts and scenario constraints.

**Gap.** Caribou habitat is binary or expert-delineated; forage quantity and trend are not represented.

**First step.** Ingest one lichen layer and report its trend under a harvest scenario.

**Risks.** Model uncertainty; scale; caribou-habitat causal links.

**Sources.**

- [Beaulieu et al. 2026, Annual lichen volume for woodland caribou](https://doi.org/10.1016/j.jag.2026.105444)

### `CARB-01` — Carbon account v0 across ws3 and ws4

- **Workstream:** Carbon and biomass accounting
- **Status / wave:** adopted / 1
- **FRESH targets:** `ws3`, `ws4`, `femic`
- **Integration:** validation
- **Effort / impact / readiness / risk:** M / 5 / 4 / 2
- **Screening score:** 5.00

**What.** Define a shared carbon-account contract and emit it from one ws4 scenario, reusing the CBM linkage and avoided-emissions examples that already exist in ws3. Version 0 may use existing volume curves with a declared basic-density and carbon-fraction conversion; the biomass curve family (`GRO-06`) is a later refinement.

**Gap.** At the time of the mine, ws3 had CBM linkage and notebook-level avoided-fire and avoided-harvest examples, but there was no shared carbon contract, no ws4 account, and no provenance-bearing conversion from FEMIC curves. This is now being addressed by FEMIC P115 and ws4 P58 (carried as P51); the candidate is retained as the adoption record.

**First step.** No new work. Track FEMIC P115 (#361) and ws4 P58 (#357) to closeout, and record the parity result and the account boundary in this register.

**Risks.** Boundary definition (stand vs product vs soil); double counting; false precision. ws3 and ws4 may disagree on product and decay boundaries. Volume-to-biomass conversion adds uncertainty until `GRO-06` lands.

**Resolution.** Adopted by UBC-FRESH/femic#361 (P115, forest carbon domain; PR #394, `30b1444`) and UBC-FRESH/ws4#357 (live phase P58, carbon accounting and carbon-aware planning; PR #408, `ddf4ed8`). The carried ws4 label P51 was stale: P51 is the release-candidate verification phase. Do not open a parallel carbon contract.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/femic#361 and UBC-FRESH/ws4#357 are closed and both cited pull requests are merged. See notes/17-p2-contract-audit.md.

**Sources.**

- [Tompalski et al. 2024, Biomass yield curves from time-series remote sensing](https://doi.org/10.1016/j.foreco.2024.121894)
- [IRSS carbon and forest dynamics research](https://irsslab.forestry.ubc.ca/research/carbon/)
- [ws3 libcbm linkage and avoided-fire/avoided-harvest examples](https://github.com/UBC-FRESH/ws3)
- [FEMIC Phase 109, log-grade value/cost accounts](https://github.com/UBC-FRESH/femic)

### `CARB-02` — Disturbance emissions and avoided emissions

- **Workstream:** Carbon and biomass accounting
- **Status / wave:** candidate / 2
- **FRESH targets:** `ws3`, `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** M / 4 / 3 / 3
- **Screening score:** 2.00

**What.** Extend the carbon account to fire, harvest, and decomposition emissions, and report avoided emissions from alternative management, reusing the ws3 avoided-fire and avoided-harvest decision-support examples.

**Gap.** ws3 has notebook-level avoided-emissions examples; there is no reusable account or contract, and disturbance emissions are absent from ws4.

**First step.** Add a post-hoc emissions report for one fire scenario before changing the objective.

**Risks.** Emission-factor uncertainty; system boundary; substitution assumptions.

**Sources.**

- [IRSS carbon dynamics and NTEMS](https://irsslab.forestry.ubc.ca/research/ntems-national-terrestrial-ecosystem-monitoring-system/)
- [Silva21 carbon and disturbance themes](https://www.silva21.com/projects)

### `CARB-03` — Wood degradation and storage value loss

- **Workstream:** Carbon and biomass accounting
- **Status / wave:** adopted / 2
- **FRESH targets:** `fhops`, `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** S / 3 / 4 / 2
- **Screening score:** 6.00

**What.** Encode species- and product-specific degradation curves for standing dead wood and roadside storage, and use them in salvage and inventory valuation.

**Gap.** Dead wood is valued as if it were green; storage and shelf-life are not part of the economics.

**First step.** Add a decay module shared by FHOPS salvage and ws4 carbon valuation.

**Risks.** Context dependence; limited species coverage; interaction with product grade.

**Resolution.** First bounded slice adopted in UBC-FRESH/fhops P44 (parent #380, child #381, PR #383, CI green, not merged on 2026-11-03). Adds the shared `salvage.decay.v1` contract, the published Prestemon & Holmes (2008) mixed-conifer fire-killed retention curve, the Barrette et al. (2015) product windows, and `fhops report salvage-shelf-life`. The curve is a US Pacific Northwest reference, not a BC-specific, species-specific, or roadside-storage operational curve. Storage-specific and species/product curves, grade/value loss, a ws4 consumer, and OPS-03 scheduling remain follow-on. See notes/19-carb03-salvage-decay.md.

**Sources.**

- [Chagnon et al. 2022, Broad-scale wood degradation dynamics](https://doi.org/10.1111/gcbb.12951)
- [Silva21 AD 4, Salvage harvesting](https://www.silva21.com/projects/salvage-harvesting-of-dead-trees)
- [Prestemon & Holmes 2008, Timber Salvage Economics](https://research.fs.usda.gov/download/treesearch/32962.pdf)
- [Barrette et al. 2015, Dynamics of dead tree degradation and shelf-life](https://doi.org/10.1093/forestry/cpv007)

### `CARB-04` — Soil carbon and site-productivity layer

- **Workstream:** Carbon and biomass accounting
- **Status / wave:** deferred / 0
- **FRESH targets:** `femic`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** M / 2 / 3 / 3
- **Screening score:** 1.00

**What.** Ingest soil organic carbon and clay maps as site descriptors for productivity and carbon modelling.

**Gap.** Soil carbon is not represented; site productivity relies on inventory and BEC.

**First step.** Ingest the layer as a read-only fragment attribute and defer dynamic modelling.

**Risks.** Map accuracy; scale mismatch; dynamic soil carbon is a research programme, not a quick integration.

**Sources.**

- [IRSS soil carbon mapping publications](https://irsslab.forestry.ubc.ca/publications/)

### `DATA-01` — Distribution fitting and uncertainty propagation for curves

- **Workstream:** Data engineering, uncertainty, and synthetic forests
- **Status / wave:** complete / 1
- **FRESH targets:** `nemora`, `femic`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 5 / 5 / 1
- **Screening score:** 12.50

**What.** Fit distributions to curve residuals and parameter uncertainty, then propagate them into ws4 scenarios as confidence bands or stochastic draws.

**Gap.** Curves are deterministic point estimates; reports imply a precision the underlying data do not support.

**First step.** Fit a distribution to one curve family and emit a 90% band into a ws4 report.

**Risks.** Residual dependence; mis-specified distributions; users ignoring bands.

**Resolution.** Created as UBC-FRESH/nemora#6, child of P5 (#7). Merged in UBC-FRESH/nemora#11 as `cbf504d`; band CSV and coverage check delivered.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/nemora#6 is closed and PR #11 is merged as `cbf504d`; parent P5 (#7) is closed. See notes/17-p2-contract-audit.md.

**Sources.**

- [Nemora fit and distributions modules](https://github.com/UBC-FRESH/nemora)
- [IRSS growth and yield uncertainty publications](https://irsslab.forestry.ubc.ca/publications/)

### `DATA-02` — Synthetic forest and stand generator for tests and scenarios

- **Workstream:** Data engineering, uncertainty, and synthetic forests
- **Status / wave:** complete / 1
- **FRESH targets:** `nemora`, `ws4`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 4 / 4 / 1
- **Screening score:** 8.00

**What.** Generate synthetic landscapes and stem populations with known attributes for testing ws4/FHOPS pipelines and exploring scenario extremes.

**Gap.** Test fixtures are small and hand-built; edge cases and scale are hard to exercise.

**First step.** Generate one synthetic landscape with known volume and run it through ws4 build and simulate.

**Risks.** Synthetic realism; false confidence; maintaining fixtures.

**Resolution.** Created as UBC-FRESH/nemora#8, child of P5 (#7). Merged in UBC-FRESH/nemora#13 as `d094c01`; deterministic WS4 synthetic fixture and local build/simulate smoke test.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/nemora#8 is closed, PR #13 is merged as `d094c01`, and parent P5 (#7) is closed. See notes/17-p2-contract-audit.md.

**Sources.**

- [Nemora synthesis module](https://github.com/UBC-FRESH/nemora)
- [IRSS LiDAR sampling and inventory research](https://irsslab.forestry.ubc.ca/research/lidar/)

### `DATA-03` — Measurement campaign simulation

- **Workstream:** Data engineering, uncertainty, and synthetic forests
- **Status / wave:** candidate / 2
- **FRESH targets:** `nemora`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** L / 4 / 3 / 2
- **Screening score:** 2.00

**What.** Simulate plot, LiDAR, and transect campaigns against synthetic forests with configurable error models to evaluate sampling designs and EFI accuracy.

**Gap.** There is no way to ask how much a sampling or LiDAR design would tell us before spending the money.

**First step.** Implement a plot-sampling simulator and reproduce a known inventory variance result.

**Risks.** Error-model realism; computational cost; validation against real campaigns.

**Sources.**

- [Nemora simulation plan](https://github.com/UBC-FRESH/nemora)
- [IRSS plot, LiDAR, and sampling methods](https://irsslab.forestry.ubc.ca/research/lidar/)

### `DATA-04` — Open inventory ingest harmonization

- **Workstream:** Data engineering, uncertainty, and synthetic forests
- **Status / wave:** complete / 1
- **FRESH targets:** `nemora`, `femic`
- **Integration:** packaging
- **Effort / impact / readiness / risk:** M / 3 / 5 / 1
- **Screening score:** 7.50

**What.** Converge inventory ingest adapters on a shared tidy schema so FEMIC and Nemora stop maintaining parallel parsers.

**Gap.** FAIB/FIA/HPS parsing exists in more than one place with different assumptions.

**First step.** Publish the shared schema and migrate one ingest path, keeping byte-level regression fixtures.

**Risks.** Upstream schema drift; licensing; breaking existing scripts.

**Resolution.** Created as UBC-FRESH/nemora#9, child of P5 (#7). Merged in UBC-FRESH/nemora#12 as `9e7ea9e`; `nemora.inventory.v1` schema and HPS migration.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/nemora#9 is closed, PR #12 is merged as `9e7ea9e`, and parent P5 (#7) is closed. See notes/17-p2-contract-audit.md.

**Sources.**

- [Nemora ingest modules (FAIB/FIA/HPS)](https://github.com/UBC-FRESH/nemora)
- [FEMIC data preparation](https://github.com/UBC-FRESH/femic)

### `DATA-05` — Imputation and data fusion toolkit

- **Workstream:** Data engineering, uncertainty, and synthetic forests
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `nemora`, `femic`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Add k-nearest-neighbour and model-based imputation with uncertainty for missing inventory attributes and multi-source fusion.

**Gap.** Missing attributes are filled by ad hoc rules; there is no uncertainty-aware imputation lane.

**First step.** Implement kNN imputation for one missing attribute and report out-of-sample error.

**Risks.** Donor bias; spatial autocorrelation; extrapolation.

**Sources.**

- [IRSS LiDAR imputation and GEDI publications](https://irsslab.forestry.ubc.ca/publications/)
- [Nemora fit and sampling modules](https://github.com/UBC-FRESH/nemora)

### `DATA-06` — Uncertainty-aware optimization

- **Workstream:** Data engineering, uncertainty, and synthetic forests
- **Status / wave:** candidate / 3
- **FRESH targets:** `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** L / 5 / 2 / 4
- **Screening score:** 0.83

**What.** Prototype robust or chance-constrained optimization so plans remain feasible under yield, price, and disturbance uncertainty.

**Gap.** ws4 assumes deterministic yields and prices; a plan that is optimal on the mean can be fragile.

**First step.** Run a small robust reformulation on an existing instance and compare the cost of robustness.

**Risks.** Solver tractability; scenario explosion; interpretation and adoption.

**Sources.**

- [ws4 optimization and Nemora uncertainty](https://github.com/UBC-FRESH/ws4)

### `DEC-01` — Scenario explorer with climate and risk layers

- **Workstream:** Decision support, provenance, and validation
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `ws4`, `fhops`
- **Integration:** ui
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Extend the ws4 web UI, and mirror the layer contract in the queued FHOPS P12 web surface, with climate, disturbance, carbon, and habitat layer toggles plus scenario comparison across those dimensions.

**Gap.** The ws4 and FHOPS web surfaces expose the models but not the environmental intelligence layers that make scenarios meaningful, and they are being built separately without a shared layer contract.

**First step.** Add one climate layer and one disturbance layer to the existing map, with provenance popovers.

**Risks.** Layer performance; visual clutter; stale data.

**Sources.**

- [ws4 web front end](https://github.com/UBC-FRESH/ws4)
- [Silva21 AN 8b, Landscape-level visualisations](https://www.silva21.com/projects/viability-of-climate-informed%2C-landscape-level-strategies)

### `DEC-02` — Forest condition report cards

- **Workstream:** Decision support, provenance, and validation
- **Status / wave:** complete / 2
- **FRESH targets:** `ws4`
- **Integration:** ui
- **Effort / impact / readiness / risk:** S / 3 / 4 / 1
- **Screening score:** 12.00

**What.** Produce a periodic, stand-level report card summarizing condition, trend, and alerts in a form managers can act on.

**Gap.** Monitoring outputs are maps or papers, not a recurring management product.

**First step.** Design the report-card schema and generate one from a pilot dataset.

**Risks.** Indicator interpretation; alert fatigue; liability.

**Resolution.** Complete. P90 added the `ws4.forest_condition.report.v1` schema and static pilot; P91 added the account-derived CLI; P92 added the read-only API; P93 added the Reports-tab view. All cards are review-required/advisory, not operational early warning.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/ws4#650, #655, #659, and #662 are closed; PRs #653, #657, #661, and #669 are merged as `6aecccb`, `a0f395a`, `4ce820c`, and `5cf5444`. See notes/22-p4-candidate-reconciliation.md.

**Sources.**

- [Silva21 OB 3b, Early alert system](https://www.silva21.com/projects/early-alert-system-for-forest-management)

### `DEC-03` — Provenance and uncertainty communication

- **Workstream:** Decision support, provenance, and validation
- **Status / wave:** complete / 2
- **FRESH targets:** `cross`
- **Integration:** ui
- **Effort / impact / readiness / risk:** M / 4 / 4 / 1
- **Screening score:** 8.00

**What.** Turn technical provenance into user-facing badges, source links, and uncertainty bands in reports and the web UI.

**Gap.** Provenance exists in manifests but is not legible to decision-makers.

**First step.** Add a provenance block and uncertainty band to one existing ws4 report.

**Risks.** Information overload; provenance gaps; false reassurance.

**Resolution.** Complete as UBC-FRESH/ws4 P108 (#734, PR #741, merge `00c0b6c`): the `ws4.report.provenance.v1` sidecar records report names, bytes, and SHA-256 digests, source metadata and hashes, run and dataset identity, and an explicit `not_stated` uncertainty status when inputs carry no uncertainty metadata. The reports API exposes the sidecar and recorded digests, and the Reports tab shows a provenance badge with links to the sidecar and source metadata. The earlier condition-card uncertainty column and provenance block landed in P100 (#670, PR #690, `d14f4ff`). Uncertainty bands beyond `not_stated` remain absent because the inputs do not state them.

**Sources.**

- [ws4 provenance phases P32/P35](https://github.com/UBC-FRESH/ws4)
- [Silva21 data management lessons (Extension Note Vol 14)](https://www.silva21.com/extensionnotes?lang=en)

### `DEC-04` — EFI model card and applicability metadata

- **Workstream:** Decision support, provenance, and validation
- **Status / wave:** complete / 1
- **FRESH targets:** `cross`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** S / 4 / 4 / 1
- **Screening score:** 16.00

**What.** Publish an EFI model-card schema (training data, predictors, accuracy, applicability domain, version) that travels with ALS-derived inventory attributes. It complements, rather than replaces, the existing `femic.lidar.product.v1` bundle manifest.

**Gap.** FEMIC's LiDAR bundle manifest describes the sensor product, not the inventory model. Two EFI layers can share a sensor specification but have different accuracy, training data, and applicability.

**First step.** Publish `efi.model.v1` with two model cards and validate them against FEMIC's existing bundle metadata.

**Risks.** Over-specific schema; adoption; vendor metadata gaps.

**Resolution.** Created as UBC-FRESH/femic#372, child of P116 (#369). Contract merged in UBC-FRESH/femic#380 as `f833ed9`; published model cards and the attribute annotation seam merged in UBC-FRESH/femic#418 as `69af694`. #372 is closed.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/femic#372 is closed and PRs #380 and #418 are merged. See notes/17-p2-contract-audit.md.

**Sources.**

- [IRSS LiDAR and EFI research](https://irsslab.forestry.ubc.ca/research/lidar/)
- [Goodbody et al. 2024, Integrating ALS into forest ecosystem management](https://doi.org/10.5558/tfc2024-014)
- [FEMIC LiDAR product bundle contract](https://github.com/UBC-FRESH/femic)

### `DEC-05` — Silva21 hub validation network and data access

- **Workstream:** Decision support, provenance, and validation
- **Status / wave:** candidate / 3
- **FRESH targets:** `cross`
- **Integration:** validation
- **Effort / impact / readiness / risk:** L / 5 / 2 / 4
- **Screening score:** 0.83

**What.** Establish data-sharing and validation agreements for a small set of Silva21 hubs so FRESH models can be tested against independent, long-term sites.

**Gap.** FRESH validation is concentrated in BC inventory and a few instances; there is no independent multi-hub benchmark.

**First step.** Identify two hubs with the most relevant data and draft a one-page validation protocol and data request.

**Risks.** Access restrictions; data harmonization; long lead time; partner priorities.

**Sources.**

- [Silva21 data portal](https://www.silva21.com/dataportal?lang=en)
- [Silva21 research sites and hubs](https://www.silva21.com/sitesderecherche?lang=en)

### `DIS-01` — Shared disturbance event schema

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** complete / 1
- **FRESH targets:** `cross`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** S / 5 / 5 / 1
- **Screening score:** 25.00

**What.** Define a cross-repo disturbance event record (type, year, severity, extent, attribution, confidence, source) that FEMIC, ws4, and FHOPS can all consume.

**Gap.** Disturbance is represented differently, or not at all, in each repo. There is no shared way to hand a fire, insect, drought, or partial-mortality event from data to model to operations.

**First step.** Publish `disturbance.v1` with a JSON schema, examples, and a validator, then wire one consumer in ws4.

**Risks.** Schema overreach; disagreement on severity scales; attribution uncertainty.

**Resolution.** Created as UBC-FRESH/femic#371, child of P116 (#369). Contract merged in UBC-FRESH/femic#379 as `ef4cff2`; ws4 consumer merged in UBC-FRESH/ws4#398 as `5ea4a05`.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/femic#371 is closed, femic PR #379 is merged as `ef4cff2`, and ws4 PR #398 is merged as `5ea4a05`. See notes/17-p2-contract-audit.md.

**Sources.**

- [IRSS disturbance and habitat change research](https://irsslab.forestry.ubc.ca/research/disturbance-habitat-change/)
- [Silva21 OB 5c, Non-stand-replacing disturbances](https://www.silva21.com/projects/identifying-and-assessing-the-impact-of-non-stand-replacing-disturbances-within-a-near--real-time-context)
- [Brown et al. 2025, Detection of non-stand replacing disturbances using HLS](https://doi.org/10.1016/j.isprsjprs.2024.12.014)

### `DIS-02` — NSR detection and attribution adapter

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** deferred / 2
- **FRESH targets:** `femic`, `ws4`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Convert HLS/NSR detections into shared disturbance events and attach them to fragments and stands for growth, risk, and silvicultural decisions.

**Gap.** FEMIC assumes stand-replacing harvest; partial mortality, defoliation, and drought stress are not represented in the estate model.

**First step.** Run the published NSR workflow on one AOI and emit `disturbance.v1` records for ws4 consumption.

**Risks.** Detection thresholds; attribution confusion; cloud and snow gaps.

**Resolution.** Implemented as the public UBC-FRESH/fresh-beast package (`0.1.0a1`) with an HLS -> NBR -> Rbeast BEAST -> `femic.disturbance.v1` path and FEMIC/WS4 consumer tests. A 2019 TSA 23 AOS Aspen Leaf Miner (`ID6`, Moderate) case-control test (31 positive / 47 control blocks) failed at the 0.5 threshold: sensitivity 25.8%, specificity 66.0%, precision 33.3%, and same-year 2019 detection 0/31. Operational use is therefore deferred; the package remains an exploratory overlay only. No objective, growth, constraint, or solver was changed.

**Sources.**

- [Brown et al. 2025, NSR detection with Harmonized Landsat-Sentinel-2](https://doi.org/10.1016/j.isprsjprs.2024.12.014)
- [Mulverhill et al. 2026, Forest condition and NSR in a continuous inventory context](https://doi.org/10.1080/2150704X.2026.2683130)
- [Trotto et al. 2024, Bitemporal ALS and NSR](https://doi.org/10.1016/j.srs.2024.100160)

### `DIS-03` — Near-real-time forest condition and early alert

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** deferred / 3
- **FRESH targets:** `ws4`, `femic`
- **Integration:** workflow
- **Effort / impact / readiness / risk:** L / 4 / 3 / 2
- **Screening score:** 2.00

**What.** Build a monitoring loop that compares current satellite condition against a baseline and emits periodic stand-level report cards and alerts.

**Gap.** The ecosystem can simulate futures but cannot ingest the current state of the forest or flag where it has diverged from the plan.

**First step.** Define a report-card schema and prototype it for one Silva21 hub or TSA.

**Risks.** Alert fatigue; baseline drift; operational trust; latency.

**Resolution.** Deferred. Static DHI/recovery and the failed NSR case-control test do not provide a defensible near-real-time alert; see notes/16-dis03-readiness.md.

**Sources.**

- [Silva21 OB 3b, Early alert system for forest management](https://www.silva21.com/projects/early-alert-system-for-forest-management)
- [Morin-Bernard et al. 2023, Predicting net growth rates with Landsat time series](https://doi.org/10.1093/forestry/cpad055)
- [Mulverhill et al. 2024, Continuous update of EFI attributes](https://doi.org/10.1093/forestry/cpae029)

### `DIS-04` — Post-fire recovery and regeneration-failure layer

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** complete / 2
- **FRESH targets:** `femic`, `ws4`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** M / 5 / 3 / 2
- **Screening score:** 3.75

**What.** Map post-fire recovery and regeneration failure, then encode regeneration status and failure risk as fragment attributes and scenario constraints.

**Gap.** Regeneration assumptions are static and optimistic; there is no way to prioritise remediation or adjust yield where regeneration has failed.

**First step.** Ingest one published recovery/failure layer and add `regen_status` to a pilot FEMIC instance.

**Risks.** Recovery metrics are not survival; time lags; species-specific interpretation.

**Resolution.** Implemented in ws4 (PRs #499, #502, #503, #509): the NTEMS fire recovery layer is applied to all 102,128 TSA23 blocks. 1,497 blocks are not recovered (21,948 ha), 58 slower (745 ha). Deferring the 491 not-recovered blocks in the 20-year schedule reduces volume 0.069% (5 years) or 0.093% (10 years); the effect is too small to justify a hard constraint. Spectral recovery is not survival; no objective change.

**Sources.**

- [Silva21 OB 1a, Regeneration after catastrophic disturbance](https://www.silva21.com/projects/regeneration-after-catastophic-disturbance)
- [Smith-Tripp et al. 2024, Landsat assessment of post-fire recovery](https://doi.org/10.1016/j.isprsjprs.2024.01.008)
- [Smith-Tripp et al. 2025, Post-fire structural recovery and climate extremes](https://doi.org/10.1007/s10980-025-02266-y)

### `DIS-05` — Burn severity and post-fire mortality inputs

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `fhops`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** M / 4 / 3 / 2
- **Screening score:** 3.00

**What.** Convert burn-severity and post-fire mortality products into fragment-level mortality fractions for salvage planning and regenerating-stand curves.

**Gap.** Salvage and regeneration assume a binary burned/unburned state, not a severity gradient with partial mortality.

**First step.** Build a severity-to-mortality lookup for one fire and attach it to FHOPS salvage blocks.

**Risks.** Severity index saturation; delayed mortality; species differences.

**Sources.**

- [IRSS fire and burn severity publications](https://irsslab.forestry.ubc.ca/publications/)
- [Smith-Tripp et al. 2024, Early spectral dynamics and post-fire growth](https://doi.org/10.1002/rse2.420)

### `DIS-06` — Hazard library for drought, pest, wind, and fire

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `ws4`, `femic`
- **Integration:** model
- **Effort / impact / readiness / risk:** L / 5 / 2 / 4
- **Screening score:** 0.83

**What.** Define a common hazard interface (probability, severity, duration, affected attributes) and implement an initial set of drought, insect, wind, and fire modifiers.

**Gap.** Risk is either absent or hard-coded; there is no registry of hazards that can be composed in a scenario.

**First step.** Publish the interface and implement one hazard end-to-end as a reference implementation.

**Risks.** Weak transferability of published functions; double-counting hazards; validation burden.

**Sources.**

- [Silva21 AD and AN themes: resilience and resistance](https://www.silva21.com/projects)
- [Chagnon et al. 2025, Thinning to increase resilience: a meta-analysis](https://doi.org/10.1016/j.foreco.2025.122788)
- [IRSS mountain pine beetle research](https://irsslab.forestry.ubc.ca/research/mountain-pine-beetle/)

### `DIS-07` — Spruce budworm defoliation risk

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** candidate / 3
- **FRESH targets:** `ws4`, `femic`
- **Integration:** model
- **Effort / impact / readiness / risk:** M / 3 / 2 / 3
- **Screening score:** 1.00

**What.** Implement a defoliation hazard modifier for eastern forests using published landscape and stand susceptibility relationships.

**Gap.** No defoliator hazard exists; eastern scenarios cannot represent budworm-driven growth loss or salvage.

**First step.** Encode one published susceptibility relationship and test it on an eastern pilot landscape.

**Risks.** Outbreak dynamics are spatially contagious; limited validation; model complexity.

**Sources.**

- [Trotto et al. 2025, Spectral remote sensing and spruce budworm resilience](https://doi.org/10.1016/j.ecolind.2025.114382)
- [Trotto et al. 2025, Landscape configuration and spruce budworm dynamics](https://doi.org/10.1007/s10980-025-02203-z)
- [Shields et al. 2025, Review of PlanetScope CubeSats for forest monitoring](https://doi.org/10.1016/j.srs.2025.100314)

### `DIS-08` — Bark beetle and mountain pine beetle hazard

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** candidate / 3
- **FRESH targets:** `ws4`, `fhops`
- **Integration:** model
- **Effort / impact / readiness / risk:** M / 3 / 3 / 3
- **Screening score:** 1.50

**What.** Implement a beetle hazard modifier and a salvage trigger for pine-leading stands, using stand vigour, climate, and landscape susceptibility.

**Gap.** Beetle mortality is not represented in scenario dynamics, and salvage planning is not linked to infestation risk.

**First step.** Build a BC pilot that drives a beetle hazard layer into ws4 and a salvage prescription into FHOPS.

**Risks.** Ephemeral outbreak dynamics; spatial spread; data recency.

**Sources.**

- [IRSS mountain pine beetle research](https://irsslab.forestry.ubc.ca/research/mountain-pine-beetle/)
- [IRSS bark beetle mortality publications](https://irsslab.forestry.ubc.ca/publications/)

### `DIS-09` — Salvage shelf-life and value-decay model

- **Workstream:** Disturbance, risk, and recovery
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `fhops`, `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** M / 4 / 3 / 2
- **Screening score:** 3.00

**What.** Add species- and product-specific shelf-life and value-decay curves so salvage scheduling trades urgency against access, cost, and product mix.

**Gap.** FHOPS has salvage-mode defaults but no time-dependent degradation or product value loss.

**First step.** Add a `shelf_life` field and a linear or exponential value-decay term to the FHOPS salvage scenario.

**Risks.** Decay rates are context-dependent; product downgrade rules; interaction with transport and mill demand.

**Sources.**

- [Silva21 AD 4, Salvage harvesting of dead trees](https://www.silva21.com/projects/salvage-harvesting-of-dead-trees)
- [Chagnon et al. 2022, Broad-scale wood degradation dynamics](https://doi.org/10.1111/gcbb.12951)

### `GRO-01` — Climate data contract and GCM ensemble

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** complete / 1
- **FRESH targets:** `cross`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** S / 5 / 5 / 1
- **Screening score:** 25.00

**What.** Define a canonical climate table (variable, year, scenario, GCM, value, source, downscaling method) and an adapter for ClimateNA/SilvR21 outputs.

**Gap.** Climate is used ad hoc, if at all; there is no provenance-bearing climate layer shared by FEMIC, ws4, and Nemora.

**First step.** Publish `climate.v1` with a JSON schema, a small sample for one AOI, and a reader in FEMIC or Nemora.

**Risks.** Scenario/GCM proliferation; licensing terms for ClimateNA; downscaling differences between providers.

**Resolution.** Created as UBC-FRESH/femic#370, child of P116 (#369). Merged in UBC-FRESH/femic#378 as `9e16be9`.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/femic#370 is closed and PR #378 is merged as `9e16be9`. See notes/17-p2-contract-audit.md.

**Sources.**

- [Silva21 climate data and SilvR21](https://www.silva21.com/climatedata?lang=en)
- [Wotherspoon et al. 2022, Climate Scenarios for Canadian Forests](https://www.silva21.com/climatedata?lang=en)
- [Wotherspoon et al. 2023, Future climate trends across Canadian ecozones](https://doi.org/10.1139/cjfr-2023-0058)

### `GRO-02` — Climate-adjusted yield curve modifiers

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `femic`, `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** L / 5 / 4 / 3
- **Screening score:** 2.22

**What.** Implement a modifier API that adjusts VDYP/TIPSY-style yield curves for climate covariates while preserving the original curve and recording the modifier version.

**Gap.** FEMIC curves are static; ws4 has no way to represent climate-driven productivity change inside a scenario.

**First step.** Implement one published response function for one species/BEC and compare scenario output against the unmodified curve.

**Risks.** Extrapolation beyond calibration range; double-counting site index and climate; weak evidence for some species.

**Sources.**

- [Silva21 AN 3a, Integration of climate drivers into growth modelling](https://www.silva21.com/projects/integration-of-climate-drivers-into-growth-modelling-(an3a))
- [Silva21 AN 3b, Integration of climate drivers into growth modelling](https://www.silva21.com/projects/integration-of-climate-drivers-into-growth-modelling-(an3b))
- [Wotherspoon et al. 2023, Future climate trends](https://doi.org/10.1139/cjfr-2023-0058)

### `GRO-03` — Climate-sensitive mortality transitions

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `femic`, `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** L / 5 / 4 / 3
- **Screening score:** 2.22

**What.** Add annual or periodic stand-level mortality probability as a model transition, driven by climate, age, density, and disturbance history.

**Gap.** FEMIC has no mortality transition; ws4 assumes scheduled harvest or natural stand development, not climate-driven loss.

**First step.** Implement a published mortality function as a transition and validate predicted losses against a held-out PSP set.

**Risks.** Rare-event calibration; confounding with disturbance; transferability across ecosystems.

**Sources.**

- [Fortin et al. 2024, Climate-sensitive models of tree mortality](https://doi.org/10.1139/cjfr-2024-0205)
- [Silva21 OB 7, Climate-sensitive growth modelling in Ontario](https://www.silva21.com/projects/climate-sensitive-growth-modelling-in-ontario)

### `GRO-04` — Stand-level model fusion

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `nemora`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** L / 4 / 2 / 4
- **Screening score:** 0.67

**What.** Prototype a fusion layer that combines empirical yield curves, process-model output, and remote-sensing growth evidence into a single stand-level projection with explicit weights.

**Gap.** The ecosystem has separate empirical and process lanes but no principled way to combine them or carry the disagreement forward.

**First step.** Reimplement the published fusion method on one species and compare against each component model.

**Risks.** Method complexity; correlated errors; unclear uncertainty propagation; new publication with limited replication.

**Sources.**

- [Johnson et al. 2026, Modifying stand-level growth under a changing climate using model fusion](https://doi.org/10.1007/s44391-025-00053-5)

### `GRO-05` — Age-independent height-growth trajectories

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** candidate / 2
- **FRESH targets:** `femic`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 3 / 3 / 3
- **Screening score:** 1.50

**What.** Use repeat ALS to estimate height-growth trajectories without relying on stand age, improving curve selection in mixedwood and uneven-aged stands.

**Gap.** FEMIC curve selection depends on age, which is unreliable in mixedwoods and partially harvested stands.

**First step.** Derive trajectories for a pilot and test whether they select a different curve family than the current age-based rule.

**Risks.** Short observation windows; disturbance contamination; limited species coverage.

**Sources.**

- [Riofrio et al. 2023, Age-independent height growth from multi-temporal ALS](https://doi.org/10.1016/j.foreco.2023.121137)

### `GRO-06` — Biomass yield curves from time-series remote sensing

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** queued / 1
- **FRESH targets:** `femic`, `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** M / 5 / 4 / 2
- **Screening score:** 5.00

**What.** Add biomass and carbon curve families derived from Landsat time series and lidar plots, alongside the existing volume curves.

**Gap.** FEMIC produces volume curves, not biomass or carbon; carbon reporting therefore requires an external conversion with no provenance.

**First step.** Add a biomass curve table and a carbon conversion report to one FEMIC instance.

**Risks.** Species-specific allometry; belowground omission; curve vintage.

**Resolution.** Open. Tracked as UBC-FRESH/femic#376, child of P117 (#374). P3.2 wrote the reviewed handoff body; creating or updating the target issue waits for separate maintainer approval.

**Provenance.** P3 selected this candidate as the first model-integration handoff after the 2026-11-03 re-score. Live target confirmed: UBC-FRESH/femic P117 (#374, active) and P117.2 (#376, open), branch `feature/p117-efi-attributes` at `67cba53`. No implementation exists and no target issue was created or edited by P3. Handoff: handoffs/femic-child-biomass-curves-p3.md.

**Owner.** UBC-FRESH/femic P117 (#374); no individual GitHub assignee is recorded on the live issue.

**Unresolved dependency.** Parent P117 (#374) and child #376 remain open. The candidate still needs a published biomass curve selection and a declared carbon-fraction boundary before integration; P117.1 is still active on the shared phase branch.

**Sources.**

- [Tompalski et al. 2024, Developing aboveground biomass yield curves from time-series remote sensing](https://doi.org/10.1016/j.foreco.2024.121894)
- [IRSS carbon and biomass publications](https://irsslab.forestry.ubc.ca/research/carbon/)

### `GRO-07` — Tree-ring, Landsat, and ALS integration for growth decline

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `nemora`
- **Integration:** validation
- **Effort / impact / readiness / risk:** M / 3 / 3 / 2
- **Screening score:** 2.25

**What.** Build a validation and attribution layer that links tree-ring series to Landsat and ALS signals, so growth declines can be diagnosed rather than assumed.

**Gap.** There is no field-based validation path for climate-growth modifiers or remotely sensed decline.

**First step.** Define a tree-ring series schema and test it on one Silva21 hub.

**Risks.** Data access and sample size; dating errors; spatial mismatch.

**Sources.**

- [Morin-Bernard et al. 2024, Tree-ring, Landsat, and ALS integration for growth declines](https://doi.org/10.1016/j.foreco.2024.121765)
- [Leduc et al. 2025, Review of dendrochronology and remote sensing integration](https://doi.org/10.1007/s40725-025-00260-w)

### `GRO-08` — Species suitability and assisted-migration layers

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** shortlisted / 3
- **FRESH targets:** `femic`, `ws4`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** L / 5 / 3 / 3
- **Screening score:** 1.67

**What.** Produce climate-informed species and provenance suitability layers that can guide regeneration assumptions, seed transfer, and land-allocation scenarios.

**Gap.** FEMIC assumes current species suitability; ws4 has no assisted-migration or seed-transfer decision surface.

**First step.** Ingest one published suitability layer for a pilot AOI and add it as a fragment attribute with provenance.

**Risks.** SDM extrapolation; provenance data gaps; policy and liability sensitivity.

**Sources.**

- [Silva21 AN 1b, Future climate envelopes](https://www.silva21.com/projects/future-climate-envelopes)
- [Silva21 AN 5, Targeted assisted migration](https://www.silva21.com/projects/targeted-assisted-migration)
- [de Liz et al. 2026, Fine-scale drivers of sugar maple habitat suitability](https://doi.org/10.1093/forestry/cpag054)

### `GRO-09` — 3-PG process-model adapter

- **Workstream:** Growth, yield, climate response, and productivity
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `nemora`
- **Integration:** model
- **Effort / impact / readiness / risk:** XL / 4 / 2 / 4
- **Screening score:** 0.40

**What.** Evaluate and adapt a 3-PG implementation as an alternative or complementary growth engine for climate scenarios and productivity mapping.

**Gap.** The ecosystem is empirical (VDYP/TIPSY) with no process-based option for novel climates or species.

**First step.** Write an adapter specification and run 3-PG on one existing FEMIC instance for comparison, without committing to integration.

**Risks.** Parameter uncertainty; calibration burden; implementation fragmentation across R/Python/Excel versions.

**Sources.**

- [IRSS research overview: 3-PG development and maintenance](https://irsslab.forestry.ubc.ca/research/)
- [IRSS 3-PG publications](https://irsslab.forestry.ubc.ca/publications/)

### `INV-01` — ALS area-based inventory imputation contract

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** complete / 2
- **FRESH targets:** `femic`, `nemora`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** M / 5 / 4 / 3
- **Screening score:** 3.33

**What.** Turn FEMIC's existing LiDAR product bundle (CHM, canopy structure, tree products) into area-based inventory attributes (height, volume, basal area, density, species fractions, canopy cover) with model metadata and per-attribute uncertainty.

**Gap.** FEMIC owns the open LiDAR source, materialization, terrain, canopy, tree, and bundle pipeline, but it stops at canopy and tree products. It does not fit or apply area-based models for inventory attributes, and it does not carry per-attribute error into curve selection.

**First step.** Define an `inventory.als` model-card table (fragment_id, attribute, value, model_id, rmse) and a reader that applies a fitted ABA model to one FEMIC LiDAR bundle; use the ws4 P48/P49 plot reconciliation as the validation lane.

**Risks.** Model transferability across BEC zones and acquisition conditions; ALS data licensing; double-counting when conventional inventory is also present.

**Resolution.** Completed through UBC-FRESH/femic P120-P122: inventory.als contract, published BA-only pilot (2,942,755 rows/pixels, 14.9% TSA coverage), strict BA RMSE 8.86 m2/ha, 36 in-range plots. Height failed independent validation; volume remains research-only. See notes/reports/inv01-tsa23-ba-pilot-release.md and .acceptance.md.

**Sources.**

- [IRSS LiDAR research theme](https://irsslab.forestry.ubc.ca/research/lidar/)
- [Coops et al. 2021, Modelling lidar-derived estimates of forest attributes over space and time](https://doi.org/10.1016/j.rse.2021.112477)
- [Silva21 OB 4a, LiDAR EFI for growth projections](https://www.silva21.com/projects/lidar-efi-for-growth-projections%3A-new-approaches)

### `INV-02` — Tree-list and stem-distribution metrics from high-density LiDAR

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `nemora`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** L / 4 / 2 / 3
- **Screening score:** 0.89

**What.** Derive DBH distributions, stem maps, and competition metrics from high-density drone or mobile LiDAR for input to tree-list models and complex mixedwood stands.

**Gap.** FEMIC curves are stand-level; there is no tree-list lane and no way to represent complex, multi-cohort structure in the estate model.

**First step.** Prototype a DBH-distribution export on one dense stand and compare predicted volume against the current TIPSY/VDYP curve.

**Risks.** QSM accuracy in dense canopies; species attribution; small sample of operational acquisitions.

**Sources.**

- [Silva21 OB 4b, LiDAR stem metrics for tree-list models](https://www.silva21.com/projects/lidar-stem-metrics-for-tree-list-models)
- [Irwin et al. 2024, Prioritizing commercial thinning with high-density drone laser scanning](https://doi.org/10.1093/forestry/cpae030)
- [Qi et al. 2022, Comparing tree attributes from quantitative structure models](https://doi.org/10.1016/j.isprsjprs.2022.07.021)

### `INV-03` — Multi-temporal ALS harmonization and periodic annual increment

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `ws4`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** L / 4 / 3 / 3
- **Screening score:** 1.33

**What.** Harmonize repeat ALS acquisitions and derive height and structure increments as an independent check on yield curves and a calibration source for growth models.

**Gap.** FEMIC curves are calibrated to provincial PSPs and TIPSY/VDYP; repeat-LiDAR evidence is not part of the curve validation loop.

**First step.** Run a two-epoch pilot in one TSA and compare height increment with VDYP/TIPSY predictions at the same locations.

**Risks.** Registration and timing differences between flights; phenology; changes in acquisition specifications.

**Sources.**

- [Riofrio et al. 2022, Harmonizing multi-temporal ALS to derive periodic annual height increments](https://doi.org/10.1139/cjfr-2022-0055)
- [Riofrio et al. 2023, Modelling height growth with multi-temporal ALS](https://doi.org/10.1016/j.foreco.2023.121137)

### `INV-04` — Site index and potential height from ALS

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** rejected / 1
- **FRESH targets:** `femic`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Produce a spatially explicit site-index or potential-height layer from ALS and use it to select or adjust FEMIC yield curves at fragment resolution.

**Gap.** Site index is carried at AU/stratum resolution and is often inherited from inventory; ALS offers a repeatable, wall-to-wall alternative.

**First step.** Add an optional `si_als` field with provenance and backtest it against the current TSA 48 or K3Z SI assignment, using the ws4 P48/P49 ground-plot validation surfaces where they apply.

**Risks.** Species-specific SI equations; young-stand height not equal to site height; overfitting to one BEC zone.

**Resolution.** Rejected as a modelling task. British Columbia already has full SI coverage through VRI polygons, VDYP outputs, and SIBEC BEC/site-series estimates. Deriving a new general ALS SI model is remote-sensing research, not software integration. The generic `femic.efi.application` engine remains available for an existing model card; no SI model work is queued. Origin: synthesized from two plantation-specific IRSS papers, not an IRSS/Silva21 project deliverable.

**Sources.**

- [Tompalski et al. 2022, Modeling site index of selected poplar clones using ALS](https://doi.org/10.1139/cjfr-2021-0257)
- [Gavilan-Acuna et al. 2022, Estimating potential tree height in Pinus radiata plantations using ALS](https://doi.org/10.1139/cjfr-2022-0121)
- [IRSS growth and productivity publications](https://irsslab.forestry.ubc.ca/publications/)

### `INV-05` — Species composition and mixedwood fraction layers

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** complete / 2
- **FRESH targets:** `femic`, `ws4`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Consume national or regional species-composition layers and store species fractions as fragment attributes that can drive curve selection and product eligibility.

**Gap.** FEMIC uses coarse species/AU labels; mixedwood composition is poorly represented and cannot flow into product or habitat accounts.

**First step.** Define a species-fraction schema and ingest one public Canada-wide layer into a pilot FEMIC instance.

**Risks.** Class confusion in mixedwoods; temporal mismatch with the inventory vintage; species labels not aligned with TIPSY/VDYP species codes.

**Resolution.** Implemented in UBC-FRESH/ws4 PRs #490 and #492. The NTEMS 2022 dominant layer and VRI species percentages are ingested into separate composition and fraction contracts. TFL 6 leading species agree on 4/6 comparable blocks; all six labelled VRI blocks are mixed (non-leading fraction 0.40-0.60). A dominant-species product cannot supply the mixedwood fraction, so VRI/ALS is the fraction source.

**Sources.**

- [Hermosilla et al. 2022, Mapping tree species in Canada's forested ecosystems](https://doi.org/10.1016/j.rse.2022.113276)
- [Queinnec et al. 2023, Mapping dominant boreal tree species groups with ALS and Sentinel-2](https://doi.org/10.1080/07038992.2022.2130742)

### `INV-06` — Structurally guided sampling with sgsR

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** complete / 1
- **FRESH targets:** `nemora`, `femic`
- **Integration:** packaging
- **Effort / impact / readiness / risk:** S / 3 / 5 / 1
- **Screening score:** 15.00

**What.** Add structurally guided sampling design and validation to Nemora/FEMIC so inventory plots and LiDAR calibration are allocated against structure rather than a uniform grid.

**Gap.** Sampling design and inventory QA are ad hoc; there is no shared tool for allocating plots or testing whether an ALS model covers the structural range.

**First step.** Wrap or port the sgsR sampling workflow into `nemora.sampling` with a CLI and a small worked example.

**Risks.** R/Python bridge maintenance; licensing of the original implementation; user confusion between sampling design and model validation.

**Resolution.** Created as UBC-FRESH/nemora#10, child of P5 (#7). Merged in UBC-FRESH/nemora#14 as `2e8776c`; the optional sgsR R bridge and worked example are in the Nemora sampling surface.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/nemora#10 is closed, PR #14 is merged as `2e8776c`, and parent P5 (#7) is closed. See notes/17-p2-contract-audit.md.

**Sources.**

- [Goodbody et al. 2023, sgsR: a structurally guided sampling toolbox](https://doi.org/10.1093/forestry/cpac055)
- [Silva21 OB 5a, Continuous forest inventory framework](https://www.silva21.com/projects/continuous-forest-inventory-framework)

### `INV-07` — Drone and mobile LiDAR pilot ingestion

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `fhops`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** L / 3 / 3 / 3
- **Screening score:** 1.00

**What.** Define a plot-level point-cloud product and ingest drone/mobile LiDAR or photogrammetry for regeneration, thinning, and tree-health assessments.

**Gap.** There is no sub-stand data path for treatment prescriptions; FEMIC and FHOPS operate at stand or block resolution.

**First step.** Publish a minimal plot-product contract and test it on one existing Silva21 drone acquisition.

**Risks.** Data volume and processing cost; regulatory constraints; proprietary formats; unclear operational cadence.

**Sources.**

- [Silva21 OB 2, Advanced RS from free-to-grow to thinning](https://www.silva21.com/projects/advanced-rs%3A-free-to-grow-to-thinning-stage)
- [Silva21 OB 6, New technologies for measurements within stands](https://www.silva21.com/projects/new-technologies-for-measurements-within-stands)
- [Olson et al. 2025, Drone-based intra-canopy photogrammetry](https://doi.org/10.1016/j.compag.2025.110200)

### `INV-08` — LiDAR structural change detection

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `ws4`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 3 / 3 / 2
- **Screening score:** 2.25

**What.** Detect structural change between LiDAR epochs and emit change polygons with magnitude and direction, complementing optical change detection.

**Gap.** Change detection in the ecosystem is optical and land-cover oriented; structural degradation and partial mortality are invisible.

**First step.** Run the polar change-vector method on one two-epoch pilot and compare with HLS NSR detections.

**Risks.** False positives from acquisition differences; sparse repeat coverage; method maturity.

**Sources.**

- [Marinelli et al. 2022, Forest change detection in LiDAR using polar change vector analysis](https://doi.org/10.1109/LGRS.2020.3022282)
- [Trotto et al. 2024, Bitemporal ALS and non-stand-replacing disturbance](https://doi.org/10.1016/j.srs.2024.100160)

### `INV-09` — Road extraction and status from ALS

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `ws4`, `fhops`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Derive or refresh road centerlines, surface condition, and access status from ALS, and feed a shared road-status layer to ws4 and FHOPS.

**Gap.** ws4 builds and costs roads from a supplied network; FHOPS assumes access. Neither ingests remotely sensed road condition.

**First step.** Define `road.status` (segment_id, status, surface, passability, source, date) and import one ALS-derived centerline set into ws4.

**Risks.** Centerline attribution errors; status classification ambiguity; integration with existing road-network topology.

**Sources.**

- [Roussel et al. 2022, Correction and enhancement of forestry road maps using ALS](https://doi.org/10.1016/j.jag.2022.103020)
- [IRSS road and access publications](https://irsslab.forestry.ubc.ca/publications/)

### `INV-10` — Genetic gain and seedlot performance from ALS

- **Workstream:** Inventory, LiDAR, and enhanced forest inventory
- **Status / wave:** candidate / 3
- **FRESH targets:** `femic`, `ws4`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 3 / 3 / 3
- **Screening score:** 1.50

**What.** Estimate realized genetic gain and seedlot performance from ALS height and crown metrics in realized-gain trials, and use it to adjust plantation yield assumptions.

**Gap.** FEMIC and TIPSY plantation curves assume a generic genetic gain; there is no link from a seedlot or trial to the curve, and no provenance for the assumption.

**First step.** Reproduce a published breeding-value or gain estimate on one trial and compare it with the default TIPSY gain assumption.

**Risks.** Trial representativeness; genotype-by-environment interaction; small sample; proprietary seedlot data.

**Sources.**

- [du Toit et al. 2022, Generating Douglas-fir breeding value estimates using ALS](https://doi.org/10.3389/fpls.2022.893017)
- [du Toit et al. 2021, Internal crown geometric features from ALS in a realized-gain trial](https://doi.org/10.1093/forestry/cpaa046)
- [IRSS tree improvement and realized-gain publications](https://irsslab.forestry.ubc.ca/publications/)

### `OPS-01` — Commercial thinning prioritization from drone LiDAR

- **Workstream:** Harvesting operations, thinning, and salvage
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `fhops`, `femic`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Generate thinning priority and prescription inputs from drone LiDAR (competition, height, density) and feed them to FHOPS treatment scheduling and FEMIC's existing CT diameter-response lane.

**Gap.** FHOPS schedules treatments from block-level assumptions; FEMIC P109 models CT diameter response at AU/bucket level; neither sees within-stand competition or can prioritize where thinning will pay.

**First step.** Build a `thinning_priority` input table and a prescription generator for one pilot stand.

**Risks.** Drone coverage cost; prescription rules vary by jurisdiction; treatment response uncertainty.

**Sources.**

- [Irwin et al. 2024, Prioritizing commercial thinning with high-density drone laser scanning](https://doi.org/10.1093/forestry/cpae030)
- [Irwin et al. 2026, Framework for commercial thinning assessment](https://doi.org/10.1016/j.foreco.2026.124029)
- [Silva21 OB 2, Advanced RS from free-to-grow to thinning](https://www.silva21.com/projects/advanced-rs%3A-free-to-grow-to-thinning-stage)
- [FEMIC Phase 109, CT diameter response and log-grade value/cost accounts](https://github.com/UBC-FRESH/femic)

### `OPS-02` — Fuel-reduction treatment and biomass recovery planning

- **Workstream:** Harvesting operations, thinning, and salvage
- **Status / wave:** candidate / 3
- **FRESH targets:** `fhops`, `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** L / 4 / 3 / 3
- **Screening score:** 1.33

**What.** Plan fuel-reduction treatments and route the resulting biomass to energy or fiber products, with cost and carbon accounting.

**Gap.** Fuel treatment is outside FHOPS; biomass recovery and utilization are not linked to treatment scheduling.

**First step.** Add a fuel-treatment scenario and a biomass product to FHOPS for one wildland- urban-interface pilot.

**Risks.** Fuel-model uncertainty; biomass market thinness; treatment effectiveness.

**Sources.**

- [Arkin et al. 2021, Vertical fuel layers in tree crowns from high-density LiDAR](https://doi.org/10.3390/rs13224598)
- [Liu et al. 2026, Wildfire fuel-reduction biomass for remote energy](https://doi.org/10.1016/j.jclepro.2026.147892)

### `OPS-03` — Salvage harvest scheduling with shelf-life

- **Workstream:** Harvesting operations, thinning, and salvage
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `fhops`
- **Integration:** workflow
- **Effort / impact / readiness / risk:** M / 4 / 3 / 2
- **Screening score:** 3.00

**What.** Add a salvage scenario template that schedules dead-wood harvest under access, decay, product-mix, and mill-demand constraints.

**Gap.** Salvage is a mode, not a planning workflow with urgency and value decay.

**First step.** Build one end-to-end salvage example from a burned landscape and report value under two access scenarios.

**Risks.** Data on dead-wood quality; safety and regulatory constraints; market capacity.

**Sources.**

- [Silva21 AD 4, Salvage harvesting of dead trees](https://www.silva21.com/projects/salvage-harvesting-of-dead-trees)
- [Chagnon et al. 2022, Broad-scale wood degradation](https://doi.org/10.1111/gcbb.12951)

### `OPS-04` — Harvest detection and plan-versus-actual monitoring

- **Workstream:** Harvesting operations, thinning, and salvage
- **Status / wave:** candidate / 3
- **FRESH targets:** `fhops`, `femic`
- **Integration:** workflow
- **Effort / impact / readiness / risk:** M / 3 / 3 / 3
- **Screening score:** 1.50

**What.** Import remotely sensed harvest polygons and compare them with FHOPS plans and FEMIC harvest history to close the plan-actual loop.

**Gap.** There is no feedback from what was actually harvested to the next planning cycle.

**First step.** Prototype a plan-versus-actual report for one operating area.

**Risks.** Detection timing; partial harvests; attribution to operators.

**Sources.**

- [Keay et al. 2022, Automated forest harvest detection with PlanetScope](https://doi.org/10.1080/07038992.2022.2154598)
- [IRSS harvest and change detection publications](https://irsslab.forestry.ubc.ca/publications/)

### `OPS-05` — Road access and status-aware scheduling

- **Workstream:** Harvesting operations, thinning, and salvage
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `fhops`, `ws4`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** M / 4 / 2 / 2
- **Screening score:** 2.00

**What.** Use a shared road-status layer to constrain FHOPS access and align operational scheduling with ws4 road construction and maintenance.

**Gap.** FHOPS assumes blocks are accessible; ws4 builds roads but does not hand a time-varying access status to operations.

**First step.** Define `road.status` and add an access constraint to one FHOPS scenario.

**Risks.** Status data freshness; topology mismatch; maintenance cost assumptions.

**Sources.**

- [Roussel et al. 2022, Forestry road maps from ALS](https://doi.org/10.1016/j.jag.2022.103020)
- [ws4 road network and access accounts](https://github.com/UBC-FRESH/ws4)

### `OPS-06` — Taper and product recovery from LiDAR and photogrammetry

- **Workstream:** Harvesting operations, thinning, and salvage
- **Status / wave:** candidate / 3
- **FRESH targets:** `fhops`, `femic`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** L / 3 / 2 / 3
- **Screening score:** 0.67

**What.** Build on FEMIC P109's log-grade value/cost accounts and add taper and product-recovery inputs from terrestrial or drone point clouds and quantitative structure models, then feed FHOPS product mix and value assumptions.

**Gap.** FEMIC P109 exports log grades and value from BTC, but taper and within-block variation are not measured. FHOPS product mix still uses block-level average stem size and recovery assumptions.

**First step.** Prototype taper curves for one species from a plot and compare the predicted product mix with the FHOPS default.

**Risks.** QSM accuracy; mill-specific recovery; small sample; species coverage.

**Sources.**

- [Qi et al. 2022, Tree attributes from quantitative structure models](https://doi.org/10.1016/j.isprsjprs.2022.07.021)
- [IRSS taper, tree volume, and terrestrial photogrammetry publications](https://irsslab.forestry.ubc.ca/publications/)
- [FEMIC Phase 109, log-grade value/cost accounts and CT diameter response](https://github.com/UBC-FRESH/femic)

### `PLAN-01` — Risk-aware forest estate planning

- **Workstream:** Landscape planning and resilience
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `ws4`, `ws3`
- **Integration:** model
- **Effort / impact / readiness / risk:** L / 5 / 3 / 3
- **Screening score:** 1.67

**What.** Add expected-loss and risk-exposure terms to ws4's objective and constraints so plans can trade productivity against disturbance risk.

**Gap.** ws4 optimises volume and spatial rules; it does not penalise plans that concentrate risk or fail under a hazard scenario.

**First step.** Add a scenario-level expected-loss report before adding it to the objective, so the risk signal can be inspected without changing optimisation.

**Risks.** Risk model credibility; objective scaling; unintended risk-seeking behaviour.

**Sources.**

- [Silva21 AN 8a, Forest management plans for resilient landscapes](https://www.silva21.com/projects/forest-management-plans-for-resilient-landscapes)
- [Silva21 AN 8b, Viability of climate-informed landscape strategies](https://www.silva21.com/projects/viability-of-climate-informed%2C-landscape-level-strategies)
- [ws4 Phase 15/16 spatial and fire-related work](https://github.com/UBC-FRESH/ws4)

### `PLAN-02` — Resilience-productivity trade-off portfolio

- **Workstream:** Landscape planning and resilience
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `ws4`
- **Integration:** workflow
- **Effort / impact / readiness / risk:** M / 4 / 3 / 2
- **Screening score:** 3.00

**What.** Generate and compare a portfolio of management strategies along a resilience- productivity frontier rather than a single optimum.

**Gap.** ws4 has multi-objective search but no resilience-oriented portfolio or trade-off narrative.

**First step.** Define three archetype strategies (productivity, resilience, balanced) and run them through the existing portfolio search.

**Risks.** Indicator selection; incommensurable objectives; stakeholder disagreement.

**Sources.**

- [Silva21 AN 8a/8b](https://www.silva21.com/projects/forest-management-plans-for-resilient-landscapes)
- [Dura et al. 2026, A renewed call for action in climate-adapted forestry](https://doi.org/10.5558/tfc2026-018)

### `PLAN-03` — Spatial resilience metrics for estate models

- **Workstream:** Landscape planning and resilience
- **Status / wave:** complete / 1
- **FRESH targets:** `ws4`
- **Integration:** validation
- **Effort / impact / readiness / risk:** M / 4 / 4 / 2
- **Screening score:** 4.00

**What.** Define a compact set of landscape-configuration metrics (connectivity, age-class diversity, patch-size distribution, fragmentation) and emit them as ws4 accounts.

**Gap.** ws4 has patch and spread accounts but no resilience-oriented summary that a planner or reviewer can interpret.

**First step.** Implement three metrics as report accounts and compare two existing ws4 schedules.

**Risks.** Metric redundancy; scale sensitivity; false precision.

**Resolution.** Implemented in UBC-FRESH/ws4#378, child of P54 (#375); PR #475 adds connectivity, age-class diversity, and fragmentation accounts plus a two-run comparison and report block.

**Provenance.** Live audit 2026-11-03: UBC-FRESH/ws4#378 is closed, PR #475 is merged as `865bef6`, and parent P54 (#375) is closed. See notes/17-p2-contract-audit.md.

**Sources.**

- [IRSS landscape pattern and disturbance research](https://irsslab.forestry.ubc.ca/research/disturbance-habitat-change/)
- [ws4 spatial, patch, and spread accounts](https://github.com/UBC-FRESH/ws4)

### `PLAN-04` — Caribou habitat and dynamic mitigation

- **Workstream:** Landscape planning and resilience
- **Status / wave:** candidate / 3
- **FRESH targets:** `ws4`
- **Integration:** model
- **Effort / impact / readiness / risk:** L / 4 / 3 / 3
- **Screening score:** 1.33

**What.** Add a caribou habitat account and dynamic mitigation constraints based on lichen volume, stand structure, and disturbance recovery.

**Gap.** Habitat is not a first-class constraint or output; caribou plans are handled outside the estate model.

**First step.** Ingest one lichen/habitat layer and add a habitat account before adding a constraint.

**Risks.** Habitat science uncertainty; legal and policy sensitivity; data availability.

**Sources.**

- [Silva21 AN 9, Flexibility in forest management to preserve caribou habitat](https://www.silva21.com/projects/flexibility-in-forest-management-to-preserve-caribou-habitat)
- [Beaulieu et al. 2026, Annual lichen volume for woodland caribou](https://doi.org/10.1016/j.jag.2026.105444)

### `PLAN-05` — Habitat connectivity account over the road and patch network

- **Workstream:** Landscape planning and resilience
- **Status / wave:** shortlisted / 2
- **FRESH targets:** `ws4`
- **Integration:** algorithm
- **Effort / impact / readiness / risk:** M / 4 / 2 / 2
- **Screening score:** 2.00

**What.** Compute connectivity and barrier effects from ws4's road and patch topology and report them alongside volume and cost.

**Gap.** ws4 models roads and patches for access and harvest adjacency, not for wildlife connectivity.

**First step.** Implement a least-cost or circuit-style connectivity metric on one ws4 dataset and compare two road strategies.

**Risks.** Resistance-surface assumptions; computational cost; interpretation.

**Sources.**

- [IRSS habitat connectivity and road impacts](https://irsslab.forestry.ubc.ca/publications/)
- [ws4 roads and patch topology](https://github.com/UBC-FRESH/ws4)

### `PLAN-06` — Deliberative-analytic and serious-game engagement

- **Workstream:** Landscape planning and resilience
- **Status / wave:** deferred / 0
- **FRESH targets:** `ws4`
- **Integration:** ui
- **Effort / impact / readiness / risk:** L / 3 / 2 / 3
- **Screening score:** 0.67

**What.** Explore a stakeholder-facing mode where participants choose strategies and see consequences, informed by the deliberative-analytic literature.

**Gap.** ws4 is an analyst tool; there is no structured public or stakeholder engagement surface.

**First step.** Write a concept note and user journey; do not build until the scenario engine and web UI are stable.

**Risks.** Scope creep; facilitation-heavy; difficult to validate; not a software-first problem.

**Sources.**

- [Silva21 AD 5a, Deliberative-analytic framework](https://www.silva21.com/projects/deliberative-analytic-framework-to-engage-publics-and-stakeholders)
- [Silva21 AD 5b, Serious game for adaptive silviculture](https://www.silva21.com/projects/climate-change-and-adaptative-silviculture%3A-playing-to-collaborate-with-a-serious-game)

### `PLAN-07` — Scenario storytelling and visualisation

- **Workstream:** Landscape planning and resilience
- **Status / wave:** complete / 2
- **FRESH targets:** `ws4`
- **Integration:** ui
- **Effort / impact / readiness / risk:** M / 3 / 4 / 1
- **Screening score:** 6.00

**What.** Add a storyboard export that combines maps, indicators, uncertainty, and trade-offs into a shareable scenario narrative.

**Gap.** ws4 maps are analytical views, not communication products; scenario comparison is table-heavy.

**First step.** Design a one-page scenario storyboard template and generate it from an existing run.

**Risks.** Visual bias; accessibility; maintenance of templates.

**Resolution.** Complete as UBC-FRESH/ws4 P101 (#696, PR #698, `91b985c`): one-page Markdown storyboard reusing the condition card and provenance. Charts, maps, and browser storyboards remain separate.

**Sources.**

- [Silva21 AD 7, Visualisation techniques for social commentary](https://www.silva21.com/projects/visualisation-techniques-for-social-commentary)
- [Silva21 AN 8b, Landscape-level visualisations](https://www.silva21.com/projects/viability-of-climate-informed%2C-landscape-level-strategies)

### `PLAN-08` — Market and policy shock scenarios

- **Workstream:** Landscape planning and resilience
- **Status / wave:** complete / 2
- **FRESH targets:** `ws4`, `fhops`
- **Integration:** data-contract
- **Effort / impact / readiness / risk:** S / 3 / 4 / 2
- **Screening score:** 6.00

**What.** Support price, cost, and policy paths as scenario inputs with provenance, rather than single static values.

**Gap.** Economic assumptions are static and buried in config; there is no scenario narrative for market or policy shocks.

**First step.** Add a `prices.v1` table and a small set of named price paths to one ws4/FHOPS scenario.

**Risks.** Forecast credibility; currency and region mismatch; overfitting to recent shocks.

**Resolution.** Complete as UBC-FRESH/ws4 P114 (#749, PR #760, merge `0dbc01a`): the typed `prices.v1` reader in `ws4/prices.py`, the `ws4 price-paths` command, the synthetic four-path fixture, and the comparison CSV/Markdown/provenance outputs with the `not a forecast` caveat. The table is read-only and no objective, constraint, growth, schedule, or solver code changed. A real public price source with currency/region provenance remains a follow-on before production use.

**Sources.**

- [Dura et al. 2025, Macroeconomic and climate-disaster effects on wood product prices](https://doi.org/10.1139/cjfr-2025-0001)
