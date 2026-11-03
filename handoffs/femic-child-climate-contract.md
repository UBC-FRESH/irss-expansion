Task identifier: P116.1
Parent phase issue: #369
Status: active
Branch: `feature/p116-shared-contracts`
Related planning: `ROADMAP.md` (Phase 116)
Source register: candidate `GRO-01`

## Goal

Add `climate.v1` and a ClimateNA/SilvR21 adapter so FEMIC, ws4, and Nemora can
consume one provenance-bearing climate table instead of three ad hoc formats.

## Scope

- Define a tidy table keyed by AOI, variable, year (or period), scenario, GCM,
  and source.
- Record units, downscaling method, baseline period, scenario label, and source
  version.
- Add a JSON schema and a validator.
- Add an adapter for ClimateNA/SilvR21 outputs.
- Add a small sample table for one AOI.
- Wire one consumer: a FEMIC reader that validates the table and exposes it to
  a curve or attribute stage. The consumer may stop at a documented interface;
  it does not need to implement a climate modifier in this task.

## Out of scope

- A new climate model, downscaling method, or GCM ensemble selector.
- A climate scenario UI.
- A full climate-growth response model. That is `GRO-02`.
- Committing third-party climate data to the repository.

## Subtasks

- [x] Define the field list, units, and controlled vocabularies.
- [x] Write the JSON schema and validator.
- [x] Implement the annual ClimateNA/SilvR21 CSV adapter.
- [x] Add a small sample for one AOI with provenance.
- [x] Add the FEMIC reader and a contract test.
- [x] Wire the first attribute consumer (`femic.climate.consumer`).
- [x] Document the contract and the scenario/GCM selection caveat.
- [x] Add a changelog entry naming the schema version.

## Acceptance criteria

- The validator rejects a missing scenario, an unknown unit, and a negative
  variance or impossible value.
- A round-trip of the sample table produces an identical table.
- A second AOI with a different GCM ensemble loads without code changes.
- The adapter records the source file, source version, downscaling method, and
  retrieval date.
- The consumer reports the provenance fields in its output.
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

- Schema and sample table.
- Adapter and reader.
- Contract tests.
- Docs page.
- Changelog entry.

## Risks

- **Licensing.** ClimateNA/SilvR21 terms must be checked before redistributing
  any derived table.
- **Ensemble ambiguity.** A single GCM is not a scenario. Record the ensemble
  and the selection rule.
- **Unit drift.** Temperature, precipitation, and variance units are a common
  source of silent error; validate them.
- **Temporal mismatch.** Climate years, simulation offsets, and inventory
  vintages are different clocks; document the mapping.

## Public sources

- Silva21 climate data: <https://www.silva21.com/climatedata?lang=en>
- Wotherspoon et al. 2022, *Climate Scenarios for Canadian Forests*:
  <https://www.silva21.com/climatedata?lang=en>
- Wotherspoon et al. 2023, future climate trends:
  <https://doi.org/10.1139/cjfr-2023-0058>
