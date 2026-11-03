Task identifier: P117.2
Parent phase issue: #374
Status: planned
Branch: `feature/p117-efi-attributes`
Related planning: `ROADMAP.md` (Phase 117)
Source register: candidate `GRO-06`

## Goal

Add a biomass curve family derived from time-series remote sensing and lidar
plots, alongside the existing volume curves, and a declared carbon conversion.

## Scope

- Add one biomass curve family for a pilot species/BEC.
- Keep the volume curve as the primary output; make the biomass family
  independently selectable.
- Add a carbon conversion using a declared fraction and boundary.
- Record the source, species, curve version, and conversion factor.
- Compare the biomass and volume curves.

## Out of scope

- The CBM package or runtime. FEMIC P115 and ws4 P51 own carbon.
- A new remote-sensing study or a global biomass map.
- Belowground biomass unless the source provides it.
- A change to the estate model's objective.

## Subtasks

- [ ] Select the published biomass curve family and document its domain.
- [ ] Add the curve table and the independent selection path.
- [ ] Add the carbon conversion and boundary note.
- [ ] Compare with the volume curve.
- [ ] Add tests for monotonicity, units, and independent selection.
- [ ] Document the source, species, and conversion.
- [ ] Add a changelog entry.

## Acceptance criteria

- The biomass curve is selectable independently of the volume curve.
- Biomass is monotonic where the source relationship is monotonic.
- The carbon conversion uses a declared fraction and records the boundary.
- The source, species, and curve version travel with the curve.
- The tests fail if the conversion factor or source is dropped.

## Verification

```bash
python -m pytest
python -m ruff check .
python -m mypy src
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Biomass curve family and conversion.
- Comparison output.
- Docs page and changelog entry.

## Risks

- **Allometry.** Species and belowground assumptions dominate.
- **Curve vintage.** Remote-sensing biomass curves have a time window.
- **Double counting.** Do not sum biomass and volume into the same account.
- **False precision.** A biomass curve is not a carbon inventory. State the
  boundary.

## Public sources

- Tompalski et al. 2024, biomass yield curves from time-series remote sensing:
  <https://doi.org/10.1016/j.foreco.2024.121894>
- IRSS carbon and biomass research:
  <https://irsslab.forestry.ubc.ca/research/carbon/>
- Planning source: IRSS x Silva21 expansion mine (2026-10-25).
