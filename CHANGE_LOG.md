# Change Log

Newest entries last. Each milestone gets a dated entry that matches the roadmap status and the GitHub issue comments.

## 2026-10-25

### P0 mine and publish the register

Added the initial IRSS x Silva21 expansion mine.

- Mined the public IRSS site: home, research index, 11 research theme pages,
  and the publications page (493 records, 2004-2023 as rendered).
- Mined the public Silva21 site: home, 47 project pages, 2022-2026 scientific
  publications, climate data/SilvR21, extension notes, and data-portal
  description.
- Mapped the sources to the five FRESH repos and cross-repo surfaces in
  `notes/01-theme-map.md` and `notes/03-fresh-gap-analysis.md`.
- Built `registry/candidates.yaml` with 62 candidates in nine workstreams,
  each with sources, targets, gap, first step, effort/impact/readiness/risk,
  and a risk note.
- Added `scripts/check_registry.py` (validation, ranking), 
  `scripts/render_registry.py` (generated `docs/candidates.md`), and
  `tests/test_registry.py`.
- Added the programme roadmap, first-wave briefs, out-of-scope note, source
  inventory, Silva21 project map, and a proposed cross-repo issue tree.
- Added `notes/10-repo-state-check.md` after checking the live repo state.
  The check corrected two things: FEMIC P114 already owns hydrology (so water
  is not queued as a new module), and FEMIC P109 already owns CT diameter and
  log-grade value/cost accounts (so `OPS-01`/`OPS-06` build on it rather than
  duplicate it).
- Added `handoffs/` with issue bodies for the wave-1 candidates.
  The ws3/ws4 carbon drafts were later moved to `handoffs/superseded/` because
  live carbon work already exists.
- Created the approved first set in GitHub:
  - `UBC-FRESH/femic` `#369` P116 (shared environmental contracts), with
    sub-issues `#370` P116.1 (`GRO-01`), `#371` P116.2 (`DIS-01`), and
    `#372` P116.3 (`DEC-04`).
  - `UBC-FRESH/nemora` `#6` (`DATA-01`, curve uncertainty).
- Marked `CARB-01` as `adopted`: it is covered by `UBC-FRESH/femic` `#361`
  (P115, forest carbon domain) and `UBC-FRESH/ws4` `#357` (P51, carbon
  accounting). No parallel carbon issue was created.
- Created the remaining wave-1 issues:
  - `UBC-FRESH/femic` `#374` P117 (EFI inventory attributes and biomass
    curves), with sub-issues `#375` (`INV-04`) and `#376` (`GRO-06`).
  - `UBC-FRESH/nemora` `#7` P5 (uncertainty, sampling, synthetic validation),
    with sub-issues `#8` (`DATA-02`), `#9` (`DATA-04`), and `#10` (`INV-06`).
    `DATA-01` `#6` was linked as `P5.1`.
  - `UBC-FRESH/ws4` `#375` P54 (habitat and resilience accounts), with
    sub-issues `#376` (`BIO-01`), `#377` (`BIO-02`), and `#378` (`PLAN-03`).
  P54 is used because P53 was taken by a ws4 release-preparation phase.
- All wave-1 candidates now carry `resolution` links in the register. The
  register status is 1 adopted (`CARB-01`), 12 queued, 23 shortlisted, 24
  candidate, and 2 deferred.

## 2026-10-25

### phase setup in the target repos

Created the four phase branches from each repo's `main`, added the roadmap
entries and planning notes, committed, and pushed:

- `femic` `feature/p116-shared-contracts` at `0bc6cf8`; P116 roadmap entry and
  `planning/phase116_shared_contracts.md`.
- `femic` `feature/p117-efi-attributes` at `a0a7cbd`; P117 roadmap entry and
  `planning/phase117_efi_attributes.md`.
- `nemora` `feature/p5-uncertainty-sampling` at `54604dc`; Phase 5 roadmap
  entry and `notes/p5_uncertainty_sampling_plan.md`.
- `ws4` `feature/p54-environmental-accounts` at `9b9b9bf`; P54 roadmap entry
  and `notes/p54-environmental-accounts.md`.

`ws4/scripts/check_workflow.py` reports 0 errors and 0 warnings. Progress
comments were posted on `femic#369`, `femic#374`, `nemora#7`, and `ws4#375`.
The parent issue phase-setup checklists are updated. No implementation, pull
request, tag, or release was created.

## 2026-10-25

### P116.1 first slice

Implemented the `femic.climate.v1` contract on
`femic/feature/p116-shared-contracts` at `6dcddc6`:

- `femic.contracts.climate` schema, validator, CSV/JSON reader and writer,
  provenance summary, and a public-safe sample table.
- Contract and API docs pages.
- 16 focused tests; targeted ruff and mypy pass; Sphinx `-W` passes.

The ClimateNA/SilvR21 adapter and the first curve/attribute consumer remain
open on `UBC-FRESH/femic#370`.

## 2026-10-25

### P116.2 disturbance contract

Implemented `femic.disturbance.v1` on `femic/feature/p116-shared-contracts` at
`85080e0`:

- `femic.contracts.disturbance` schema, validator, JSON reader/writer,
  provenance summary, ws4-facing consumer rows, and fire/NSR examples.
- Contract and API docs pages.
- 18 focused tests; the two contract suites now total 34 passing tests;
  targeted ruff and mypy pass; Sphinx `-W` passes.

The actual ws4 loader and scenario report remain open on
`UBC-FRESH/femic#371`.

## 2026-10-25

### P116.3 EFI model-card contract

Implemented `femic.efi.model.v1` on `femic/feature/p116-shared-contracts` at
`cba4173`:

- `femic.contracts.efi` schema, nested training/validation/applicability
  metadata, applicability checks, and attribute-row annotation.
- Two public-safe synthetic cards (height and volume), contract/API docs, and
  22 focused tests. The three contract suites total 56 passing tests.
- Targeted ruff and mypy pass; Sphinx `-W` passes.

Real project/published model cards and the FEMIC attribute-pipeline wiring
remain open on `UBC-FRESH/femic#372`.

## 2026-10-26

### P116.1 ClimateNA adapter

Implemented `femic.contracts.climate_na.read_climate_na_csv` on
`femic/feature/p116-shared-contracts` at `1df155a`:

- Annual ClimateNA/SilvR21 CSV adapter with a default column map, explicit
  `column_map` override, missing-token handling, and source-column provenance.
- Public-safe ClimateNA-shaped fixture and 11 focused tests; the four contract
  suites total 67 passing tests.
- Targeted ruff and mypy pass; Sphinx `-W` passes.

The first curve/attribute consumer remains open on `UBC-FRESH/femic#370`.

## 2026-10-26

### P116.1 climate consumer

Implemented the first `femic.climate.v1` consumer on
`femic/feature/p116-shared-contracts` at `b2d7478`:

- `femic.climate.consumer` context selection, ambiguity and mixed-source
  checks, per-row AOI resolution, and provenance-bearing attachment to
  attribute rows.
- 13 focused tests; the five contract/consumer suites total 80 passing tests.
- Targeted ruff and mypy pass; Sphinx `-W` passes.

P116.1 is implementation-complete on the branch and ready for PR/closeout.

## 2026-10-26

### PRs opened

- `UBC-FRESH/ws4#398`: P56.1 disturbance consumer, base `main`. Rebased onto
  `origin/main` at `c0f71af`; dashboard **GREEN**; all CI checks pass; PR is
  mergeable and ready for maintainer approval.
- `UBC-FRESH/femic#377`: P116 shared contracts, **draft** because P116.2/P116.3
  follow-ups remain. Carries the climate contract/adapter/consumer, disturbance
  contract, and EFI model-card contract. CI checks pass; mergeable.

No merge, tag, or release was performed at the time of the first PR report.

## 2026-10-26

### P117 cancelled; software-only scope

- Cancelled P117 as a modelling exercise. SI is already covered by VRI, VDYP,
  and SIBEC; no new general ALS SI/height model will be derived.
- `INV-04` is `rejected`, not deferred. The generic `femic.efi.application`
  engine remains available for an existing model card.
- Tightened the planning scope: consume existing BC products; no new
  remote-sensing science. Examples: VRI, VDYP, SIBEC, LidarBC, NTEMS/HLS.
- The active queue is software integration, workflow, reporting, validation,
  and deployment work.

## 2026-10-26

### P5.1 curve uncertainty merged

- `UBC-FRESH/nemora#11` squash-merged as `cbf504d`.
- `DATA-01` marked `complete`; nemora #6 closed, parent #7 open for P5.2-P5.4.
- Real TSA46 CWH_HW height pilot: 840 train / 306 holdout pairs, Weibull 90%
  ratio interval 0.686-1.989, holdout coverage 87.6%.
- Full Nemora suite: 149 passed, 4 skipped; CI green.

## 2026-10-26

### P117.1 parked

- Parked P117.1. Deriving a defensible new general height/site-index model is
  research, not integration.
- The merged `femic.efi.application` engine remains generic infrastructure.
- `INV-04` is marked `deferred`; P117 is `deferred` in the roadmap.
- Added a scope rule: consume existing published models/products; if a
  candidate needs a new general model, park it as research and name the
  partner, data, or grant it would need.
- No further SI model work is queued. The VRI-proxy pilot and data-readiness
  notes are retained as evidence for why.

## 2026-10-26

### VRI-proxy pilot

- Downloaded four LidarBC point-cloud tiles (1.2 GiB) around the TSA46
  `1389961` area with FEMIC materialization.
- Built CHM at 2 m and sampled 32 VRI polygons with `SITE_INDEX` in a 20 m
  buffer.
- CHM p95 alone: R² 0.11, LOO RMSE 6.37 m. CHM p95 + age: R² 0.58, LOO RMSE
  4.56 m, but the target is derived from height/age and is circular.
- Decision: do not train or ship a VRI-proxy SI model; use as screening
  evidence. Added `notes/13-vri-proxy-pilot.md`.

## 2026-10-26

### LidarBC pilot

- Pulled FEMIC `origin/main` (`b71ea1a`) and ws4 `origin/main` (`f8117e5`), and
  read the P79/P52/P59 LiDAR docs and closeout notes.
- Discovered and materialized one open LidarBC point-cloud tile
  (`bc_093d038_4_4_3_xyes_8_utm09_2019.laz`, 64.1 MiB, OGL-BC, 2019) for TSA46
  site `1389961`.
- Derived CHM at five VRI polygons inside the tile; three had points. The VRI
  centroid is about 112 m outside the actual point extent.
- Coverage audit: of 17 ground-plot sites, only `1389961` has point cloud,
  two have DEM, and none has DSM. The open coverage cannot support a multi-site
  SI backtest.
- Added `notes/12-lidarbc-pilot.md`. No coefficients were fabricated.

## 2026-10-26

### P117.1 engine merged; data readiness

- Focused P117.1 PR `UBC-FRESH/femic#381` squash-merged as `02aba7c`.
- `#375` remains open for real coefficients, LiDAR metric mapping, `si_als`
  pipeline wiring, and the P48/P49 backtest.
- Added `notes/11-p1171-data-readiness.md`: TSA46 has 20 ground plots with
  `observed_si` but no ALS predictors; TFL6 has CHM + VRI height but no observed
  SI. The real backtest is data-blocked; no coefficients were fabricated.

## 2026-10-26

### P116.3 contract merged

- Focused P116.3 PR `UBC-FRESH/femic#380` squash-merged as `f833ed9`.
- `#372` was auto-closed by the PR text and has been re-opened: real
  project/published cards and the FEMIC attribute-pipeline wiring remain.
- `DEC-04` is marked `complete` for the contract, with the #372 follow-up
  recorded.
- `#369` remains open for the P116.3 follow-ups.

## 2026-10-26

### P116.2 merged

- Focused P116.2 PR `UBC-FRESH/femic#379` squash-merged as `ef4cff2`.
- `#371` closed; `#369` remains open for P116.3.
- `DIS-01` is marked `complete` in the register.
- The ws4 consumer was already merged in `UBC-FRESH/ws4#398` (`5ea4a05`).

## 2026-10-26

### P116.1 merged

- Draft PR #377 was closed as superseded.
- Focused P116.1 PR `UBC-FRESH/femic#378` squash-merged as `9e16be9`.
- `#370` closed; `#369` remains open for P116.2 and P116.3.
- `GRO-01` is marked `complete` in the register.

## 2026-10-26

### P56 merged and closed out

- `UBC-FRESH/ws4#398` squash-merged as `5ea4a05`; `#394` and `#393` closed.
- Closeout PR `#404` squash-merged as `089f3e4`; P56 roadmap status is
  `complete` and the phase changelog records the merge hash.
- `UBC-FRESH/femic#377` remains a draft; the P116.2 contract is not yet merged.
  The FEMIC `#371` ws4-consumer note now points at the merged ws4 phase.

## 2026-10-26

### P56 disturbance consumer

Implemented the cross-repo ws4 consumer on
`ws4/feature/p56-disturbance-consumer` at `c0f71af`:

- `ws4/disturbance.py` and `ws4 disturbance --events <path> [--json] [--block-id ...]`.
- Loads the flat `consumer_rows()` shape or the full `femic.disturbance.v1`
  record and reports counts, types, years, severity, affected blocks/fragments,
  area, sources, and confidence range.
- 13 unit tests and 4 CLI tests; `ws4` dashboard **GREEN**.

The FEMIC P116.2 ws4-consumer item is now implemented on the ws4 branch and can
close when that phase merges.

## 2026-10-26

### P117.1 model application engine

Rebased `femic/feature/p117-efi-attributes` onto the P116 branch (`a8bbe16`) so
the EFI model-card contract is available, then implemented the first P117.1
slice at `67cba53`:

- `femic.efi.application`: `femic.efi.coefficients.v1` contract, linear
  prediction, applicability checks, domain flagging/dropping, and a
  bias/RMSE/MAE/R-squared backtest.
- A synthetic site-index pilot card and coefficients, 13 focused tests, and
  contract/API docs.
- The P117.1 and P116 contract suites total 69 passing tests; targeted ruff and
  mypy pass; Sphinx `-W` passes.

Real site-index coefficients, the `si_als` fragment pipeline, and the instance
backtest against P48/P49 remain open on `UBC-FRESH/femic#375`.

Verification:

```bash
python scripts/check_registry.py
# OK: registry is valid

python -m pytest
# 12 passed

python scripts/render_registry.py
# wrote docs/candidates.md
```

The handoff drafts were checked for internal links and placeholder discipline;
they are not executed.

Limitations:

- The mine is metadata and abstract level. It is not a full-text systematic
  review of 493 IRSS papers.
- The IRSS publication page appears to stop at 2023; Silva21's publication
  page covers 2024-2026.
- The Silva21 data portal is access-controlled. No data-sharing agreement was
  requested or assumed.
- Readiness scores are integration judgements, not author-confirmed estimates.
- No candidate was discussed with IRSS or Silva21 authors. The next step is a
  maintainer review, not an external commitment.

## 2026-10-26

### P119 SI reconciliation

Added P119 as the software response to the rejected P117 ALS site-index lane.
It consumes the existing VRI, VDYP, and SIBEC products instead of deriving a
new model.

- `femic` #392 (phase), #393 (P119.1), #399 (P119.2).
- P119.1 merged in `femic` #396 (`2a02fac`) and #400 (`e8898a1` closeout).
- Added `femic.site_index`: SIBEC tidy loader/aggregate, VRI and VDYP readers,
  feature-level reconciliation, JSON summary, CLI, tests, contract, guide, and
  API page.
- TSA46 pilot: 171,826 VRI features, 136,807 SIBEC matches, 3,384 VDYP
  primary-layer SI, 2,285 complete triples, 25,643 conflicts at 2.0 m.
- Recorded the limits: SIBEC is a BEC-unit/species range, not a polygon point
  estimate; VDYP primary-layer SI is sparse; the SIBEC 2014 addendum and
  AU-level TSA SI are P119.2.
- No curve, AAC, THLB, or schedule was changed.

## 2026-10-26

### P5.3 shared inventory schema

Closed `DATA-04` in Nemora.

- Added `nemora.inventory.v1` in `nemora.ingest.schema`: plots, trees, species,
  canonical units, provenance, validation, and a versioned release
  reader/writer.
- Migrated HPS through `inventory_release_from_hps` / `export_hps_inventory`
  and `nemora ingest-faib-hps --inventory-dir`.
- Kept the historical per-plot CSV and manifest bytes locked by checked-in
  fixtures.
- Added schema failure tests, a nightly schema regression step, and the
  contract/migration guide.
- Verification: 163 passed, 4 skipped; ruff, mypy, and Sphinx `-W` pass.
- Merged as nemora #12 (`9e7ea9e`). P5.2 (`DATA-02`, #8) and P5.4 (`INV-06`,
  #10) remain open.

## 2026-10-26

### P5.2 synthetic WS4 fixture

Closed `DATA-02` in Nemora.

- Added `nemora.synthesis.ws4_fixture`: seeded Voronoi fragments, three age
  classes, placeholder stems, and a WS4 recipe/fragments/schedule export.
- Published `examples/ws4_synthetic/` with the truth table, seed metadata, and
  landscape GeoJSON.
- Known fixture: seed `20261026`, 12 fragments, 36.0 ha, expected first-year
  volume `6623.03115 m3`.
- Local WS4 build/simulate reproduced `6623.031150000001 m3` at offset 0.
- Added deterministic, checked-in-fixture, truth-table, missing-seed/truth-table,
  and WS4 smoke tests plus the fixture/how-to/API docs.
- Verification: 169 passed, 4 skipped; ruff, mypy, Sphinx `-W`, and CI pass.
- Merged as nemora #13 (`d094c01`). P5.4 (`INV-06`, #10) remains open.

## 2026-10-26

### P5.4 sgsR sampling bridge

Closed `INV-06` in Nemora and closed the P5 parent.

- Chose an R bridge over a port: sgsR is GPL (>= 3), Nemora is MIT.
- Added `nemora.sampling.sgsr`, the bundled R bridge, and
  `nemora sampling-sgsr`.
- Returns allocation, sample coordinates, structural strata, strata raster, and
  R/sgsR/terra/sf provenance.
- Deterministic example: 24 samples, seed 42, three strata -> 8/8/8.
- Added reproducibility, seed-required, bad-input, missing-R/sgsR,
  constant-metric, and CLI tests; real bridge tests skip when sgsR is absent.
- Verification: 176 passed, 4 skipped with R 4.3.3 and sgsR 1.5.0; ruff, mypy,
  Sphinx `-W`, and CI pass.
- Merged as nemora #14 (`2e8776c`); P5 children #6, #8, #9, and #10 are closed.

## 2026-10-26

### P119.2 SIBEC addendum and AU-level SI

Closed the P119 follow-up and parent #392.

- Added `femic.sibec.v2` with explicit `source_table` provenance; parsed the
  2014 addendum (224 usable rows) and combined it with the 2013 approximation.
- Added explicit addendum-first source selection and carried the selected source
  into `femic.site-index.reconciliation.v2`.
- Added `femic.site-index.au.v1` for the TSA `03_input` table at the
  analysis-unit/species grain; polygon and AU reports remain separate.
- TSA46 pilot: 148 addendum-selected polygon rows; 21 AUs and 462 AU/species
  rows; leading-species SI 6.3-22.5 m.
- Focused tests: 15 passed; ruff, mypy, Sphinx `-W`, and CI pass. Full suite
  still has the same 42 pre-existing instance/runtime failures and 1778 passes.
- Merged as femic #415 (`b664025`); closeout #416 (`49d541f`); parent #392
  closed.

## 2026-10-26

### P116.3 published EFI cards and annotation

Closed the P116.3 follow-up and parent #369.

- Added two published metadata-only EFI cards:
  - CWH Lorey's height (White et al. 2015; RMSE 2.88 m, bias 0.05 m, 140 plots);
  - southeastern USA loblolly site index (Gopalakrishnan et al. 2019; RMSE 3.8 m,
    bias -0.28 m, 75 FIA plots).
- Both sources are CC BY 4.0. The published models are Random Forest or
  ALS-plus-Landsat, so no linear coefficients were invented.
- Added `femic.efi.pipeline.annotate_attribute_table` and `femic efi annotate`
  with flag/drop/require domain policies.
- Verification: 42 EFI tests pass; ruff, mypy for `femic.efi`, Sphinx `-W`, and
  CI pass. Full suite: 1785 passed, 42 pre-existing instance/runtime failures.
- Merged as femic #418 (`69af694`); closeout #419 (`a3a6152`); parent #369
  closed.

## 2026-10-30

### INV-01 adopted

- Merged `UBC-FRESH/femic#469` (`e9c0031`): `femic.inventory.als.v1` contract,
  model-card reader, `femic lidar inventory`, CHM grid features, published
  boreal transfer cards, and local CWH pilot cards.
- Changed `INV-01` from `shortlisted` to `adopted`.
- The local CWH model is a 14-plot pilot, not a TSA 23 operational model.
  Independent P48/P49 field-plot reconciliation remains required.

## 2026-11-01

### P4.1a registry reconciliation

- Reconciled completed candidates against the live handoffs:
  - `INV-01` complete: P120-P122 BA-only pilot, 2,942,755 rows/pixels, 14.9%
    TSA coverage, strict BA RMSE 8.86 m2/ha; height/volume research-only.
  - `INV-06` complete: nemora #14 (`2e8776c`), sgsR bridge.
  - `DATA-02` complete: nemora #13 (`d094c01`), synthetic fixture.
  - `DATA-04` complete: nemora #12 (`9e7ea9e`), inventory schema/HPS migration.
- Kept `GRO-06` queued because P117.2 (#376) is still open.
- Filtered completed/adopted-out candidates from the generated “Top of the queue”
  table; they remain in workstream and detail sections.
- Verification: `python scripts/check_registry.py` -> OK; `python -m pytest` ->
  13 passed; `python scripts/render_registry.py` regenerated `docs/candidates.md`.

## 2026-11-01

### DEC-02 readiness

- Checked `DEC-02` against the live WS4 state: P54 provides DHI, structure
  habitat, resilience metrics, and report blocks, but there is no recurring
  condition report card.
- Recorded the `ws4.forest_condition.report.v1` schema, indicator fields,
  advisory-alert rules, and the dependency on `DIS-03`.
- The implementation is held because WS4 P82/P83 are active; the planning note
  is `notes/15-dec02-readiness.md`.
- No target issue, branch, or PR was created.

## 2026-11-02

### DEC-02 schema and pilot

- WS4 P90 (#650, PR #653, `6aecccb`) added the report-only
  `ws4.forest_condition.report.v1` schema, Markdown/JSON renderer, fixture,
  docs, and ten tests.
- `DEC-02` remains shortlisted: the UI, real condition source, and `DIS-03`
  alert integration are not part of P90.

## 2026-11-02

### DEC-02 run consumer

- WS4 P91 (#655, PR #657, `a0f395a`) added `build_report_from_accounts` and
  `ws4 condition-card`, deriving review-required cards from `account_values.csv`.
- P90 supplied the card contract; P91 supplies the first run consumer. UI, real
  condition sources, and `DIS-03` alerting remain separate.

## 2026-11-02

### DEC-02 API

- WS4 P92 (#659, PR #661, `4ce820c`) added the read-only
  `/api/runs/{run}/condition-card` endpoint over the P91 account builder.
- `DEC-02` now has schema, CLI, and API consumers; front-end rendering, real
  condition sources, and `DIS-03` alerting remain out of scope.

## 2026-11-02

### DEC-02 UI

- WS4 P93 (#662, PR #669, `5cf5444`) added the Reports-tab condition-card
  panel over the P92 API.
- `DEC-02` now has schema, CLI, API, and browser reporting. A real condition
  source and `DIS-03` alerting remain out of scope; the UI is advisory only.

## 2026-11-02

### DIS-03 readiness

- Audited `DIS-03` against the current WS4 sources. DHI and recovery are static
  overlays; the NSR detector is exploratory and failed its TSA 23 case-control
  test. No real-time condition feed, alert-rule review, or response owner is
  present.
- Marked `DIS-03` deferred rather than queued. It needs an annual/near-real-time
  source, baseline, alert rule, and validation case before implementation.

## 2026-11-02

### DEC-02 complete

- P90-P93 delivered the schema/pilot, account CLI, read-only API, and Reports-tab
  view. The register now marks `DEC-02` complete, with the explicit limit that
  the cards are review-required and advisory, not operational early warning.

## 2026-11-02

### DEC-03 first surface

- WS4 P100 (#670, PR #690, `d14f4ff`) added the condition-card uncertainty column
  and provenance block. This is the first DEC-03 report surface; general report
  badges and uncertainty bands remain shortlisted.

## 2026-11-02

### PLAN-07 complete

- WS4 P101 (#696, PR #698, `91b985c`) added `ws4 storyboard`, a one-page
  Markdown narrative with the account-derived condition card, provenance, and
  limits. The register now marks `PLAN-07` complete; charts/maps/browser
  storyboards remain separate.

## 2026-11-03

### PLAN-08 readiness

- Added `notes/18-plan08-prices.md`: WS4/FHOPS have no shared price-path
  contract, and PLAN-08 depends on DEC-03 provenance. The first step is a
  `prices.v1` table and one named path, not a price-forecasting model.
- PLAN-08 remains shortlisted; no issue, branch, or implementation was created.

## 2026-11-03

### PLAN-08 complete

- WS4 P114 (#749, PR #760) squash-merged to `main` as `0dbc01a` and the branch
  was deleted. Child task #750 and parent #749 are closed.
- The change added the typed `prices.v1` reader in `ws4/prices.py`, the
  `ws4 price-paths` command, a synthetic four-path fixture, and CSV/Markdown/
  provenance outputs with a mandatory `not a forecast` caveat. The table is
  read-only; no objective, constraint, growth, schedule, simulator, or solver
  code changed.
- Local `python scripts/dashboard.py` reported `OVERALL: GREEN` on all seven
  gates before merge, and CI on `3e5c39b` passed every check.
- The register now marks `PLAN-08` complete with a resolution pointing at the
  merge. `notes/18-plan08-prices.md` records the outcome. A real public price
  source with currency/region provenance and a FHOPS consumer remain follow-on.
- Verification after the register change: `python scripts/check_registry.py`
  and `python -m pytest`; `docs/candidates.md` regenerated with
  `python scripts/render_registry.py`.

## 2026-11-03

### CARB-03 first slice adopted

- Audited FHOPS and ws4: FHOPS had salvage harvest systems and
  `salvage_processing_mode`, but no time-dependent degradation or shelf-life
  code; ws4 had carbon pools and `prices.v1`, but no wood-product degradation
  surface.
- Implemented the first bounded `CARB-03` slice in FHOPS P44 (parent #380,
  child #381, PR #383, branch `feature/p44-salvage-degradation`):
  - shared `salvage.decay.v1` curve contract in `fhops.salvage`;
  - the published Prestemon & Holmes (2008) mixed-conifer fire-killed retention
    factors (1.00, 0.99, 0.89, 0.58, 0.22, 0.00 at years 0-5);
  - the Barrette et al. (2015) Canadian boreal product windows;
  - `fhops report salvage-shelf-life`, a read-only block-level report with
    optional caller-supplied `--value-per-m3` and CSV/Markdown output.
- No objective, constraint, heuristic, or solver code changed. No scenario
  schema change. No new coefficients were fitted or extrapolated.
- The curve is a US Pacific Northwest reference, not a BC-specific,
  species-specific, or roadside-storage operational curve. Chagnon et al.
  (2022) remains context only because it does not publish product-value loss
  factors.
- Registry: `CARB-03` moved from `shortlisted` to `adopted` with a resolution
  pointing at P44/PR #383 and the remaining work. Added the Prestemon & Holmes
  and Barrette sources. `DIS-09` and `OPS-03` remain shortlisted; the shared
  module supplies their shelf-life surface, but their scheduling/ws4 work is
  follow-on.
- New note: `notes/19-carb03-salvage-decay.md`.
- Verification in the FHOPS worktree: `ruff format --check src tests`,
  `ruff check src tests`, `mypy src` (191 files), full `pytest`,
  `FHOPS_RUN_FULL_CLI_TESTS=1 pytest tests/test_cli_report_salvage.py`
  (5 passed), `pytest tests/test_salvage_degradation.py` (18 passed), and
  `sphinx-build -b html docs _build/html -W` (clean).
- PR #383 is mergeable and both `lint-test-docs` CI runs passed; `deploy-history`
  was skipped as expected for a pull request.
- Re-ran `python scripts/check_registry.py` (OK) and `python -m pytest`
  (13 passed); regenerated `docs/candidates.md`.

## 2026-11-03

### Created this repository from the workflow seed

- Created IRSS x Silva21 Expansion Mine from the UBC-FRESH dev workflow seed. The agent contract, roadmap, docs skeleton, and validator came from the seed. Every phase is planned, and no parent issues exist yet.

## 2026-11-03

### Public repository seeded and published

- Seeded the public repository from `UBC-FRESH/ubc-fresh-dev-workflow` with the project name
  `IRSS x Silva21 Expansion Mine` and slug `irss-expansion`.
- Preserved the seed's `AGENTS.md`, `ROADMAP.md`, `CHANGE_LOG.md`, contribution guide,
  workflow files, dashboard, validator, issue templates, tests, and docs skeleton.
- Carried over the public-safe planning content:
  - `registry/candidates.yaml` with 62 candidates in nine workstreams;
  - all numbered notes and readiness notes, the notes index, the ADR template, and the
    phase close-out template;
  - the handoff issue bodies, including the superseded carbon drafts;
  - `docs/candidates.md`, `scripts/check_registry.py`, `scripts/render_registry.py`, and
    `tests/test_registry.py`.
- Adapted `README.md`, `ROADMAP.md`, `AGENTS.md`, the docs index, and the API toctree for
  this project. The carried programme history is recorded in `ROADMAP.md` and this log; it
  does not create parent issues in this repository.
- Rewrote scratch paths in the carried notes and handoff index to `$WORKDIR` and
  `$FRESH_SCRATCH` placeholders. No raw data, caches, bytecode, build output, credentials, or
  machine-specific paths are tracked.
- Added `LICENSE`, `CITATION.cff`, and `CODE_OF_CONDUCT.md` so the public repository states
  its licence and community expectations.
- Added `PyYAML` and `types-PyYAML` to the development requirements, and added coverage for
  the carried registry scripts.

Verification:

```bash
python scripts/dashboard.py
# lint, format, types, tests, validator, docs: GREEN

python scripts/check_registry.py
# OK: registry is valid; 62 candidates

python scripts/render_registry.py
# wrote docs/candidates.md; the generated file did not change

python -m pytest -q
# 181 passed; 100% branch coverage of scripts/
```

Limitations:

- The mine remains metadata and abstract level. It is not a full-text systematic review.
- The register records target-repository outcomes as of the source draft; the next audit
  should re-check the live repositories before any handoff.
- Phase 0 is planned. Its parent issue and child issues do not exist yet, so no phase is
  active in this repository.

## 2026-11-03

### Fix the Docs workflow dependency for the registry API

- The Docs workflow installs only `docs/requirements.txt`, while the new API pages autodoc the
  registry scripts. Those scripts import `yaml`, so the documentation build failed on the first
  public push with `ModuleNotFoundError: No module named 'yaml'`.
- Added `PyYAML>=6.0` to `docs/requirements.txt` so the docs and development environments agree.
- Verification: the local docs build passes with warnings as errors, and `python scripts/dashboard.py`
  reports every gate green.

## 2026-11-03

### Docs deploy blocked on the Pages setting

- The Docs workflow now builds the site successfully, including the registry API pages.
- The deploy job fails with a 404 from `actions/deploy-pages` because GitHub Pages is not enabled
  for this repository. The build job itself passes.
- Enabling Pages is a repository settings change, so it needs explicit maintainer approval. No
  workflow, gate, or visibility setting was changed to work around it.

## 2026-11-03

### Activate P0 governance and publish the documentation site

- Created the Phase 0 parent issue #1 (`P0: Bootstrap and publish`) with the `phase` label,
  and child issues #2-#5 for P0.1-P0.4, each labelled `task` and linked as a sub-issue of #1.
- Enabled GitHub Pages with the GitHub Actions source (`build_type: workflow`) for
  `UBC-FRESH/irss-expansion`. The failed Docs deploy at run 41624210028 now passes on re-run,
  and `https://ubc-fresh.github.io/irss-expansion/` returns HTTP 200.
- Set P0 to `active` in `ROADMAP.md` and the tracker map, recording parent issue #1, child issue
  numbers #2-#5, the `feature/p0-bootstrap` branch, and the next step. No implementation branch
  was created.
- Verification: `python scripts/check_workflow.py` reports 0 errors and 0 warnings;
  `python scripts/dashboard.py` reports every gate green (lint, format, types, tests, validator,
  docs); CI passes on the head commit.

## 2026-11-03

### P0 bootstrap complete; pull request #6 queued

- Adapted `README.md` so Phase 0 is active with parent issue #1 and child issues #2-#5, and
  replaced the stale "create the parent issue" next action with the review-and-merge step.
  `AGENTS.md` already described this project and its public boundary; it needed no rewrite.
- Verified the carried public-safe material: `registry/candidates.yaml` (62 candidates),
  the numbered and readiness notes, the handoff bodies and superseded drafts, the generated
  register, the registry and workflow scripts, and their tests. `python scripts/render_registry.py`
  reproduces `docs/candidates.md` with no diff.
- Ran the registry-specific checks: `python scripts/check_registry.py` reports `OK: registry is
  valid; 62 candidates`; `python -m pytest -q` reports 181 passed with 100% branch coverage of
  `scripts/`.
- Ran the full dashboard: `python scripts/dashboard.py` reports lint, format, types, tests,
  validator, and docs all GREEN, with `OVERALL: GREEN. Every gate passed.`
- Ran `python scripts/check_workflow.py`: 0 errors and 0 warnings, including the public-safety
  scan. `git ls-files` contains no caches, build output, bytecode, coverage records, or runtime
  files, and no personal paths were found.
- Confirmed the public remote: `gh repo view` reports `UBC-FRESH/irss-expansion`, `PUBLIC`,
  default branch `main`. `gh api repos/UBC-FRESH/irss-expansion/pages` reports
  `build_type: workflow` and `html_url: https://ubc-fresh.github.io/irss-expansion/`; the URL
  returns HTTP 200. CI run 41696981546 and Docs run 41696981559 pass on `main` at `23cca3e`.
- Opened pull request #6 (`feature/p0-bootstrap` into `main`) with `Part of #1`, and recorded
  P0 as `pr-open` in `ROADMAP.md`. Added the close-out report at
  `notes/reports/p0-bootstrap.md`.
- The pull request is queued for maintainer approval. It is not merged, no branch was deleted,
  no issue was closed, and no accepted history was rewritten. Phase 1 remains `planned`.

## 2026-11-03

### P0 close-out approved; Phase 0 marked complete

- The maintainer approved the P0 close-out on 2026-11-03 and authorized the squash merge of pull
  request #6, deletion of `feature/p0-bootstrap`, closure of issues #1-#5, and launch of P1.
- `ROADMAP.md` marks P0 `complete`, and `README.md` records the completed phase and the P1 launch
  point. The source draft history remains unchanged.
- `notes/reports/p0-bootstrap.md` records the approval and the merge sequence.
- Verification before the merge: `python scripts/check_workflow.py`, `python scripts/dashboard.py`,
  `python scripts/check_registry.py`, and `python -m pytest -q` all pass on the merge head.
- Phase 1 starts from the merged `main`; no candidate is queued and no target-repository issue,
  branch, or pull request is created by this close-out.

## 2026-11-03

### P1.1 activate Phase 1 and confirm the scope rule

- Created `feature/p1-scope-design` from the merged `main` at `aacd102` and activated P1 under
  parent issue #7, with child issues #8-#11 and status `active` in `ROADMAP.md`.
- Confirmed the scope rule in `README.md`: candidates must consume an existing provincial product,
  published model, dataset, reference implementation, or partner coefficient set with provenance
  and a validation boundary. New general models remain out of scope.
- Reviewed `notes/06-out-of-scope.md`: every deferred and screened-out entry keeps its revisit
  trigger. No item was added, removed, or re-scored.
- Linked the out-of-scope list directly from the scope rule in `README.md`, the only wording
  change in this task.
- Corrected the Silva21 extension-note count from 14 to 16 notes across 15 volumes, because
  Volume 6 is published as two issues.
- Verification: `python scripts/check_workflow.py` and `python scripts/dashboard.py` pass.

## 2026-11-03

### P1.2 review the source inventory and publication signals

- Re-fetched all 22 public source URLs in `notes/00-source-inventory.md`; every one returned
  HTTP 200.
- Re-derived the carried counts from the current pages: 493 IRSS publication records
  (2004-2023), 47 Silva21 project pages, 12 hubs, 65 DOI-linked scientific publications, and
  62 registry candidates.
- Corrected the Silva21 extension-note count from 14 to 16 notes across 15 volumes. The source
  page lists volumes 1-14 and publishes Volume 6 as two issues; the earlier figure counted
  volume numbers.
- Checked the 44 candidate references in `notes/02-publication-signals.md` against
  `registry/candidates.yaml`; every ID exists and none was renamed or removed.
- Fixed the notes index gap: `notes/README.md` now lists the readiness notes
  `15-dec02-readiness.md` and `16-dis03-readiness.md`.
- No source was re-mined, no candidate evidence changed, and no score changed.
- Verification: `python scripts/check_workflow.py`, `python scripts/check_registry.py`, and
  `python scripts/dashboard.py` pass.

## 2026-11-03

### P1.3 record the design-decision outcome

- Decided that P1 produced no new design decision. The scope rule, the out-of-scope list, and the
  scoring rubric were confirmed, not changed, so no numbered ADR was created.
- Recorded the no-decision outcome and its reasoning in `notes/reports/p1-scope-design.md`.
  A future boundary or formula change must add an ADR under `notes/adr/` with status `accepted`
  or `deferred`.
- Left the ADR template and every accepted contract-wave decision unchanged.
- Verification: `python scripts/check_workflow.py` and `python scripts/dashboard.py` pass.

## 2026-11-03

### P1.4 confirm the scoring rubric

- Confirmed the formula `priority = (impact * readiness) / (effort_points * risk)` against
  `priority_score` in `scripts/check_registry.py`, including the S/M/L/XL effort map and
  two-decimal rounding.
- Checked all 13 rows of the first-wave table against the validator output: every ID, score, and
  effort code matches. The registry wave counts are 2 in wave 0, 13 in wave 1, 25 in wave 2, and
  22 in wave 3.
- Confirmed the impact, readiness, effort, and risk rubrics and the wave logic are unchanged. A
  wave remains a dependency and sequencing judgement, not a score threshold.
- Kept readiness described as an integration judgement, not an author-confirmed science claim.
- No candidate was re-scored, no wave changed, and the formula was not altered.
- Verification: `python scripts/check_registry.py`, `python scripts/check_workflow.py`, and
  `python scripts/dashboard.py` pass.

## 2026-11-03

### P1 scope and design complete; pull request #12 queued

- Opened pull request #12 (`feature/p1-scope-design` into `main`) with `Part of #7`, and set P1
  to `pr-open` in `ROADMAP.md` and the README status.
- Confirmed every P1 acceptance criterion and recorded the evidence in
  `notes/reports/p1-scope-design.md`.
- Fixed the notes index gap so the readiness notes 15 and 16 are listed, and refreshed the
  source-inventory and publication-signal review dates.
- No new ADR: the scope rule, out-of-scope list, and scoring rubric were confirmed, not changed.
- No candidate was re-scored, no source was re-mined, and no target-repository issue, branch, or
  pull request was created.
- The pull request is queued for maintainer approval. It is not merged, no branch was deleted,
  and no P1 issue was closed.
- Verification: `python scripts/dashboard.py` reports all six gates GREEN;
  `python scripts/check_workflow.py` reports 0 errors and 0 warnings; `python scripts/check_registry.py`
  reports 62 valid candidates; `python scripts/render_registry.py` produces no diff.

## 2026-11-03

### P1 close-out approved; Phase 1 marked complete

- The maintainer approved the P1 close-out on 2026-11-03 and authorized the squash merge of pull
  request #12, deletion of `feature/p1-scope-design`, closure of issues #7-#11, and creation of the
  P2 governance issues.
- Squash-merged pull request #12 to `main` at `2b4620d` (`P1: confirm scope, sources, design
  decision, and scoring`). The branch `feature/p1-scope-design` was deleted after the merge.
- Closed parent issue #7 and child issues #8-#11 with closeout comments that cite `2b4620d` and the
  gate evidence.
- `ROADMAP.md` marks P1 `complete` and records P2 parent issue #13 with child issues #14-#17.
  `README.md` records the completed phase and the P2 activation gate.
- Created P2 governance only: parent issue #13 (`P2: Contracts and prototype`) with child issues
  #14 P2.1, #15 P2.2, #16 P2.3, and #17 P2.4, each linked as a sub-issue and labelled `task`.
  P2 remains `planned`; no P2 branch, commit, or implementation exists.
- Verification on the merged `main` with the close-out edits: `python scripts/check_workflow.py`
  reports 0 errors and 0 warnings; `python scripts/dashboard.py` reports all six gates GREEN with
  `OVERALL: GREEN`; `python scripts/check_registry.py` reports a valid registry with 62 candidates;
  `python scripts/render_registry.py` produces no diff.
- CI run 41710569721 and Docs run 41710569637 pass on `main` at `2b4620d`; the Pages site
  `https://ubc-fresh.github.io/irss-expansion/` returns HTTP 200.
- No new ADR, no candidate was re-scored, no source was re-mined, and no target-repository issue,
  branch, or pull request was created.

## 2026-11-03

### P2.1 activate Phase 2 and audit the contract-wave records

- Created `feature/p2-contracts-prototype` from the merged `main` at `d991dea`
  and set P2 to `active` under parent issue #13 in `ROADMAP.md` and `README.md`.
- Added `notes/17-p2-contract-audit.md`, which audits the twelve contract-wave
  candidates (`GRO-01`, `DIS-01`, `DEC-04`, `DATA-01`, `CARB-01`, `BIO-01`,
  `BIO-02`, `PLAN-03`, `DATA-02`, `DATA-04`, `INV-06`, `GRO-06`) against the
  live target issues, pull requests, and merge commits.
- Result: eleven candidates are complete or adopted with merged evidence, and
  `GRO-06` is open. No candidate has a missing target record.
- Recorded six drift items, including the ws4 carbon phase label (`P51` carried,
  live `P58`), the `DEC-04` follow-up merge (#418), the `BIO-02` real-data
  follow-up (#484), and stale open/active wording in `README.md` and
  `handoffs/README.md`.
- Updated the stale carbon references from ws4 P51 to P58 in `README.md` and
  the affected notes and handoff index. The audit note preserves the carried
  label and the reason for the correction.
- No target repository was changed; no candidate was re-scored or retired.

Verification:

```bash
python scripts/check_workflow.py
python scripts/check_registry.py
python scripts/dashboard.py
```

`check_workflow.py` reports 0 errors and 0 warnings; `check_registry.py` reports
62 valid candidates; the dashboard reports all six gates GREEN.
