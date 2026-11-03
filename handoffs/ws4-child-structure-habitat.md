Task identifier: P54.2
Parent phase issue: #375
Status: planned
Branch: `feature/p53-environmental-accounts`
Related planning: `ROADMAP.md` (Phase 53)
Source register: candidate `BIO-02`

## Goal

Implement a published forest structure habitat index from ALS metrics and
report it as a stand- and landscape-level account, with a comparison to DHI.

## Scope

- Implement the published structure habitat index.
- Attach it to fragments or blocks from the FEMIC LiDAR product bundle.
- Report the index at stand and landscape level.
- Compare it with the DHI account and record agreement/disagreement.
- Add a caveat note on index validity.

## Out of scope

- A species-specific habitat model.
- A new ALS segmentation or canopy algorithm. FEMIC P79 owns the LiDAR products.
- A change to the optimisation objective.
- Carbon accounting. It is owned by P51.

## Subtasks

- [ ] Confirm the published index definition and weights.
- [ ] Implement the index from the available ALS metrics.
- [ ] Add the fragment/block attachment and coverage check.
- [ ] Emit the stand and landscape accounts.
- [ ] Add the DHI comparison.
- [ ] Document the caveats and the metric availability.
- [ ] Add tests for index arithmetic, coverage, and reproducibility.

## Acceptance criteria

- The index is computable wherever the required metrics exist; missing metrics
  are reported, not imputed silently.
- The account is reproducible from the LiDAR bundle and the index version.
- The DHI comparison is reported, including disagreement.
- The caveat note is present in the report.
- The tests fail if a required metric or the index version is dropped.

## Verification

```bash
python scripts/dashboard.py
```

Record the exact commands and results in `CHANGE_LOG.md`.

## Artifacts

- Index implementation.
- Account and comparison output.
- Docs page and changelog entry.

## Risks

- **Index validity.** A structural index is not a species observation. State the
  evidence and the limits.
- **Metric availability.** Some ALS acquisitions lack the required metrics.
- **Weight sensitivity.** Report the weights and, where feasible, a sensitivity
  check.

## Public sources

- IRSS structure habitat index publications:
  <https://irsslab.forestry.ubc.ca/publications/>
- Silva21 OB 5b, composition and structure metrics:
  <https://www.silva21.com/projects/metrics-for-silvicultural-prescription%3A-composition-and-structure>
- Planning source: IRSS x Silva21 expansion mine (2026-10-25).
