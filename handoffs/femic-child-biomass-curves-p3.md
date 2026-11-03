Task identifier: P117.2
Parent phase issue: #374
Target repository: `UBC-FRESH/femic`
Target phase: P117 EFI Inventory Attributes and Biomass Curves (active)
Branch: `feature/p117-efi-attributes`
Status: planned
Source register: candidate `GRO-06`
Handoff status: reviewed by P3.2 and P3.3 on 2026-11-03. This body is for the
existing P117.2 issue (#376), not a new issue. No target issue, branch, or pull
request was created or edited by P3.

## Goal

Add one published biomass curve family alongside the existing volume curve,
make it independently selectable, and add a declared aboveground biomass to
carbon conversion with its boundary and provenance.

## Why now

FEMIC produces volume curves, not biomass or carbon curves. Carbon reporting
therefore needs an external conversion with no recorded source, version, or
applicability domain. A bounded biomass family closes that gap without
duplicating the FEMIC P115 carbon package or the P117.1 site-index lane.

P117 is already active on `feature/p117-efi-attributes`; P117.1 is the
site-index lane and P117.2 is this biomass lane. The phase, child issue, branch,
and acceptance path already exist, so this handoff does not open a new target
phase.

## Provenance

- `GRO-06` in `registry/candidates.yaml`.
- Tompalski et al. (2024), "Developing aboveground biomass yield curves from
  time-series remote sensing", <https://doi.org/10.1016/j.foreco.2024.121894>.
- IRSS carbon and biomass research, <https://irsslab.forestry.ubc.ca/research/carbon/>.
- FEMIC P117 parent issue, <https://github.com/UBC-FRESH/femic/issues/374>.
- FEMIC P117.2 issue, <https://github.com/UBC-FRESH/femic/issues/376>.
- FEMIC P115 carbon package, <https://github.com/UBC-FRESH/femic/issues/361>
  (consumer boundary only; this task does not change it).

## Scope

- Select one published biomass curve family for one pilot species/BEC and
  document its applicability domain, units, source, and vintage.
- Add a biomass curve table and an independent selection path. Selecting biomass
  must not change the volume curve, and selecting volume must not change the
  biomass curve.
- Add an aboveground biomass to carbon conversion using a declared carbon
  fraction with a cited source or an explicit project assumption.
- Record the model/source id, species, BEC, curve version, units, applicability
  range, carbon fraction, and boundary on the curve table or its metadata.
- Compare the biomass and volume curves on the pilot instance and report where
  they diverge.
- Add tests, docs, and a changelog entry in `femic`.

## Named consumers

- The FEMIC curve and export stage, which selects the family for a pilot
  instance.
- The FEMIC/ws4 estate-model input path, which reads the selected family instead
  of an external conversion.
- The carbon report path only as a labelled conversion. The CBM runtime, carbon
  package, and ws4 carbon engine remain owned by FEMIC P115 and ws4 P58.

## Out of scope

- Refitting a biomass model or creating a new remote-sensing study.
- A global biomass map or a new allometric equation.
- Belowground biomass unless the published source provides it explicitly.
- The FEMIC P115 carbon package, CBM runtime, GCBM export, or ws4 carbon engine.
- A change to an estate-model objective, constraint, growth curve, or solver.
- A new site-index lane; that is P117.1.
- Copying a third-party table into the repository where redistribution is not
  permitted. Use a cited schema fixture or the minimum published points that may
  be redistributed.

## First step

Select the published biomass curve family and write its applicability card. If
the source table cannot be redistributed, encode a synthetic fixture with the
same schema and cite the source; keep the real pilot data outside tracked files.

## Validation boundary

- The curve is a **published relationship consumed as-is**, not a refit.
- The pilot is **one species/BEC**, not an operational or province-wide product.
- The curve is **aboveground biomass** unless the source states otherwise.
- The carbon fraction is a **declared parameter** with a source or an explicit
  assumption. It is not a measured carbon inventory.
- The curve vintage and remote-sensing time window are explicit.
- The comparison with volume is a **screening check**, not an independent
  validation of the published model.
- No carbon-inventory, CBM-parity, or regulatory claim is made.

## Subtasks

- [ ] Select one published biomass curve family and record species, BEC, units,
  source, vintage, and applicability range.
- [ ] Add the biomass curve table and its metadata (source, species, version,
  domain, carbon fraction, boundary).
- [ ] Add the independent selection path for volume and biomass.
- [ ] Add the aboveground biomass to carbon conversion and a boundary note.
- [ ] Compare biomass and volume on the pilot instance and record the divergence.
- [ ] Add `tests/test_biomass_curves.py` with the acceptance tests below.
- [ ] Document the source, method, units, domain, and limits.
- [ ] Add a `femic` changelog entry and update the P117 roadmap.

## Acceptance test

The acceptance test is executable in `UBC-FRESH/femic`:

```bash
python -m pytest tests/test_biomass_curves.py -q
```

The new test file must contain and pass these cases:

1. `test_biomass_family_selectable_independently` — selecting the biomass family
   leaves the volume output unchanged, and selecting volume leaves biomass
   unchanged.
2. `test_biomass_monotonic_within_source_domain` — biomass is non-decreasing
   where the published source is non-decreasing; an age outside the declared
   domain is rejected or flagged, not silently extrapolated.
3. `test_carbon_conversion_requires_declared_fraction_and_boundary` — a missing
   carbon fraction, unit, source, or boundary raises a typed error.
4. `test_provenance_travels_with_curve` — every row or its table metadata carries
   the source id, species, BEC, curve version, units, and applicability range.
5. `test_volume_and_biomass_not_double_counted` — a report selects one family or
   labels the two families separately; it does not sum them into one account.

Regression and gates:

```bash
python -m pytest tests/test_managed_curves.py tests/test_vdyp_curves.py -q
python -m pytest
python -m ruff check .
python -m mypy src
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in the `femic` `CHANGE_LOG.md`. A fixture
run must show the volume and biomass selections producing different curve
columns while preserving the rest of the output.

## Artifacts

- Biomass curve family and metadata.
- Independent selection path and carbon conversion.
- Volume-versus-biomass comparison output.
- `tests/test_biomass_curves.py`.
- Docs page and `femic` changelog entry.

## Risks

- **Allometry.** Species and belowground assumptions can dominate the result.
- **Domain transfer.** The published family may not cover the pilot BEC or age
  range.
- **Curve vintage.** Remote-sensing biomass curves have a time window.
- **Double counting.** Biomass and volume must not be summed into one account.
- **False precision.** A biomass curve is not a carbon inventory. State the
  boundary.

## Approval gate

This is a handoff draft. Updating issue #376, creating a branch or pull request,
or implementing the candidate requires separate maintainer approval. P3 does none
of those actions.
