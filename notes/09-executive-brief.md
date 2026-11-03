# Executive brief

## The ask

Decide whether FRESH should open a cross-repo expansion programme that turns
the IRSS and Silva21 public research record into a shared environmental
intelligence layer for FEMIC, ws3, ws4, FHOPS, and Nemora.

## The finding

FRESH has strong decision engines and a thin environmental state layer.

- FEMIC builds a static inventory and static yield curves.
- ws3 and ws4 optimise estate plans against those curves.
- FHOPS schedules operations against block-level assumptions.
- Nemora fits distributions but does not yet push uncertainty into the models.

IRSS and Silva21 have spent roughly two decades building the missing layer:
LiDAR/EFI, optical monitoring, climate-sensitive growth and mortality,
disturbance and recovery, carbon, habitat, and resilience. The material is
mature enough to integrate in pieces, but not as a single research programme.

## The recommendation

Start with **four contracts and one proof**:

1. **Climate contract** (`GRO-01`): a canonical climate table and a
   ClimateNA/SilvR21 adapter.
2. **Disturbance schema** (`DIS-01`): one event record for fire, insect,
   drought, wind, partial mortality, and harvest.
3. **EFI model card** (`DEC-04`): the inventory-model metadata that the LiDAR
   product bundle does not carry.
4. **Curve uncertainty** (`DATA-01`): distribution-based bands for one curve
   family, propagated into a report.
5. **Carbon account v0** (`CARB-01`): already adopted by FEMIC P115 and ws4
   P58; do not open a parallel carbon issue.

Then add the quick wins that make the layer visible: DHI biodiversity
(`BIO-01`), structure habitat index (`BIO-02`), sgsR sampling (`INV-06`), ALS
site index (`INV-04`), spatial resilience metrics (`PLAN-03`), synthetic
landscape fixtures (`DATA-02`), biomass curves (`GRO-06`), and ingest
harmonization (`DATA-04`).

## What it buys

| Capability | Before | After the first two waves |
| --- | --- | --- |
| State | A static inventory vintage | A climate- and disturbance-aware state layer |
| Dynamics | Static curves | Climate modifiers, mortality, NSR, recovery, hazards |
| Values | Volume and cost | Carbon, habitat, resilience, risk exposure |
| Uncertainty | Point estimates | Bands, provenance, and a validation path |
| Operations | Generic treatments | Salvage, thinning, fuel treatment, access-aware scheduling |

## Cost and sequencing

- First wave: 13 candidates, mostly S/M. One is adopted (carbon); the active
  starting set is the four contracts plus the first quick win.
- Second wave: 25 candidates, model-level integration.
- Third wave: 22 candidates, frontier and validation.
- Two candidates are held: soil carbon and serious-game engagement.

The full register has effort, impact, readiness, risk, dependencies, and a
screening score for each candidate.

## Status

All wave-1 issues are created (2026-10-25):

- FEMIC P116 `#369` and P117 `#374`, with their children.
- Nemora P5 `#7`, with `#6`, `#8`, `#9`, and `#10`.
- ws4 P54 `#375`, with `#376`, `#377`, and `#378`.

`CARB-01` is adopted by FEMIC P115 and ws4 P58. No branch, commit, or release
was created by this handoff; phase setup is the first checkbox in each parent.

## Decision requested

1. Approve the programme framing and the four contracts.
2. Contract home: **decided**, `femic/contracts` for this wave; a separate
   `fresh-contracts` repo remains the long-term option.
3. Start the phase-setup checklists: branch, roadmap entry, progress comment.
4. Defer any external data request or partnership until the contracts have a
   merged consumer.

## Risks

- **Transferability.** Published relationships are calibrated in specific hubs
  and BEC zones. Every model candidate needs a validation case.
- **Data access.** The Silva21 portal is access-controlled. Access is a
  dependency, not an assumption.
- **Scope creep.** The mine includes material that does not belong in a forest
  estate model. The out-of-scope note is part of the deliverable.
- **Contract sprawl.** Four contracts are useful; fourteen are a new platform.
  Keep them small and additive.

## The one-sentence version

Do not port 493 papers; build four contracts and five adapters, and let the
rest of the queue follow the evidence.
