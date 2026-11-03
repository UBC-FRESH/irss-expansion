# First-wave briefs

The first wave is the contract-and-quick-win layer. Each brief is deliberately
small enough to become one parent issue in the target repo. If a brief cannot
name a consumer, an acceptance test, and a public source, it is not ready.

**Status note (2026-10-25).** `CARB-01` is now **adopted** by live work:
FEMIC P115 (`#361`, forest carbon domain) and ws4 P58 (`#357`, carbon
accounting; the carried label was P51). Its brief is retained for context and should not be opened as a
parallel issue.

Created issues:

| Candidate | Issue |
| --- | --- |
| `GRO-01` | [femic #370](https://github.com/UBC-FRESH/femic/issues/370) |
| `DIS-01` | [femic #371](https://github.com/UBC-FRESH/femic/issues/371) |
| `DEC-04` | [femic #372](https://github.com/UBC-FRESH/femic/issues/372) |
| `DATA-01` | [nemora #6](https://github.com/UBC-FRESH/nemora/issues/6) |
| `CARB-01` | [femic #361](https://github.com/UBC-FRESH/femic/issues/361), [ws4 #357](https://github.com/UBC-FRESH/ws4/issues/357) (adopted) |
| `INV-04` | [femic #375](https://github.com/UBC-FRESH/femic/issues/375) |
| `GRO-06` | [femic #376](https://github.com/UBC-FRESH/femic/issues/376) |
| `DATA-02` | [nemora #8](https://github.com/UBC-FRESH/nemora/issues/8) |
| `DATA-04` | [nemora #9](https://github.com/UBC-FRESH/nemora/issues/9) |
| `INV-06` | [nemora #10](https://github.com/UBC-FRESH/nemora/issues/10) |
| `BIO-01` | [ws4 #376](https://github.com/UBC-FRESH/ws4/issues/376) |
| `BIO-02` | [ws4 #377](https://github.com/UBC-FRESH/ws4/issues/377) |
| `PLAN-03` | [ws4 #378](https://github.com/UBC-FRESH/ws4/issues/378) |

The recommended starting order is `GRO-01`, `DIS-01`, `DEC-04`, `DATA-01`,
then the rest. The first four are load-bearing contracts. `CARB-01` is adopted
by live carbon work and is not a parallel opener.

---

## `GRO-01` Climate data contract and GCM ensemble

**Why now.** Every climate-sensitive candidate depends on a shared climate
table. Building them separately would produce three incompatible climate
adapters.

**Scope.** Define `climate.v1`: a tidy table keyed by AOI, variable, year,
scenario, GCM, and source, with units, downscaling method, and provenance. Add
an adapter for ClimateNA/SilvR21 outputs. Do not build a climate model or a GCM
ensemble selector UI.

**Deliverable.**

- A JSON schema and a small sample table for one AOI.
- A reader in `nemora` or `femic` that validates units and provenance.
- A short note on scenario/GCM selection and the meaning of the ensemble.

**Insertion point.** `femic` data preparation or a shared `fresh-contracts`
module. The first consumer should be `GRO-02` or `BIO-03`.

**Acceptance test.** The schema rejects a missing scenario, a negative
variance, or an unknown unit. A round-trip of the sample table produces an
identical table. A second AOI with a different GCM ensemble loads without
code changes.

**Effort / risk.** S / low. The science is mature; the risk is scope creep into
climate modelling.

**Sources.** Silva21 climate data and SilvR21; Wotherspoon et al. 2022 and 2023.

---

## `DIS-01` Shared disturbance event schema

**Why now.** FEMIC, ws4, and FHOPS each need to know what happened, where, when,
how severe, and how confident. Without a shared record, every integration
invents its own event table.

**Scope.** Define `disturbance.v1`: event id, type (fire, insect, drought, wind,
partial mortality, harvest, salvage), year, geometry or fragment ids, severity,
attribution, confidence, source, and provenance. Include a small controlled
vocabulary and a severity scale that can carry both categorical and continuous
values.

**Deliverable.**

- A JSON schema and a validator.
- Two example events (a fire and an NSR event).
- One ws4 consumer that reads an event and reports it in a scenario.

**Insertion point.** `ws4/model/schema.py` for the consumer; a shared contracts
package for the schema.

**Acceptance test.** The validator rejects an event with no type, no year, or a
severity outside the declared scale. ws4 reads the two examples and reports the
correct year and type. A round-trip through JSON preserves provenance.

**Effort / risk.** S / low. The risk is schema overreach; keep the first
version small and additive.

**Sources.** IRSS disturbance research; Silva21 OB 5c; Brown et al. 2025.

---

## `DEC-04` EFI model card and applicability metadata

**Why now.** FEMIC already ships a LiDAR product bundle with sensor metadata.
What is missing is the **inventory model** metadata: what the model predicts,
what it was trained on, how accurate it is, and where it applies.

**Scope.** Define `efi.model.v1`: model id, version, target attribute, unit,
predictors, training data, validation design, RMSE/bias, applicability domain,
and licence. Do not duplicate the sensor bundle manifest.

**Deliverable.**

- A JSON schema and two model cards from real published or project models.
- A validator that checks required accuracy fields and applicability bounds.
- A FEMIC reader that attaches a model card to an ALS-derived attribute table.

**Insertion point.** `femic/lidar` product application layer, or a shared
contracts package consumed by FEMIC and Nemora.

**Acceptance test.** A model card missing an applicability domain or an accuracy
field fails validation. Two cards with different training regions can coexist.
The FEMIC reader preserves the model id and RMSE on every attribute row.

**Effort / risk.** S / low. The risk is over-specific fields; keep the schema
extensible.

**Sources.** IRSS LiDAR/EFI research; Goodbody et al. 2024; FEMIC LiDAR bundle
contract.

---

## `DATA-01` Distribution fitting and uncertainty propagation for curves

**Why now.** The ecosystem's reports imply a precision that the underlying
curves do not support. This is the cheapest credibility improvement available.

**Scope.** Fit a distribution to curve residuals or parameter uncertainty, emit
a confidence band, and propagate it into one ws4 report. Do not attempt a full
Bayesian treatment in the first version.

**Deliverable.**

- A `nemora.fit` workflow for one curve family.
- A 90% band in a ws4 report or CSV.
- A coverage check on a holdout set.

**Insertion point.** `nemora/fit` and `nemora/distributions`; `ws4/report.py`
for the band.

**Acceptance test.** The fitted distribution reproduces the observed residual
quantiles within a stated tolerance. The report band contains the point
estimate. A holdout coverage check is recorded, even if it fails.

**Effort / risk.** M / low. The risk is mis-specified distributions and users
ignoring the band.

**Sources.** Nemora fit/distributions; IRSS growth and yield data.

---

## `CARB-01` Carbon account v0 across ws3 and ws4 (adopted)

**Why now.** ws3 already has a CBM linkage and avoided-fire/avoided-harvest
examples. The gap is a shared account contract and a ws4 output, not a new
carbon model.

**Scope.** Define the account fields (stand biomass, harvested biomass, product
pool, emissions, decay) and emit them from one ws4 scenario. Reuse the ws3 CBM
path for the product and decay boundaries. Label every conversion factor.

**Deliverable.**

- A carbon account table and a report block.
- A comparison with the ws3 CBM path on a compatible scenario.
- A boundary note: what is included and what is not.

**Insertion point.** `ws4/report.py` and the account tables; `ws3/forest.py`
and `integration.py` for the CBM comparison.

**Acceptance test.** The stand carbon equals biomass times the declared carbon
fraction. The ws3 and ws4 paths agree within a stated tolerance on the shared
boundary. Every factor has a source and a version.

**Effort / risk.** M / moderate. The risk is boundary disagreement between ws3
and ws4, and false precision.

**Sources.** Tompalski et al. 2024; ws3 CBM linkage; IRSS carbon research.

---

## `BIO-01` Dynamic Habitat Indices as biodiversity layers

**Why now.** DHI is a public, mature product that gives the ecosystem a
biodiversity layer without new science. It is the fastest way to make habitat
visible in a scenario.

**Scope.** Ingest one DHI product, attach it to the AOI, and report its
trajectory under two schedules. Do not claim it is a species-specific habitat
model.

**Deliverable.**

- A DHI ingest adapter and a landscape account.
- A two-schedule comparison.
- A caveat note on scale and interpretation.

**Insertion point.** `ws4` account layer and web map; `ws3` for strategic
comparison.

**Acceptance test.** The layer covers the AOI without unexpected NaNs. The
account is reproducible from the source raster and the schedule. The caveat
note is present in the report.

**Effort / risk.** S / low. The risk is over-interpretation.

**Sources.** IRSS biodiversity and DHI publications.

---

## `INV-06` Structurally guided sampling with sgsR

**Why now.** A reference implementation exists. Wrapping it is cheaper than
reimplementing it and gives Nemora a real sampling-design capability.

**Scope.** Wrap or port the sgsR workflow into `nemora.sampling`, with a CLI and
one worked example. Do not build a new sampling theory.

**Deliverable.**

- A `nemora sampling` command or Python API.
- A worked example with a structural metric and a plot allocation.
- A reproducibility test.

**Insertion point.** `nemora/sampling`; `femic` for inventory QA.

**Acceptance test.** The same inputs produce the same allocation. The output
includes the structural strata and the plot count. A deliberately bad input
(e.g., a constant structure metric) produces a clear error or warning.

**Effort / risk.** S / low. The risk is R/Python bridge maintenance.

**Sources.** Goodbody et al. 2023; Silva21 OB 5a.

---

## `INV-04` Site index and potential height from ALS

**Why now.** FEMIC already has the LiDAR bundle. Turning canopy height into a
site-index layer is a small adapter that improves every curve decision.

**Scope.** Apply a published species-specific SI/potential-height relationship
to FEMIC LiDAR metrics and add an optional `si_als` attribute with provenance.
Backtest against the current SI assignment on one instance.

**Deliverable.**

- An SI adapter and a provenance record.
- A backtest report: bias, RMSE, and where the assignment changes.
- A note on species and age limits.

**Insertion point.** `femic` inventory/curve stage.

**Acceptance test.** The layer covers the pilot AOI. The backtest reports a
quantified difference from the current SI. A species outside the calibrated set
is rejected or flagged, not silently predicted.

**Effort / risk.** M / moderate. The risk is species-specific equations and
young-stand height bias.

**Sources.** Tompalski et al. 2022; Gavilan-Acuna et al. 2022; IRSS LiDAR.

---

## `PLAN-03` Spatial resilience metrics for estate models

**Why now.** ws4 already has patch and spread accounts. A small set of
resilience-oriented metrics turns those accounts into a story a planner can use.

**Scope.** Implement three metrics: a connectivity or barrier metric, an
age-class diversity metric, and a patch-size or fragmentation metric. Report
them; do not put them in the objective yet.

**Deliverable.**

- Three report accounts with definitions and units.
- A comparison of two existing schedules.
- A property test for identical schedules.

**Insertion point.** `ws4/patch/` and `ws4/report.py`.

**Acceptance test.** Identical schedules produce identical metrics. The metrics
change in the expected direction for a deliberately fragmented schedule. The
definitions and units are in the report.

**Effort / risk.** M / low. The risk is metric redundancy and false precision.

**Sources.** IRSS landscape pattern research; ws4 patch/spread accounts.

---

## `DATA-02` Synthetic forest and stand generator for tests and scenarios

**Why now.** Nemora synthesis already generates tessellations, stands, and
stems. Using it to build ws4/FHOPS fixtures makes edge cases and scale testable.

**Scope.** Generate one synthetic landscape with known volume, age, and
structure, export it in the ws4 build format, and run it through build and
simulate. Do not build a new generator.

**Deliverable.**

- A synthetic landscape fixture with known properties.
- A ws4 build/simulate smoke test.
- A short note on realism and limits.

**Insertion point.** `nemora/synthesis`; `ws4` test fixtures.

**Acceptance test.** The known volume is reproduced within a stated tolerance
after build. The simulation runs. The fixture is deterministic from a seed.

**Effort / risk.** M / low. The risk is false confidence in synthetic realism.

**Sources.** Nemora synthesis; IRSS LiDAR sampling.

---

## `GRO-06` Biomass yield curves from time-series remote sensing

**Why now.** Carbon and biomass are user-visible gaps, and a published curve
family already exists. The work is a curve family and a conversion, not a new
remote-sensing study.

**Scope.** Add a biomass curve table and a carbon conversion to one FEMIC
instance. Keep the volume curve as the primary output and the biomass curve as
a parallel family with provenance.

**Deliverable.**

- A biomass curve family and a conversion report.
- A comparison with the volume curve.
- A provenance record for the source and species.

**Insertion point.** `femic` curve stage and export.

**Acceptance test.** Biomass is monotonic where the source relationship is
monotonic. The conversion to carbon uses a declared fraction. The volume and
biomass curves can be selected independently.

**Effort / risk.** M / moderate. The risk is allometry and belowground omission.

**Sources.** Tompalski et al. 2024; IRSS carbon.

---

## `BIO-02` Forest structure habitat index from ALS

**Why now.** FEMIC has the canopy structure; a published index turns it into a
habitat account. This is a direct bridge from LiDAR to a non-timber value.

**Scope.** Implement the published structure habitat index on one ALS-covered
landscape, report it as a stand and landscape account, and compare it with DHI.
Do not claim it is a species-specific habitat model.

**Deliverable.**

- An index implementation and a report account.
- A comparison with DHI.
- A caveat note on index validity.

**Insertion point.** `ws4` account layer; `femic` LiDAR products.

**Acceptance test.** The index is computable wherever the required metrics
exist. The comparison with DHI is reported, including disagreement. The caveat
note is present.

**Effort / risk.** M / moderate. The risk is index validity and metric
availability.

**Sources.** IRSS structure habitat index publications; Silva21 OB 5b.

---

## `DATA-04` Open inventory ingest harmonization

**Why now.** FAIB/FIA/HPS parsing exists in more than one place. Converging on a
shared schema removes duplicate work and makes the other data candidates
cheaper.

**Scope.** Publish the shared tidy schema and migrate one ingest path, with
byte-level regression fixtures. Do not migrate all sources at once.

**Deliverable.**

- A shared schema and a migration note.
- One migrated ingest path.
- Regression fixtures and a nightly check.

**Insertion point.** `nemora/ingest`; `femic` data preparation.

**Acceptance test.** The migrated path reproduces the existing output on the
fixture. The schema rejects a missing key. The nightly ingest still passes.

**Effort / risk.** M / low. The risk is upstream schema drift and breaking
existing scripts.

**Sources.** Nemora ingest; FEMIC data preparation.
