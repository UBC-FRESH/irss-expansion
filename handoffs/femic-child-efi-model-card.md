Task identifier: P116.3
Parent phase issue: #369
Status: active
Branch: `feature/p116-shared-contracts`
Related planning: `ROADMAP.md` (Phase 116)
Source register: candidate `DEC-04`

## Goal

Add `efi.model.v1`, a model card that travels with ALS-derived inventory
attributes so a consumer can tell what the model predicts, how accurate it is,
where it applies, and what it was trained on.

FEMIC already ships a sensor-product bundle manifest (`femic.lidar.product.v1`).
This task adds the missing **inventory-model** metadata; it does not replace the
bundle manifest.

## Scope

- Define the model card: model id, version, target attribute, unit, predictors,
  training data, validation design, RMSE/bias, applicability domain, licence,
  and provenance.
- Add a JSON schema and a validator.
- Add two model cards from real published or project models.
- Add a FEMIC reader that attaches a model card to an ALS-derived attribute
  table.
- Document how a consumer should reject an attribute outside the applicability
  domain.

## Out of scope

- Rebuilding the LiDAR product bundle or its acquisition metadata.
- Training or retraining an area-based model. That is `INV-01`.
- Claiming field accuracy that the model did not measure.
- A model registry service or database.

## Subtasks

- [x] Define the field list and the applicability-domain representation.
- [x] Write the JSON schema and validator.
- [x] Add two public-safe synthetic model cards.
- [ ] Replace or augment the synthetic cards with two real project or published cards.
- [x] Add the row-annotation helper and a contract test.
- [ ] Wire the card metadata through the FEMIC attribute pipeline.
- [x] Document the reject/flag rule for out-of-domain attributes.
- [x] Add a changelog entry naming the schema version.

## Acceptance criteria

- A card missing an accuracy field or an applicability domain fails validation.
- Two cards with different training regions and species coexist.
- The FEMIC reader preserves the model id and RMSE on every attribute row.
- A consumer can identify an out-of-domain attribute without reading prose.
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

- Schema and two model cards.
- FEMIC attachment.
- Contract tests.
- Docs page.
- Changelog entry.

## Risks

- **Over-specific schema.** Models differ by sensor, species, and region. Keep
  version 1 small and extend by version.
- **Vendor metadata gaps.** A commercial EFI model may not disclose its training
  data; the card must allow a declared unknown without pretending otherwise.
- **Applicability drift.** A model card is a claim at a point in time. Record
  the version and the validation date.
- **False authority.** A model card is not a validation certificate. It makes
  the claim inspectable, not true.

## Public sources

- IRSS LiDAR research: <https://irsslab.forestry.ubc.ca/research/lidar/>
- Goodbody et al. 2024, integrating ALS into forest ecosystem management:
  <https://doi.org/10.5558/tfc2024-014>
- FEMIC LiDAR product bundle contract (existing):
  <https://github.com/UBC-FRESH/femic>
