Task identifier: P5.4
Parent phase issue: #7
Status: planned
Branch: `feature/p5-uncertainty-sampling`
Related planning: `ROADMAP.md` (Phase 5)
Source register: candidate `INV-06`

## Goal

Wrap or port the sgsR structurally guided sampling workflow into
`nemora.sampling`, with a CLI/API and one worked example.

## Scope

- Implement or wrap the sgsR sampling design workflow.
- Accept a structural metric layer and a target plot count or sampling budget.
- Return the allocation and the structural strata.
- Add a CLI or Python API and a worked example.
- Record the implementation choice (port vs R bridge) and its maintenance cost.

## Out of scope

- A new sampling theory.
- A new LiDAR metric or canopy pipeline.
- A field campaign.
- A change to FEMIC or ws4 model inputs.

## Subtasks

- [ ] Review the sgsR algorithm and licence.
- [ ] Choose port vs R bridge and record the decision.
- [ ] Implement the wrapper and the structural strata.
- [ ] Add the CLI/API and the worked example.
- [ ] Add reproducibility and bad-input tests.
- [ ] Document the method and the maintenance cost.
- [ ] Add a changelog entry.

## Acceptance criteria

- The same inputs produce the same allocation.
- The output includes the structural strata and the plot count.
- A constant or missing structural metric produces a clear error or warning.
- The worked example is reproducible from the repository.
- The tests fail if the seed or the structural strata are dropped.

## Verification

```bash
python -m pytest
ruff check src tests
mypy src
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Sampling wrapper.
- CLI/API and worked example.
- Docs note and changelog entry.

## Risks

- **R/Python bridge.** A bridge adds a runtime dependency; a port adds
  maintenance. Record the trade-off.
- **Licence.** Check the original implementation's licence before copying.
- **Structural metric availability.** The method needs a meaningful structure
  layer; state the fallback.

## Public sources

- Goodbody et al. 2023, sgsR:
  <https://doi.org/10.1093/forestry/cpac055>
- Silva21 OB 5a, continuous forest inventory:
  <https://www.silva21.com/projects/continuous-forest-inventory-framework>
- Nemora sampling: <https://github.com/UBC-FRESH/nemora>
