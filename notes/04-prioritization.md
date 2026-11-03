# Prioritisation method

Reviewed: 2026-11-03 (P1.4). The formula, effort points, rubrics, wave logic,
and first-wave table match `scripts/check_registry.py`; no score or wave
assignment changed.

## Why a score at all

The mine produced 62 candidates. Without a transparent screen, the queue
becomes a list of everything interesting, which is the same as no queue. The
score is a **screening aid**, not an approval mechanism. It makes the
trade-offs visible and gives a reviewer something concrete to disagree with.

## The formula

```
priority = (impact * readiness) / (effort_points * risk)
```

- `effort_points`: S = 1, M = 2, L = 3, XL = 5.
- `impact`, `readiness`, `risk`: integers from 1 to 5.
- The score is rounded to two decimals.
- A higher score means "more valuable per unit of effort and risk".

The validator computes the score; it is not stored in the YAML. That keeps the
registry from drifting when a score changes.

## Rubrics

### Impact (1-5)

How much the candidate changes a FRESH decision, model, or user capability.

| Score | Meaning |
| ---: | --- |
| 5 | Changes a core model output or unlocks a new class of decision (climate, risk, carbon, habitat) |
| 4 | Materially improves an existing output or workflow |
| 3 | Useful improvement, but the ecosystem can function without it |
| 2 | Niche or indirect benefit |
| 1 | Interesting science with no near-term FRESH decision |

### Readiness (1-5)

How ready the method, data, and integration path are.

| Score | Meaning |
| ---: | --- |
| 5 | Published method, open or accessible data, clear adapter, existing reference implementation |
| 4 | Published method, data available but needs preparation, adapter is clear |
| 3 | Method is published but transferability or data access is uncertain |
| 2 | Research-grade; needs a pilot or a partner |
| 1 | Concept only |

### Effort (S/M/L/XL)

Integration effort, not research effort.

| Code | Rough size | Typical shape |
| --- | --- | --- |
| S | Days to two weeks | Schema, reader, wrapper, one report |
| M | Two to six weeks | Adapter, tests, one consumer, documentation |
| L | Two to three months | New module, validation, multiple consumers |
| XL | More than three months | New modelling lane, partner data, or solver work |

### Risk (1-5)

The chance that the integration is wrong, unusable, or cannot be validated.

| Score | Meaning |
| ---: | --- |
| 1 | Low: a contract or a wrapper with a clear oracle |
| 2 | Moderate: a published relationship with a validation path |
| 3 | Material: transferability, data access, or model-form uncertainty |
| 4 | High: changes an optimisation objective, needs new science, or depends on a partner |
| 5 | Very high: unresolved causal or policy question |

## Wave assignment

The wave is **not** a score threshold. It encodes dependency order and
strategic sequencing.

| Wave | Meaning | Rule of thumb |
| ---: | --- | --- |
| 1 | Contracts and quick wins | Unblocks later work; S/M effort; low risk; one consumer |
| 2 | Model integration | Needs wave-1 contracts; changes a model output or workflow |
| 3 | Frontier and validation | Needs wave-2 evidence; research-grade or partner-dependent |
| 0 | Hold or reject | Not a near-term FRESH decision, or a deliberate "no" |

A candidate can have a high score and still sit in wave 2 because it depends on
a wave-1 contract. A candidate can have a lower score and sit in wave 1 because
it is a prerequisite.

## The first-wave choice

The first wave is deliberately **contract-heavy**:

| ID | Score | Effort | Why it is wave 1 |
| --- | ---: | --- | --- |
| `GRO-01` | 25.00 | S | Climate is the input to every dynamics candidate |
| `DIS-01` | 25.00 | S | Disturbance is the shared event language |
| `DEC-04` | 16.00 | S | EFI model cards make ALS attributes trustworthy |
| `DATA-01` | 12.50 | M | Uncertainty is the cheapest credibility win |
| `BIO-01` | 20.00 | S | A public biodiversity layer with an immediate account |
| `INV-06` | 15.00 | S | A reference implementation already exists |
| `INV-04` | 4.00 | M | Improves curve selection at fragment resolution |
| `CARB-01` | 5.00 | M | Adopted by FEMIC P115 and ws4 P58; no parallel issue |
| `GRO-06` | 5.00 | M | Biomass curves unlock carbon and habitat |
| `PLAN-03` | 4.00 | M | Turns existing spatial accounts into a resilience story |
| `DATA-02` | 8.00 | M | Makes testing at scale possible |
| `BIO-02` | 4.00 | M | Links structure to habitat |
| `DATA-04` | 7.50 | M | Removes duplicated ingest work |

## High score, not wave 1

These are good candidates held back by dependency or sequencing:

| ID | Score | Why not wave 1 |
| --- | ---: | --- |
| `DEC-02` | 12.00 | Depends on the monitoring loop (`DIS-03`), which is wave 3 |
| `DEC-03` | 8.00 | Better after the uncertainty and climate contracts exist |
| `CARB-03` | 6.00 | Depends on salvage shelf-life (`DIS-09`) and carbon (`CARB-01`) |
| `PLAN-07` | 6.00 | Needs the scenario explorer (`DEC-01`) and uncertainty bands |
| `PLAN-08` | 6.00 | Needs the provenance contract (`DEC-03`) |

## Low score, still wave 1

| ID | Score | Why it is still early |
| --- | ---: | --- |
| `INV-04` | 4.00 | It is a small adapter that improves every curve decision |
| `CARB-01` | 5.00 | It reuses an existing CBM path and unlocks a new report |
| `GRO-06` | 5.00 | It is the data prerequisite for carbon and biomass |
| `PLAN-03` | 4.00 | It uses existing ws4 accounts; low new science |

## Dependency spine

The main dependency chains are:

```
GRO-01 climate contract
  -> GRO-02 climate-adjusted curves
  -> GRO-03 mortality
  -> PLAN-01 risk-aware planning
  -> DATA-06 uncertainty-aware optimization

DIS-01 disturbance schema
  -> DIS-02 NSR adapter
  -> DIS-04 recovery/regeneration
  -> DIS-06 hazard library
  -> PLAN-01 risk-aware planning
  -> CARB-02 disturbance emissions

DEC-04 EFI model cards
  -> INV-01 ALS inventory attributes
  -> INV-04 site index
  -> INV-10 genetic gain and seedlot performance
  -> BIO-02 structure habitat index

INV-02 tree lists
  -> OPS-06 taper and product recovery

DATA-01 uncertainty
  -> CARB-01 carbon account
  -> DEC-03 provenance communication
  -> DATA-06 robust optimization

CARB-01 carbon account
  -> CARB-02 emissions
  -> CARB-03 degradation
  -> OPS-03 salvage scheduling
```

`GRO-01`, `DIS-01`, `DEC-04`, and `DATA-01` are the four load-bearing contracts.
If the programme does only four things, it should do those.

## Sensitivity

The score is sensitive to `risk` and `effort` because they are denominators. A
one-point risk increase on a 5x5 candidate drops the score by roughly 20%. That
is intentional: an unvalidated model change is expensive.

The score is less sensitive to `impact` when readiness is low. A high-impact,
research-grade candidate scores poorly. That is also intentional: it belongs in
wave 3, not in the first quarter.

## When to change a score

Change a score when the evidence changes, not when the priority changes. Valid
reasons:

- A dataset becomes open, or a licence becomes restricted.
- A reference implementation is released.
- A paper is replicated (or fails to replicate) in a relevant ecosystem.
- A target repo changes its data model or objective.
- A pilot shows the adapter is cheaper or more expensive than assumed.

Invalid reasons:

- A senior person wants it higher.
- A competitor announced something.
- The score is inconvenient for the current sprint.

Record the reason in `CHANGE_LOG.md` and, if the change is material, in the
candidate's `risks` or `first_step`.

## Review cadence

- Re-score at the end of each wave.
- Re-read the source pages before adding a candidate.
- Retire candidates that have been `candidate` for two waves without a
  first-step owner.
- Keep the first wave small enough to finish. Thirteen is already ambitious for
  a part-time programme; the recommended first five are the true starting
  point.

## 2026-11-03 review (P1.4)

- Confirmed `priority = (impact * readiness) / (effort_points * risk)` against
  `priority_score` in `scripts/check_registry.py`. The effort map is still
  S = 1, M = 2, L = 3, XL = 5, and the score is rounded to two decimals.
- Confirmed the impact, readiness, effort, and risk rubrics and the wave logic
  are unchanged. A wave is still a dependency and sequencing judgement, not a
  score threshold.
- Compared all 13 rows of the first-wave table with the validator output. Every
  ID, score, and effort code matches, including `DATA-01` at 12.50 and the four
  low-score wave-1 entries.
- Confirmed the registry wave counts: wave 0 has 2 candidates, wave 1 has 13,
  wave 2 has 25, and wave 3 has 22.
- Did not re-score a candidate, change a wave, or alter the formula. Readiness
  remains an integration judgement, not an author-confirmed science claim.

