# Out of scope, deferred, and deliberately rejected

A queue is defined as much by what it refuses as by what it admits. This note
records the material that was reviewed and **not** turned into a near-term
candidate, with the reason.

## Deferred in the register

These have candidate IDs because they are plausible later, but they are wave 0.

| ID | Candidate | Why deferred | What would change the decision |
| --- | --- | --- | --- |
| `CARB-04` | Soil carbon and site-productivity layer | Dynamic soil carbon is a research programme, not an integration. The map layer is useful, but it does not change a near-term decision. | A validated, spatially explicit soil-carbon model with a clear boundary and a partner. |
| `PLAN-06` | Deliberative-analytic and serious-game engagement | Valuable, but facilitation-heavy and not software-first. It also depends on a stable scenario portfolio and web UI. | A funded engagement project and a stable `DEC-01`/`PLAN-02` surface. |

## Screened out entirely

These were reviewed but not registered. They are not judgements on their
scientific quality; they are judgements about FRESH fit.

### Urban energy and urban canopy mapping

IRSS has a strong urban programme: LiDAR-based building energy demand, solar
potential, urban vegetation, and street-tree mapping. It does not change a
forest estate or harvesting decision. A municipal canopy module is a different
product with a different user, data model, and sales motion.

**Revisit if:** FRESH creates an urban or community-forest product line.

### Leaf traits, spectroscopy, and biodiversity from space

IRSS has substantial work on leaf functional traits, spectral diversity, and
Essential Biodiversity Variables. The methods are sophisticated, but the output
is a trait or diversity map, not a forest-management decision variable. It
would sit above the habitat accounts rather than replace them.

**Revisit if:** a user needs a trait-based habitat or conservation layer, and
the structure/DHI accounts are already in place.

### Global species distribution modelling as a product

IRSS has avian, mammal, and tree SDMs across large regions. A general global
SDM platform is out of scope: it is a separate modelling product with a
different validation burden. The register keeps a **lightweight SDM pipeline**
(`BIO-03`) and **specific suitability layers** (`GRO-08`) instead.

**Revisit if:** a partner needs a multi-species SDM service.

### Full LANDIS-II / TACA-GEM coupling

The IRSS disturbance/habitat work includes LANDIS-II and TACA-GEM for
long-term forest ecosystem and grizzly-food simulation. Coupling a landscape
succession model into FRESH would be a major architectural commitment and would
duplicate capabilities the estate model already has.

**Revisit if:** the question is explicitly long-term ecosystem succession, not
timber supply or operations, and a partner funds the coupling.

### A from-scratch fire-spread simulator

ws4's P15/P16 work already ran a fire model against treated masks and produced a
**documented negative result** at the treated footprint: the fire ranking did
not survive the scale and stochasticity of the experiment. The register treats
fire as a hazard or an expected-loss term (`DIS-06`, `PLAN-01`), not as a new
simulator.

**Revisit if:** a validated fire model with the right footprint and stochastic
design is available, and the question requires spatial fire behaviour rather
than risk exposure.

### Operational water and snow hydrology (owned by FEMIC P114)

IRSS has a strong snow/hydrology programme: SnowWarp, ALS-derived snow metrics,
equivalent clear-cut area thresholds, and stream morphology. This mine does
**not** queue a hydrology module because FEMIC already has an active phase for
it: **P114, Forest Hydrology and Flood-Risk Optimization** (`#351`). The
register keeps **stream and riparian metrics** (`BIO-04`) because they affect
buffers and operations, and treats IRSS/Silva21 snow and stream work as a
potential input or validation source for P114.

**Revisit if:** P114 needs a specific IRSS product (SnowWarp, ALS snow metrics,
stream morphology) as an input or validation layer. Coordinate with P114 rather
than creating a parallel hydrology lane.

### Wood products, markets, and nighttime-lights economics

IRSS has work on lumber production from nighttime lights, wood degradation, and
macroeconomic price shocks. The register keeps the **degradation** piece
(`CARB-03`) because it affects salvage, and a **price-path** scenario input
(`PLAN-08`) because it affects planning. A full market model is out of scope.

**Revisit if:** FHOPS or ws4 needs a market-clearing or mill-capacity model.

### Drone regulations, pilot training, and field campaign logistics

Silva21 has useful extension notes on choosing a drone and becoming a foreign
drone pilot. These are operational guidance, not software. They belong in a
field manual, not a FRESH repo.

**Revisit if:** FRESH ships a field-data collection companion.

### A FRESH-hosted data portal

The Silva21 portal uses Globus and institutional storage. Building a FRESH data
portal is a separate infrastructure project. The register keeps **data access
and validation relationships** (`DEC-05`) and **provenance** (`DEC-03`), not a
portal.

**Revisit if:** FRESH needs to publish its own multi-hub data products.

### Social and cultural values as a first-class model input

Silva21 has important work on culturally important species, Indigenous
relationships to black ash, and deliberative engagement. These are central to
responsible forestry, but they are not a near-term software feature. Reducing
them to a layer or a weight would be worse than leaving them as a partnership
and engagement activity.

**Revisit if:** co-designed with the relevant Nations and communities, with
their own governance and data protocols.

## The "not now" list

Things that are plausible but not yet worth a candidate ID:

- A general-purpose forest carbon marketplace model.
- A national-scale LiDAR change detection service.
- A real-time fire alerting product.
- A forest health app for the public.
- A standalone climate downscaling pipeline.
- A machine-learning yield model with no interpretability or provenance.

Each of these could become a candidate if a user, a dataset, and a validation
path appear. Until then, they are noise in the queue.

## How to revive a screened-out item

1. Name the FRESH decision it changes.
2. Name the data and the licence.
3. Name the validation case.
4. Name the target repo and the insertion point.
5. Add it to `registry/candidates.yaml` with a source and a first step.

If those five things cannot be named, it is not ready to be a candidate.
