# FRESH gap analysis

This note records what the ecosystem does well today, where the IRSS/Silva21
material actually fits, and what should **not** be rebuilt.

Basis: inspection of the five repositories' READMEs, roadmaps, and reference
docs, plus the source module layout, on 2026-10-25. This is a planning
assessment, not a code audit.

## Summary

| Repo | Strong today | Thin today | Best IRSS/Silva21 fit |
| --- | --- | --- | --- |
| `femic` | Inventory prep, stratification, VDYP/TIPSY curve fitting, Patchworks/Woodstock export, open LiDAR product pipeline, DataLad data | Area-based EFI attribute models, climate/variable curves, disturbance and recovery attributes, carbon, uncertainty, model cards | Inventory, site index, species, curve modifiers, disturbance/recovery attributes, LiDAR EFI |
| `ws3` | Strategic estate model, curves/actions, optimization, spatial allocation, CBM linkage, avoided-fire/harvest examples | Shared climate/risk contracts, modern hazard layers, operational link | Carbon contract, risk-aware scenarios, strategic comparison |
| `ws4` | Fragments/blocks/strata/tracks, simulation, metaheuristic and MIP optimization, patch/spread accounts, roads, web UI, provenance | Environmental state layers, climate/risk transitions, carbon/habitat accounts, uncertainty | Accounts, constraints, risk, habitat, carbon, web layers |
| `fhops` | Scenario contract, operational MIP, heuristics, rolling horizon, costing/productivity, hauling, road access, salvage mode | Shelf-life/decay, fuel treatment, thinning priority, plan-versus-actual, carbon | Salvage, thinning, fuel treatment, access, monitoring |
| `nemora` | Distribution registry, fitting, sampling, ingest, synthesis, CLI | Simulation, uncertainty propagation to models, SDM, imputation, validation harness | Fitting, synthetic forests, sampling, imputation, validation |

## `femic`: the upstream builder

### Strong today

- **Pipeline boundaries are explicit.** Stage 00 inventory prep and
  stratification, Stage 01a VDYP/TIPSY curve fitting and BatchTIPSY handoff,
  Stage 01b post-processing, and export are documented contracts. This is a good
  place to add attributes because the seams are already named.
- **Open LiDAR is a real pipeline, not an idea.** FEMIC discovers LidarBC
  tiles, materializes them resumably, derives terrain and slope, builds stream
  candidates, derives CHM/canopy structure, inspects individual-tree products,
  and packages a versioned product bundle (`femic.lidar.product.v1`) for WS4
  and FHOPS consumers. The bundle carries CRS, resolution, vertical datum,
  licence, lineage, and checksums.
- **Curve fitting and export are mature.** VDYP/TIPSY are wired, and the
  Patchworks/Woodstock export path is a tested contract.
- **Provenance is already a habit.** Instance roots, external data roots,
  DataLad, manifests, and stage boundaries are documented.

### Thin today

- **No area-based inventory model.** The LiDAR pipeline stops at canopy and
  tree products. It does not fit or apply ABA models for volume, basal area,
  density, species fractions, or site index, and it does not carry per-attribute
  error into curve selection. This is the single most valuable `femic` gap.
- **No climate-aware curve lane.** VDYP/TIPSY curves are static. There is no
  modifier contract, no climate provenance, and no way to compare a baseline
  curve with a climate-adjusted one.
- **No disturbance/recovery attributes.** Partial mortality, defoliation,
  drought stress, and regeneration failure are not first-class fragment
  attributes.
- **No carbon lane.** TIPSY-CBM is an idea in the incoming queue, not a
  contract.
- **No model card for derived attributes.** The sensor bundle is well
  described; the inventory model that turns it into attributes is not.

### Where to insert

- `femic/lidar/*` products -> new inventory-attribute application layer.
- `femic/vdyp_io/*` and the curve-fitting stage -> modifier and provenance
  hooks.
- `femic/models/<instance>` and `config/silviculture*.yaml` -> disturbance,
  recovery, and treatment attributes.
- Export XML/fragments -> new feature and product accounts.

## `ws3`: the strategic lane

### Strong today

- A full `ForestModel` with curves, actions, themes, and optimization.
- `spatial.py` allocates an aspatial schedule to a raster representation.
- **CBM is already integrated.** `forest.py` contains CBM site classifiers,
  disturbance types, inventory/yield/events/transitions, and `to_cbm_sit`.
  The examples include avoided-fire and avoided-harvest decision support.
- Agent capabilities with real oracles.

### Thin today

- No shared climate/risk contract. Scenarios are built from model files, not
  from a state layer.
- The CBM linkage is a notebook/API capability, not a reusable carbon account
  contract.
- The strategic and spatial lanes (`ws3` and `ws4`) do not share environmental
  inputs.

### Where to insert

- `forest.py` curve/action/transition definitions -> climate and hazard
  modifiers.
- `integration.py` and `to_cbm_sit` -> carbon contract and shared account.
- `spatial.py` -> risk and habitat layers for allocation.

## `ws4`: the spatial estate engine

### Strong today

- Space is first-class: fragments, runtime blocks, adjacency, patch structure,
  and roads are enforced in simulation and optimization.
- Simulation, metaheuristic search, portfolio search, MIP lane, constraint
  repair, goal normalization, and reproducibility are mature.
- Patch, spread, road, and flow accounts exist.
- The web UI, map serving, comparison, and provenance surfaces are real.
- The optimizer already has a fire/patch experiment with a documented negative
  result. This is a warning against porting a fire-spread model wholesale.

### Thin today

- **The state layer is static.** A compiled dataset is built once; there is no
  climate, disturbance, carbon, or habitat state that updates between runs.
- **No risk transition.** Hazards are not in the simulation; risk is not in the
  objective except through the existing spatial accounts.
- **No carbon or habitat account.** The accounting surface is volume, product,
  feature, patch, spread, and roads.
- **No uncertainty.** Yields and prices are deterministic.
- **External environmental layers are not first-class.** They arrive, if at
  all, as bespoke feature curves.

### Where to insert

- `ws4/model/schema.py`: new account and attribute tables.
- `ws4/sim/`: transition and hazard hooks.
- `ws4/opt/objective.py` and `ws4/opt/constraints.py`: expected loss and
  resilience terms.
- `ws4/patch/` and `ws4/spread/`: resilience and connectivity metrics.
- `ws4/roads/`: road status and access.
- `ws4/web/`: climate/risk/carbon/habitat layers and report cards.

## `fhops`: the operations engine

### Strong today

- A Pydantic scenario contract for blocks, machines, landings, calendars,
  products, facilities, inventory, consumption, and outside purchases.
- Operational MIP and a heuristic engine (SA, ILS, Tabu), rolling horizon,
  locks, initial state, and playback.
- Costing and productivity regressions with FPInnovations provenance.
- Hauling, network, marine/port legs, and road access (`BlockRoadAccess`).
- `salvage_processing_mode` exists on blocks.

### Thin today

- **Salvage is a mode, not a workflow.** There is no shelf-life, value decay,
  or urgency model.
- **No fuel-treatment or biomass-recovery planning.** Fuel layers and biomass
  products are not part of the scenario.
- **No within-stand thinning priority.** Blocks carry average stem size and
  density, not a LiDAR-derived competition or thinning prescription.
- **No plan-versus-actual loop.** Harvest detection is not compared with
  schedules.
- **No carbon.** Product flows are not converted to carbon.

### Where to insert

- `fhops/scenario/contract/models.py`: shelf-life, decay, fuel, biomass, and
  carbon fields.
- `fhops/planning/tactical_operational/models.py`: products, road access,
  silviculture transitions.
- `fhops/optimization/`: salvage urgency and fuel-treatment objectives.
- `fhops/eval/kpis.py`: plan-versus-actual and carbon KPIs.

## `nemora`: the analytics substrate

### Strong today

- A distribution registry with fitting, mixtures, and sampling.
- Ingest pipelines for FAIB, FIA, and HPS with nightly integration tests.
- Synthesis: tessellation, stand attributes, stems, exporters, and CLI.
- A working alpha surface and a nightly ingest benchmark.

### Thin today

- **Simulation is planned, not built.** There is no measurement-campaign
  simulator.
- **Uncertainty does not reach the models.** Fitting exists, but curves in
  FEMIC/ws4 are point estimates.
- **No SDM or imputation module.**
- **No cross-repo validation harness.**

### Where to insert

- `nemora/distributions`, `fit`, `sampling` -> curve uncertainty.
- `nemora/synthesis` -> synthetic landscapes and FHOPS/FEMIC fixtures.
- `nemora/ingest` -> shared inventory schema.
- New `nemora/simulation` -> measurement campaigns and validation.
- New `nemora/impute` or `nemora.fusion` -> imputation and data fusion.

## Cross-cutting gaps

| Gap | Evidence | Consequence |
| --- | --- | --- |
| **State layer** | FEMIC builds a static inventory; ws4 compiles a static dataset; no monitoring loop | Plans are anchored to a vintage, not the current forest |
| **Dynamics** | Static VDYP/TIPSY curves; no climate, mortality, or hazard transitions | The model cannot answer "what if the climate or disturbance regime changes?" |
| **Values** | Volume/product/feature accounts; CBM only in ws3 notebooks | Carbon, habitat, and resilience are external analyses, not scenario outputs |
| **Uncertainty** | Deterministic curves, prices, and yields | Reports imply false precision; robust plans are not tested |
| **Provenance to the user** | Manifests exist in FEMIC/ws4, but reports do not show them | Decision-makers cannot see which assumptions drive a result |
| **Independent validation** | Validation is concentrated in BC inventory and a few instances | Claims do not generalize across hubs, species, or disturbance regimes |

## What not to rebuild

The mine is as much about avoiding duplicate work as adding it.

- **Do not rebuild the LiDAR source/materialization/terrain/canopy/bundle
  pipeline.** FEMIC owns it and has contracts. Add the inventory-attribute
  layer on top.
- **Do not rebuild CBM.** ws3 has a working linkage. Define a shared account
  and reuse it.
- **Do not rebuild the ws4 spatial engine.** Patch, spread, road, and flow
  accounts are mature. Add new metrics and layers through their interfaces.
- **Do not rebuild the FHOPS operations engine.** The scenario contract, MIP,
  heuristics, and costing are mature. Add salvage, fuel, thinning, and carbon
  fields and objectives.
- **Do not rebuild the Nemora fitting/sampling stack.** It is the strongest
  analytics surface in the ecosystem. Add simulation, imputation, and
  uncertainty propagation.
- **Do not port a fire-spread simulator.** ws4's P15/P16 experiment produced a
  documented negative result at the treated footprint. Treat fire as a hazard
  or an expected-loss term, not a new simulator, until the evidence changes.

## Sequencing implication

The gaps are ordered:

1. **Contracts** (state, climate, disturbance, model cards, accounts).
2. **Adapters** (curves, inventories, hazards, operations).
3. **Uncertainty and validation** (distributions, synthetic data, hub network).

This is why the first wave is contract-heavy and the third wave is
research-heavy. The register's wave assignment encodes that order even when a
later candidate has a higher raw score.
