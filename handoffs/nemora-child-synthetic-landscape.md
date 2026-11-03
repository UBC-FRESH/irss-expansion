Task identifier: P5.2
Parent phase issue: #7
Status: planned
Branch: `feature/p5-uncertainty-sampling`
Related planning: `ROADMAP.md` (Phase 5)
Source register: candidate `DATA-02`

## Goal

Generate one synthetic landscape with known volume, age, and structure, export
it in the ws4 build format, and run it through ws4 build and simulate.

## Scope

- Use the existing `nemora.synthesis` tessellation, stand, and stem modules.
- Produce a deterministic landscape from a seed.
- Export the known attributes and the ws4-compatible build inputs.
- Run the fixture through ws4 build and simulate.
- Add a short note on realism and limits.

## Out of scope

- A new generator or a new tessellation algorithm.
- A calibrated synthetic forest that claims to represent a real landscape.
- The measurement-campaign simulator (`DATA-03`).
- A carbon or habitat account.

## Subtasks

- [ ] Define the fixture parameters and the known target properties.
- [ ] Generate the landscape and stems from a seed.
- [ ] Export the ws4 build inputs and a truth table.
- [ ] Run ws4 build and simulate.
- [ ] Add a smoke test that asserts the known volume within tolerance.
- [ ] Document the realism limits.
- [ ] Add a changelog entry.

## Acceptance criteria

- The fixture is deterministic from the seed.
- The known volume is reproduced within a stated tolerance after build.
- ws4 build and simulate run without manual edits.
- The truth table is published with the fixture.
- The test fails if the seed or the truth table is dropped.

## Verification

```bash
python -m pytest
ruff check src tests
mypy src
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Fixture and truth table.
- ws4 smoke test.
- Docs note and changelog entry.

## Risks

- **False confidence.** Synthetic realism is not evidence.
- **Fixture drift.** The truth table and the generator can diverge; test them
  together.
- **Scale.** A fixture that is too large slows CI; keep it small and add one
  scale case later.

## Public sources

- Nemora synthesis: <https://github.com/UBC-FRESH/nemora>
- IRSS LiDAR sampling and inventory research:
  <https://irsslab.forestry.ubc.ca/research/lidar/>
