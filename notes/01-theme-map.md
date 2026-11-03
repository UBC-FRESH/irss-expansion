# Theme map: IRSS and Silva21 to FRESH

## The shape of the opportunity

IRSS and Silva21 are not a bag of unrelated papers. They form a stack that maps
unusually well onto what a forest modelling ecosystem needs:

```
   measurement          dynamics              decisions
   -----------          --------              ---------
   LiDAR / EFI          growth + mortality     estate planning
   optical time series  disturbance/recovery   operations
   field plots          carbon                habitat / risk
   climate layers       species suitability    monitoring
        |                    |                     |
        +-----------> FRESH state layer <----------+
                             |
                    FEMIC / ws3 / ws4 / FHOPS / Nemora
```

FRESH has the right-hand side and the engines. The left and middle are thin.
The programme is therefore a **state-and-dynamics layer**, delivered as shared
contracts and adapters, not a rewrite of the engines.

## IRSS research themes

| IRSS theme | What it produces | FRESH relevance | Candidate IDs |
| --- | --- | --- | --- |
| NTEMS | National Landsat change, attribution, recovery, land cover | Disturbance events, recovery state, validation | `DIS-01`, `DIS-02`, `DIS-04` |
| BioSpace | Biodiversity modules, fragmentation, Dynamic Habitat Indices | Biodiversity accounts, landscape metrics | `BIO-01`, `PLAN-03` |
| Biodiversity | Avian SDMs, DHI, conservation regionalization, habitat indices | Habitat accounts, species suitability, connectivity | `BIO-01`, `BIO-02`, `BIO-03`, `PLAN-05` |
| Disturbance and habitat change | Anthropogenic disturbance regimes, grizzly food landscapes, LANDIS-II/TACA-GEM | Disturbance schema, hazard library, habitat scenarios | `DIS-01`, `DIS-06`, `PLAN-04` |
| Carbon and forest dynamics | Disturbance-carbon links, Landsat attributes, GPP, biomass | Carbon account, emissions, biomass curves | `CARB-01`, `CARB-02`, `GRO-06` |
| Data fusion | Hyperspectral + LiDAR + Landsat for composition and structure | Species fractions, structure habitat index, imputation | `INV-05`, `BIO-02`, `DATA-05` |
| Mountain pine beetle | Beetle infestation patterns, landscape fragmentation | Beetle hazard, salvage trigger | `DIS-08` |
| LiDAR | Structure, canopy depth, GPP, biomass, change, genetic gain | EFI contract, site index, tree lists, change detection, seedlot performance | `INV-01` to `INV-04`, `INV-08` to `INV-10`, `DEC-04` |
| Urban | Urban energy, canopy, vegetation | Out of scope for the estate model; no near-term candidate | None (screened out) |
| Mobile remote sensing | Smartphone fuels app, volunteered data | Field-data intake, fuels, public participation | `OPS-02` (component) |
| Water resources | Snow, hydrology, stream structure | Input/validation for the active FEMIC P114 hydrology phase; stream metrics via `BIO-04` | `BIO-04` |

Two IRSS themes are deliberately not core: **urban** and **water resources**.
They are strong research programmes but they do not change a near-term FRESH
estate or operations decision. The exceptions are stream/riparian metrics
(`BIO-04`) and a future water module.

## Silva21 themes

Silva21 organises its work into three verbs. They map cleanly onto the FRESH
stack.

### Observe (OB)

Sensors, inventory, monitoring, and measurement.

| Cluster | Projects | FRESH hook | Candidates |
| --- | --- | --- | --- |
| Continuous forest inventory | OB 5a, OB 5b, OB 5c, OB 5d | State layer, update, prescription metrics | `INV-01`, `DIS-02`, `DIS-03`, `DEC-02` |
| LiDAR and EFI | OB 4a, OB 4b, OB 2, OB 6 | EFI contract, growth integration, tree lists, drone data | `INV-01`, `INV-02`, `INV-07`, `DEC-04` |
| Optical monitoring | OB 3a, OB 3b, OB 3c | Seasonal composites, early alert, operational adoption | `DIS-02`, `DIS-03`, `DEC-02` |
| Regeneration and recovery | OB 1a, OB 1b, OB 7 | Post-fire recovery, regeneration failure, burn patterns | `DIS-04`, `DIS-05` |
| Climate-sensitive growth | OB 7 (Ontario) | Mortality and growth models | `GRO-03`, `GRO-07` |

### Anticipate (AN)

Climate, growth, mortality, species, and landscape futures.

| Cluster | Projects | FRESH hook | Candidates |
| --- | --- | --- | --- |
| Climate envelopes | AN 1a, AN 1b, AN 1c, AN 1e | Climate contract, species suitability, acute events | `GRO-01`, `GRO-08`, `DIS-06` |
| Growth and mortality | AN 3a, AN 3b, AN 1c, AN 7 | Climate modifiers, mortality transitions, thinning response | `GRO-02`, `GRO-03`, `GRO-05` |
| Assisted migration | AN 5, AD 9a, AD 9b | Suitability and provenance layers | `GRO-08` |
| Landscape strategies | AN 8a, AN 8b | Risk-aware estate planning, resilience portfolio | `PLAN-01`, `PLAN-02` |
| Habitat | AN 9 | Caribou habitat and dynamic mitigation | `PLAN-04`, `BIO-05` |
| Wood and tree rings | AN 1d, AN 2, AN 4 | Validation data, wood quality | `GRO-07` |

### Adapt (AD)

Silviculture, operations, salvage, and engagement.

| Cluster | Projects | FRESH hook | Candidates |
| --- | --- | --- | --- |
| Silvicultural scenarios | AD 2, AD 3a, AD 3b, AD 3c | Treatment design, resilience, multi-objective | `PLAN-02`, `OPS-01` |
| Salvage | AD 4 | Salvage scheduling, shelf-life, value decay | `DIS-09`, `OPS-03`, `CARB-03` |
| Assisted migration trials | AD 9a, AD 9b | Provenance and establishment evidence | `GRO-08` |
| Engagement and policy | AD 5a, AD 5b, AD 6, AD 7, AD 8a | Deliberation, serious games, visualisation, cultural values | `PLAN-06` (deferred), `PLAN-07` |
| Trials and synthesis | AD 1a, AD 1b, AD 8b, AD 10 | Long-term evidence, extension | `GRO-07`, `DIS-06` |

## Cross-cutting capabilities

Four capabilities recur across both bodies of work and deserve special
attention because they are **reusable infrastructure**, not one-off studies.

| Capability | Why it matters to FRESH | Candidate IDs |
| --- | --- | --- |
| LiDAR and EFI | The most mature measurement stack; directly improves inventory and curves | `INV-01` to `INV-09`, `DEC-04` |
| Optical time series | The only practical way to keep the state layer current | `DIS-02`, `DIS-03`, `OPS-04` |
| Climate downscaling | The input to every climate-sensitive model | `GRO-01`, `GRO-08` |
| Field and long-term trials | The validation layer that keeps models honest | `GRO-07`, `DEC-05`, `DATA-03` |

## The three integration modes

Every candidate uses one of three modes. The mode predicts effort and risk more
than the topic does.

1. **Data product ingestion.** A layer, table, or raster is consumed and stored
   with provenance. Lowest effort; the risk is licensing and schema drift.
   Examples: `BIO-01`, `INV-05`, `GRO-06`.
2. **Model or algorithm adapter.** A published relationship becomes a function,
   transition, account, or constraint. Medium effort; the risk is
   transferability and validation. Examples: `GRO-02`, `DIS-06`, `CARB-01`.
3. **Co-developed research module.** New science is needed, often with a
   partner and new data. Highest effort and risk. Examples: `GRO-04`,
   `GRO-09`, `DATA-06`, `DEC-05`.

The first wave is deliberately almost all mode 1 and mode 2. Mode 3 is held
until the contracts exist and the validation network is real.

## What the map implies

- **The biggest near-term win is not a model.** It is the shared state layer:
  climate, disturbance, LiDAR/EFI, and account contracts.
- **FEMIC is the natural entry point** for inventory, site index, species, and
  curve modifiers.
- **ws4 is the natural entry point** for accounts, constraints, risk, habitat,
  carbon, and the web surface.
- **FHOPS is the natural entry point** for salvage, thinning, fuel treatment,
  road access, and plan-versus-actual.
- **Nemora is the natural entry point** for fitting, uncertainty, sampling,
  synthesis, imputation, and validation.
- **ws3 is the strategic comparison lane**: the same climate/risk/carbon
  scenarios should run in both ws3 and ws4 so the ecosystem can compare
  strategic and spatial answers.
