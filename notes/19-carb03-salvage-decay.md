# CARB-03 implementation: salvage shelf-life and wood degradation

Status: first bounded slice adopted in FHOPS P44 (parent #380, child #381,
PR #383, mergeable with CI green). This note records what landed, the source
boundaries, and what remains. It does not claim a complete species- or
product-specific value model.

## Candidate

`CARB-03` — Wood degradation and storage value loss. The registry describes the
goal as species- and product-specific degradation curves for standing dead wood
and roadside storage, used in salvage and inventory valuation.

The sibling candidates are `DIS-09` (salvage shelf-life and value-decay model)
and `OPS-03` (salvage harvest scheduling with shelf-life). This slice supplies a
shared surface they can consume, but it does not complete their scheduling or
ws4 valuation work.

## Audit result

FHOPS before P44 had salvage harvest systems and an optional
`salvage_processing_mode` block field, but no time-dependent degradation,
shelf-life, or value-retention code. ws4 had carbon pools and `prices.v1`, but no
wood-product degradation surface. The gap recorded in
`notes/03-fresh-gap-analysis.md` was accurate.

## Sources and why they were chosen

### Chagnon et al. (2022)

Chagnon, C., Moreau, G., Bombardier-Cauffopé, C., Barrette, J., Havreljuk, F.
and Achim, A. (2022). "Broad-scale wood degradation dynamics in the face of
climate change: A meta-analysis." *GCB Bioenergy* 14:941-958,
<https://doi.org/10.1111/gcbb.12951>.

This is the candidate's climate/degradation context. It publishes a
time-since-death (TSD) meta-regression by decay class, maximum summer
temperature, annual precipitation, wood density, and phylogeny. It does **not**
publish product-value loss factors or a merchantable-grade mapping. Turning its
decay classes into product value would require a new mapping, which would be
invented science. It is therefore not used for numeric coefficients in P44.

### Prestemon and Holmes (2008)

Prestemon, J.P. and Holmes, T.P. (2008). "Timber Salvage Economics." In:
Holmes, T.P., Prestemon, J.P., Abt, K.L. (eds), *The Economics of Forest
Disturbances*. Springer, Dordrecht, pp. 167-190, section 4.2.6. Public PDF:
<https://research.fs.usda.gov/download/treesearch/32962.pdf>.

This supplies the explicit net-volume retention factors used in P44: 0.99 after
1 year, 0.89 after 2 years, 0.58 after 3 years, 0.22 after 4 years, and zero
after 5 years. The report attributes years 1-3 to Lowell and Cahill (1996) and
years 4-5 to Prestemon et al. (2006).

Boundary: mixed-conifer fire-killed timber in southwest Oregon (Biscuit fire).
The FHOPS curve is labelled as a reference curve, not a BC-specific,
species-specific, or roadside-storage-specific operational curve. FHOPS adds no
points and fits no model; whole-year values are exact and intervening ages use
linear interpolation.

### Barrette et al. (2015)

Barrette, J., Thiffault, E., Saint-Pierre, F., Wetzel, S., Duchesne, I. and
Krigstin, S. (2015). "Dynamics of dead tree degradation and shelf-life following
natural disturbances: can salvaged trees from boreal forests 'fuel' the forestry
and bioenergy sectors?" *Forestry* 88(3):275-290,
<https://doi.org/10.1093/forestry/cpv007>. Abstract mirrored at
<https://hero.epa.gov/reference/6726560/>.

The review supplies the Canadian boreal shelf-life windows: lumber generally
1-2 years after death, pulp usually not recommended after 3-4 years, then
bioenergy. The Silva21 AD 4 context presentation by Hébert, Duchesne and Mvolo
(IEA Bioenergy / Université Laval, 2023) repeats the same summary and cites
Barrette et al.:

<https://task43.ieabioenergy.com/wp-content/uploads/sites/38/2023/10/Hebert-Duchesne-Mvolo_Post-fire-salvage-logging-in-Canada.pdf>.

These are encoded as advisory, overlapping windows, not a mill-acceptance rule.

## Landed artifacts

In `UBC-FRESH/fhops` branch `feature/p44-salvage-degradation`, PR #383:

- `src/fhops/salvage/degradation.py` — typed `salvage.decay.v1` curve library,
  provenance and boundary records, linear retention interpolation, product
  windows.
- `data/reference/degradation/salvage_decay.v1.json` — published curve and
  product windows with citation, URL, boundary, and retrieval date.
- `src/fhops/salvage/report.py` — read-only consumer that joins a storage/age
  table to scenario blocks.
- `src/fhops/cli/reporting.py` — `fhops report salvage-shelf-life`.
- `tests/test_salvage_degradation.py`,
  `tests/test_cli_report_salvage.py`.
- `docs/howto/salvage_shelf_life.rst`, `docs/api/fhops.salvage.rst`.
- `examples/salvage_shelf_life/`.
- `notes/carb03_salvage_degradation.md` in FHOPS.

Example CLI output on `examples/tiny7`:

| block | age (years) | retention | original m³ | retained m³ | products |
| --- | ---: | ---: | ---: | ---: | --- |
| B01 | 1 | 0.99 | 2,007.91 | 1,987.83 | lumber; pulp |
| B02 | 4 | 0.22 | 2,406.79 | 529.49 | pulp; bioenergy |

## Deliberate exclusions

- No MILP objective, constraint, heuristic, or solver changes.
- No scenario-schema change; age comes from a side table.
- No price forecast, grade recovery, or market model.
- No ws4 carbon-engine change. The module is a reusable contract, but a ws4
  consumer should be a separate phase with a BC-relevant curve.
- No new coefficients, fitted points, or extrapolation beyond the published
  last point.

## Remaining work

1. **BC or species-specific retention curve.** Needs a public or
   project-approved source with explicit factors by species/product and a
   climate/storage boundary. The BC deadwood synthesis by Huggard and Kremsater
   (2007) is a habitat-decay synthesis, not a product-value curve, so it was not
   used.
2. **Dedicated roadside-storage curve.** P44 uses time since fire/death because
   that is what the published curve says. A deck-storage curve needs its own
   public source.
3. **Grade/value loss.** Barrette et al. gives shelf-life windows, not
   value-loss percentages. A value model needs grade recovery and price data.
4. **ws4 consumer.** Consume the same contract only after a BC-relevant curve
   exists; do not silently reuse the US reference curve as a BC operational
   assumption.
5. **OPS-03 scheduling.** The report is read-only. Scheduling salvage under
   decay, access, and mill-demand constraints is still `OPS-03`.

## Verification

In the FHOPS P44 worktree:

```bash
ruff format --check src tests
ruff check src tests
mypy src
pytest
FHOPS_RUN_FULL_CLI_TESTS=1 pytest tests/test_cli_report_salvage.py
sphinx-build -b html docs _build/html -W
```

All passed. The full `pytest` suite completed without failures; targeted
salvage tests: 18 unit/consumer tests and 5 CLI tests.
