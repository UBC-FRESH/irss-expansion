Issue: https://github.com/UBC-FRESH/nemora/issues/6

Source register: candidate `DATA-01`

## Goal

Turn one FEMIC/ws4 curve family from a point estimate into a distribution with
a defensible 90% band, and propagate that band into one report. This is the
cheapest credibility improvement in the ecosystem: the model currently implies
a precision the underlying data do not support.

## Scope

- Select one curve family with enough residual or parameter evidence to fit.
- Fit a distribution to the residuals or parameters using the Nemora
  distribution registry and fitting stack.
- Emit a point estimate, a 90% band, and the fitted distribution metadata.
- Propagate the band into one ws4 report or CSV.
- Run a holdout coverage check and record the result, including a failure.
- Document the assumptions and the difference between parameter uncertainty and
  prediction uncertainty.

## Out of scope

- A full Bayesian hierarchical treatment.
- Uncertainty in every curve family.
- Uncertainty in prices, disturbance, or climate. Those are separate
  candidates (`PLAN-08`, `DIS-06`, `GRO-01`).
- Changing the ws4 optimisation objective. This task reports the band; it does
  not make the optimiser robust. That is `DATA-06`.

## Subtasks

- [ ] Choose the curve family and document why it is suitable.
- [ ] Assemble the residuals or parameter evidence.
- [ ] Fit the distribution and record the diagnostics.
- [ ] Emit the band and the metadata.
- [ ] Add the ws4 report or CSV output.
- [ ] Run the holdout coverage check.
- [ ] Document the method and its limits.
- [ ] Add tests for the fit, the band, and the report wiring.

## Acceptance criteria

- The fitted distribution reproduces the observed residual quantiles within a
  stated tolerance, or the task records why it does not.
- The report band contains the point estimate.
- The holdout coverage result is recorded, even if it misses the nominal level.
- The output carries the curve id, distribution family, parameters, sample
  size, and fit date.
- A deliberately bad input (too few observations, a constant residual) produces
  a clear error or warning, not a plausible-looking band.
- The tests can fail if the band is replaced by a constant.

## Verification

```bash
python -m pytest
ruff check src tests
mypy src
sphinx-build -b html docs _build/html -W
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Fitting workflow or module.
- Band output and metadata.
- ws4 report/CSV wiring.
- Coverage check note.
- Docs page and changelog entry.

## Risks

- **Mis-specified distribution.** A poor fit can produce a narrow, confident,
  wrong band. Report diagnostics.
- **Residual dependence.** Curve residuals are often spatially and temporally
  correlated; an i.i.d. fit understates uncertainty.
- **Users ignoring bands.** A band in a CSV is easy to miss. Put it in the
  report and the web view, not only the artifact.
- **Scope creep.** Do not turn this into a general uncertainty platform. One
  family, one report, one honest coverage check.

## Public sources

- Nemora fit and distributions modules: <https://github.com/UBC-FRESH/nemora>
- IRSS growth and yield publications:
  <https://irsslab.forestry.ubc.ca/publications/>
- Planning source: IRSS x Silva21 expansion mine (2026-10-25).
