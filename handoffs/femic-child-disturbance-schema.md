Task identifier: P116.2
Parent phase issue: #369
Status: active
Branch: `feature/p116-shared-contracts`
Related planning: `ROADMAP.md` (Phase 116)
Source register: candidate `DIS-01`

## Goal

Add `disturbance.v1`, a shared event record that FEMIC, ws4, and FHOPS can use
for fire, insect, drought, wind, partial mortality, harvest, and salvage.

## Scope

- Define the event record: event id, type, year, geometry or fragment ids,
  severity, attribution, confidence, source, and provenance.
- Define a small controlled vocabulary for type and a severity representation
  that can carry both categorical and continuous values.
- Add a JSON schema and a validator.
- Add two examples: a stand-replacing fire and a non-stand-replacing event.
- Add a ws4 consumer that reads an event and reports its year and type in a
  scenario.
- Document how an event maps to a fragment or block.

## Out of scope

- A new disturbance detection or attribution algorithm. Existing layers and
  published detectors supply the events.
- A fire-spread simulator.
- A full hazard model. That is `DIS-06`.
- Rebuilding ws4's patch, spread, or road accounts.

## Subtasks

- [x] Define the field list and controlled vocabularies.
- [x] Choose the severity representation and document its limits.
- [x] Write the JSON schema and validator.
- [x] Add the fire and NSR examples.
- [x] Add the ws4-facing consumer rows and a contract test.
- [x] Add the actual ws4 loader and a scenario report (ws4 P56.1, branch `feature/p56-disturbance-consumer`).
- [x] Document the fragment/block mapping and the confidence field.
- [x] Add a changelog entry naming the schema version.

## Acceptance criteria

- The validator rejects an event with no type, no year, or a severity outside
  the declared scale.
- The two examples validate and round-trip without losing provenance.
- ws4 reads both examples and reports the correct year and type.
- The event records which fragments or blocks it touches, or carries a geometry
  that can be resolved without implicit assumptions.
- The tests fail if the schema is loosened without an explicit version bump.

## Verification

```bash
python -m pytest
ruff check src tests
mypy src
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Schema, examples, and validator.
- ws4 consumer.
- Contract tests.
- Docs page.
- Changelog entry.

## Risks

- **Schema overreach.** Disturbance is a broad category. Freeze a small
  vocabulary and extend by version.
- **Severity ambiguity.** Categorical burn severity and continuous mortality
  are not the same scale. Carry both explicitly.
- **Attribution uncertainty.** A confidence field is not a substitute for a
  validated attribution method.
- **Double counting.** A fire and a salvage event can touch the same area; the
  record must preserve the relationship rather than merging them.

## Public sources

- IRSS disturbance and habitat change:
  <https://irsslab.forestry.ubc.ca/research/disturbance-habitat-change/>
- Silva21 OB 5c, non-stand-replacing disturbances:
  <https://www.silva21.com/projects/identifying-and-assessing-the-impact-of-non-stand-replacing-disturbances-within-a-near--real-time-context>
- Brown et al. 2025, NSR detection with HLS:
  <https://doi.org/10.1016/j.isprsjprs.2024.12.014>
