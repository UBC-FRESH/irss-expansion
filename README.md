# IRSS x Silva21 Expansion Mine

A public-safe planning mine of IRSS and Silva21 outputs, screened against the FRESH
forest modelling stack, with a prioritised integration queue and traceable public
provenance.

The project mines the public output of the UBC Integrated Remote Sensing Studio
(IRSS) and the Silva21 research program, screens it against the current FRESH
software stack (`femic`, `ws3`, `ws4`, `fhops`, `nemora`), and maintains a
prioritised queue of candidate integrations.

- Sources mined: <https://irsslab.forestry.ubc.ca> and <https://www.silva21.com>
- Registry: [`registry/candidates.yaml`](registry/candidates.yaml)
- Browsable register: [`docs/candidates.md`](docs/candidates.md)
- Programme plan: [`ROADMAP.md`](ROADMAP.md)
- Working contract: [`AGENTS.md`](AGENTS.md)
- Change history: [`CHANGE_LOG.md`](CHANGE_LOG.md)
- Handoff drafts: [`handoffs/README.md`](handoffs/README.md)
- Notes index: [`notes/README.md`](notes/README.md)

## Status

Phase 0 (bootstrap and publish) is complete under parent issue
[#1](https://github.com/UBC-FRESH/irss-expansion/issues/1). Tasks
[#2](https://github.com/UBC-FRESH/irss-expansion/issues/2)-[#5](https://github.com/UBC-FRESH/irss-expansion/issues/5)
were completed on `feature/p0-bootstrap` and squash-merged in pull request
[#6](https://github.com/UBC-FRESH/irss-expansion/pull/6). `ROADMAP.md` lists the
phases, and the GitHub issues carry the live status. The planning content was
carried over from the source draft, whose own programme phases (mine, contract
wave, model integration, and review) are recorded in `ROADMAP.md` and
`CHANGE_LOG.md`. Carrying that history does not create parent issues in this
repository.

Phase 1 (scope and design) is complete under parent issue
[#7](https://github.com/UBC-FRESH/irss-expansion/issues/7), with tasks
[#8](https://github.com/UBC-FRESH/irss-expansion/issues/8)-[#11](https://github.com/UBC-FRESH/irss-expansion/issues/11)
completed on `feature/p1-scope-design` and squash-merged in pull request
[#12](https://github.com/UBC-FRESH/irss-expansion/pull/12). It confirmed the
carried scope and scoring decisions without re-mining the sources.

Phase 2 (contracts and prototype) is active under parent issue
[#13](https://github.com/UBC-FRESH/irss-expansion/issues/13), with tasks
[#14](https://github.com/UBC-FRESH/irss-expansion/issues/14)-[#17](https://github.com/UBC-FRESH/irss-expansion/issues/17)
running on `feature/p2-contracts-prototype`. P2.1 audits the twelve contract-wave
candidates against the live target repositories without changing them.

## How this project works

This project follows the UBC-FRESH dev workflow. Work is planned as phases, tasks,
and subtasks in `ROADMAP.md`, mirrored in GitHub issues, and recorded in
`CHANGE_LOG.md`. The agent operating contract is in `AGENTS.md`. Read `AGENTS.md`,
then `ROADMAP.md`, before you change anything.

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/dashboard.py
```

Validate the registry and print the ranking:

```bash
python scripts/check_registry.py
```

Regenerate the browsable register after editing the YAML:

```bash
python scripts/render_registry.py
```

Run the workflow validator or the tests on their own:

```bash
python scripts/check_workflow.py
python -m pytest
```

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Operating contract for coding agents |
| `ROADMAP.md` | Plan of record and issue tracker map |
| `CHANGE_LOG.md` | Dated narrative of changes |
| `registry/candidates.yaml` | Machine-readable candidate queue, the source of truth |
| `docs/candidates.md` | Generated browsable register; do not edit by hand |
| `notes/` | Source inventory, theme map, gap analysis, readiness notes, ADRs, and plans |
| `handoffs/` | Reviewable issue bodies for the cross-repo handoff |
| `docs/` | Documentation site and the generated register |
| `scripts/check_workflow.py` | Workflow validator |
| `scripts/check_registry.py` | Registry validator and ranking |
| `scripts/render_registry.py` | Register renderer |
| `scripts/dashboard.py` | The green dashboard |
| `tests/` | pytest suite, including a check that the planning surfaces pass the validator |

## The finding in one paragraph

IRSS and Silva21 have spent roughly two decades building the layer FRESH is
thinnest in: **environmental intelligence**. They have the measurement science
(LiDAR/EFI, optical time series, drone and mobile sensors), the dynamics
(climate-sensitive growth and mortality, disturbance and recovery), and the
values (carbon, habitat, resilience, assisted migration). FRESH has strong
decision engines (FEMIC, ws3, ws4, FHOPS) and an emerging analytics substrate
(Nemora), but it mostly consumes static inventory and deterministic yield
curves. The highest-leverage programme is therefore **not** to port individual
papers. It is to define a small set of shared contracts (climate, disturbance,
LiDAR/EFI metadata, carbon/habitat accounts) and then wire IRSS/Silva21 methods
into the existing engines as adapters. That is what this register queues.

## Scope rule

This is a **software integration programme for applied forest management**, not
a remote-sensing or modelling research programme.

A candidate is in scope only when it consumes an existing provincial product,
published model, dataset, reference implementation, or partner-supplied
coefficient set with clear provenance and a validation boundary. If a candidate
requires deriving a new general growth, height, site-index, carbon, disturbance,
or remote-sensing model, it is out of scope. Use the existing BC products.

Examples of existing products that should be consumed, not reinvented:

- **VRI** for polygon site index and inventory attributes;
- **VDYP** for the SI and yield curves FEMIC already uses;
- **SIBEC** for BEC/site-series/species SI estimates and standard errors;
- **LidarBC** for open LiDAR products;
- **NTEMS / HLS / Landsat** for existing change and recovery products.

A useful paper is not enough. The question is whether FRESH can integrate its
output without pretending to have produced new science.

The deferred and screened-out material, with a revisit trigger for each item,
is in [`notes/06-out-of-scope.md`](notes/06-out-of-scope.md).

## What was mined

| Source | What was reviewed | Scale |
| --- | --- | --- |
| IRSS research pages | 11 research themes, project narratives, methods | NTEMS, BioSpace, biodiversity, disturbance/habitat, carbon, data fusion, MPB, LiDAR, urban, mobile RS, water |
| IRSS publications page | Titles, years, journals, DOIs as rendered | 493 records, 2004-2023 |
| Silva21 projects | 47 project pages across the AD, AN, and OB themes | 38 funded projects, 12 hubs, 5 universities, 50 collaborators |
| Silva21 publications | 2022-2026 scientific papers and extension notes | 50+ papers and 16 extension notes across 15 volumes |
| Silva21 data/climate | Data portal, ClimateNA/SilvR21, hub climate products | 12 hub climate packages; Globus-hosted LiDAR and spatial data |

The mining was **metadata and abstract level**, not a full-text systematic
review. Every candidate cites the public source that motivated it. Readiness is
a judgement about integration cost, not a claim that the underlying science is
settled. See [`notes/00-source-inventory.md`](notes/00-source-inventory.md) for
the method and its limits.

## The queue at a glance

62 candidates in nine workstreams. Thirteen are in the first wave; most are
short, contract-shaped moves that unlock later model work.

| Workstream | Code | Candidates | First-wave focus |
| --- | --- | ---: | --- |
| Inventory, LiDAR, EFI | `INV` | 10 | site index, sgsR sampling |
| Growth, yield, climate | `GRO` | 9 | climate contract, biomass curves |
| Disturbance, risk, recovery | `DIS` | 9 | event schema |
| Landscape planning, resilience | `PLAN` | 8 | spatial resilience metrics |
| Carbon and biomass | `CARB` | 4 | carbon account v0 |
| Biodiversity and habitat | `BIO` | 5 | DHI, structure habitat index |
| Harvesting operations, salvage | `OPS` | 6 | none in wave 1 |
| Data, uncertainty, synthetic | `DATA` | 6 | uncertainty propagation, synthetic forests, ingest |
| Decision support, provenance | `DEC` | 5 | EFI model card |

### Recommended starting set

`CARB-01` is already in flight under live carbon phases (FEMIC P115 and ws4
P58), so it has moved from "recommended" to "adopted". The remaining starting
set is four contracts plus the first quick win:

1. **`GRO-01` Climate data contract and GCM ensemble.** A canonical climate
   table and a ClimateNA/SilvR21 adapter. Everything climate-sensitive depends
   on it, and it is a small, low-risk contract.
2. **`DIS-01` Shared disturbance event schema.** One record type for fire,
   insect, drought, wind, partial mortality, and harvest. It lets FEMIC data,
   ws4 scenarios, and FHOPS operations talk about the same event.
3. **`DEC-04` EFI model card and applicability metadata.** Training data,
   predictors, accuracy, applicability domain, and version. FEMIC already carries
   a sensor-product manifest; this is the missing inventory-model contract.
4. **`DATA-01` Distribution fitting and uncertainty propagation.** Turn
   deterministic curves into distributions with defensible bands. This is the
   cheapest credibility win in the ecosystem.
5. **`BIO-01` Dynamic Habitat Indices.** A public, mature biodiversity layer
   and a quick account that makes the environmental layer visible. (`CARB-01`
   is adopted by FEMIC P115 and ws4 P58; see `notes/10-repo-state-check.md`.)

The full first-wave table, with effort and dependencies, is in
[`notes/05-first-wave.md`](notes/05-first-wave.md).

## Where the candidates land

| FRESH repo | Insertion points | Representative candidates |
| --- | --- | --- |
| `femic` | inventory adapters, AU/strata attributes, curve modifiers, disturbance/recovery attributes, climate provenance | `INV-01`, `INV-04`, `INV-05`, `GRO-02`, `GRO-03`, `GRO-06`, `DIS-02`, `DIS-04` |
| `ws4` | feature/product accounts, transition rules, objective and constraints, spatial accounts, web layers | `PLAN-01`, `PLAN-02`, `PLAN-03`, `PLAN-05`, `CARB-01`, `CARB-02`, `BIO-01`, `BIO-02`, `DEC-01` |
| `ws3` | strategic scenarios, transitions, multi-model comparison | `PLAN-01`, `CARB-01`, `BIO-01`, `GRO-01` |
| `fhops` | treatment prescriptions, salvage, fuel reduction, road access, plan-versus-actual | `OPS-01`, `OPS-02`, `OPS-03`, `OPS-05`, `DIS-09`, `CARB-03` |
| `nemora` | fitting, sampling, synthesis, simulation, ingest, imputation | `DATA-01`, `DATA-02`, `DATA-03`, `DATA-04`, `DATA-05`, `INV-06`, `BIO-03` |
| cross-repo | shared schemas, provenance, validation network | `GRO-01`, `DIS-01`, `DEC-03`, `DEC-04`, `DEC-05` |

## Working with the register

The registry is the source of truth. `docs/candidates.md` is generated; do not
edit it by hand. Candidate status changes (`candidate` -> `shortlisted` ->
`queued`) should be recorded in the registry and in `CHANGE_LOG.md`.

```bash
python scripts/check_registry.py
python scripts/render_registry.py
python -m pytest
```

## Handoff drafts and created issues

All wave-1 issues were created on 2026-10-25:

- `femic`: **P116** [#369](https://github.com/UBC-FRESH/femic/issues/369) with
  [#370](https://github.com/UBC-FRESH/femic/issues/370) (merged as `9e16be9`),
  [#371](https://github.com/UBC-FRESH/femic/issues/371) (closed; ws4 consumer
  merged as `5ea4a05`), and
  [#372](https://github.com/UBC-FRESH/femic/issues/372) (closed; contract merged
  `f833ed9`, cards and annotation merged as `69af694`); **P117**
  [#374](https://github.com/UBC-FRESH/femic/issues/374) with
  [#375](https://github.com/UBC-FRESH/femic/issues/375) and
  [#376](https://github.com/UBC-FRESH/femic/issues/376).
- `nemora`: **P5** [#7](https://github.com/UBC-FRESH/nemora/issues/7) with
  [#6](https://github.com/UBC-FRESH/nemora/issues/6),
  [#8](https://github.com/UBC-FRESH/nemora/issues/8),
  [#9](https://github.com/UBC-FRESH/nemora/issues/9), and
  [#10](https://github.com/UBC-FRESH/nemora/issues/10).
- `ws4`: **P54** [#375](https://github.com/UBC-FRESH/ws4/issues/375) with
  [#376](https://github.com/UBC-FRESH/ws4/issues/376),
  [#377](https://github.com/UBC-FRESH/ws4/issues/377), and
  [#378](https://github.com/UBC-FRESH/ws4/issues/378).

`CARB-01` is **adopted** by live carbon work: `UBC-FRESH/femic` `#361` (P115)
and `UBC-FRESH/ws4` `#357` (P58; carried as P51). Its drafts are in
[`handoffs/superseded/`](handoffs/superseded/README.md); do not create a
parallel carbon issue.

Each parent has a phase-setup checklist: branch, roadmap entry, progress
comment. No branch, commit, tag, or release was created by this handoff. The
full issue bodies and links are in [`handoffs/README.md`](handoffs/README.md).

## What is deliberately out of scope

Not every IRSS output belongs in a forest estate model. Urban energy mapping,
leaf-trait spectroscopy, global biodiversity SDMs, full LANDIS-II/TACA-GEM
coupling, and a from-scratch fire-spread simulator are screened out or held.
The rationale is in [`notes/06-out-of-scope.md`](notes/06-out-of-scope.md).
This matters as much as the inclusions: the programme stays credible by
refusing work that does not change a FRESH decision.

## Status and next action

The source draft's programme phase P0 (mine and publish the register) is
complete. Its P1 (contract wave) is complete: P116.1, P116.2, and P116.3 are
merged, including two published EFI cards and the attribute annotation seam.
`INV-04` (P117.1) is rejected as a new ALS site-index model; P119 replaces it
with VRI/VDYP/SIBEC reconciliation, which is complete. `GRO-06` (P117.2)
remains queued under the still-open P117 parent. P5.1-P5.4 are complete and
parent #7 is closed. ws4 P54 is complete.

The 2026-11-01 registry reconciliation marks `INV-01`, `INV-06`, `DATA-02`, and
`DATA-04` complete with their merged evidence; `INV-01` is the BA-only pilot
(14.9% TSA coverage, strict BA RMSE 8.86 m2/ha), not a volume/height product.
The next planned wave is P2 model integration; no new remote-sensing model is
scheduled. `DEC-02` is complete across WS4 P90-P93: report schema, account CLI,
read-only API, and Reports-tab view. The cards are review-required/advisory, not
operational early warning. A real condition source and `DIS-03` alerting remain
out of scope; see `notes/15-dec02-readiness.md` and
`notes/16-dis03-readiness.md`.

Phase 0 and Phase 1 are complete and merged. Phase 1 squash-merged in pull
request #12 at `2b4620d`: it confirmed the scope rule and out-of-scope list,
reviewed the source inventory and publication signals, recorded that no new ADR
is required, and confirmed the scoring rubric. Phase 2 (contracts and prototype)
is planned under parent issue #13 with child issues #14-#17; its branch and work
wait for maintainer approval. No new candidate or target-repo issue is queued by
this close-out.

## Reading order

0. [`notes/09-executive-brief.md`](notes/09-executive-brief.md): the one-page
   decision brief.
1. [`notes/01-theme-map.md`](notes/01-theme-map.md): IRSS/Silva21 themes mapped
   to FRESH.
2. [`notes/03-fresh-gap-analysis.md`](notes/03-fresh-gap-analysis.md): what the
   stack does now and where the gaps are.
3. [`notes/04-prioritization.md`](notes/04-prioritization.md): scoring method
   and how to read the ranking.
4. [`notes/05-first-wave.md`](notes/05-first-wave.md): the first-wave briefs.
5. [`notes/02-publication-signals.md`](notes/02-publication-signals.md): the
   papers and projects behind the candidates.
6. [`notes/07-silva21-project-map.md`](notes/07-silva21-project-map.md): all 47
   Silva21 project pages with a relevance judgement.
7. [`notes/08-handoff-issue-tree.md`](notes/08-handoff-issue-tree.md): the
   proposed cross-repo issue tree for wave 1.
8. [`notes/10-repo-state-check.md`](notes/10-repo-state-check.md): live-repo
   overlaps and the adjustments they forced.
9. [`notes/11-p1171-data-readiness.md`](notes/11-p1171-data-readiness.md): why
   the real site-index backtest is data-blocked.
10. [`notes/12-lidarbc-pilot.md`](notes/12-lidarbc-pilot.md): a real LidarBC
    tile download and the coverage audit.
11. [`notes/13-vri-proxy-pilot.md`](notes/13-vri-proxy-pilot.md): the
    32-polygon VRI `SITE_INDEX` proxy pilot and why it is not a model.
12. [`notes/14-si-reconciliation.md`](notes/14-si-reconciliation.md): the TSA46
    VRI/VDYP/SIBEC reconciliation, coverage, conflicts, and limits.

`DIS-03` is deferred: the static DHI/recovery layers and the failed NSR
case-control test do not support a near-real-time alert. See
`notes/16-dis03-readiness.md`.

`CARB-03` now has a first bounded slice in FHOPS P44 (parent #380, child #381,
PR #383): a shared `salvage.decay.v1` contract, the published Prestemon &
Holmes (2008) mixed-conifer fire-killed retention curve, the Barrette et al.
(2015) product windows, and `fhops report salvage-shelf-life`. The curve is a US
Pacific Northwest reference, not a BC-specific or species-specific operational
curve; those curves, a dedicated storage curve, grade/value loss, a ws4
consumer, and `OPS-03` scheduling remain follow-on. See
`notes/19-carb03-salvage-decay.md`.

## Public by design

This repository is public. Keep private data, credentials, raw transcripts, and
machine-specific paths out of it. The validator checks the mechanical parts of
that rule. The rest is on you.

The source material is summarized and linked, not copied. Public provenance is
kept in the registry and notes, and third-party data tables, paywalled text, and
raw data are deliberately absent.

## License

MIT. Copyright (c) 2026 UBC FRESH Lab. See [`LICENSE`](LICENSE). Cite the
repository with [`CITATION.cff`](CITATION.cff).
