# P4 acceptance evidence

Date: 2026-11-03
Phase: P4 Verify
Parent issue: #25
Task: P4.1
Branch: `feature/p4-verify`, created from `main` at `8b23206`
Scope: local acceptance checks, `main` CI, Docs, the public Pages site, and a
clean-checkout reproduction

## Purpose and method

This note records the P4.1 acceptance evidence. The local checks ran against the
P4 working tree: `main` at `8b23206` plus the P4 activation edits in `ROADMAP.md`
and this note. The final report commit is the head that the pull request CI run
covers; section 7 records that later run.

All target-repository checks are read-only. No target issue, branch, pull
request, setting, tag, or release was created or changed.

## 1. Local acceptance checks

Commands, run from the repository root on 2026-11-03:

```bash
python scripts/check_workflow.py
python scripts/check_registry.py
python scripts/render_registry.py
git diff --exit-code docs/candidates.md
python -m pytest -q
python scripts/dashboard.py
```

Results:

| Command | Result |
| --- | --- |
| `python scripts/check_workflow.py` | `0 error(s), 0 warning(s)` |
| `python scripts/check_registry.py` | 62 candidates valid; 17 complete, 2 adopted, 1 queued, 14 shortlisted, 23 candidate, 4 deferred, 1 rejected |
| `python scripts/render_registry.py` | wrote `docs/candidates.md`; `git diff --exit-code` reported no change |
| `python -m pytest -q` | `186 passed`; 100% branch coverage of `scripts/` (817 statements, 346 branches) |
| `python scripts/dashboard.py` | all six gates GREEN: lint, format, types, tests, validator, docs; `OVERALL: GREEN` |

The registry counts come from the validator's ranking output. The command wrote
the generated register under the repository root and left no diff.

## 2. Public `main` CI and Docs runs

The live `main` head at the start of P4 was
`8b2320646008c90c055ad20d9cc3b3d1e1cb8338` (`8b23206`).

| Workflow | Run | Head | Conclusion | Jobs |
| --- | --- | --- | --- | --- |
| CI | [41721924289](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41721924289) | `8b23206` | success | Quality gates, Green dashboard summary, Pre-commit parity all success |
| Docs | [41721924173](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41721924173) | `8b23206` | success | build and deploy both success |

Both runs were triggered by the push to `main`, not by the P4 branch.

## 3. Public Pages site

Checked on 2026-11-03 with an HTTP client following redirects:

| URL | HTTP status |
| --- | ---: |
| <https://ubc-fresh.github.io/irss-expansion/> | 200 |
| <https://ubc-fresh.github.io/irss-expansion/register.html> | 200 |
| <https://ubc-fresh.github.io/irss-expansion/candidates.md> | 200 |
| <https://ubc-fresh.github.io/irss-expansion/llms.txt> | 200 |

The site reflects the deployed `main` content at `8b23206`; the P4 branch is not
published.

## 4. Clean-checkout reproduction

A fresh clone of the public repository was made under a scratch path outside the
working tree, then the dashboard was run from it:

```bash
git clone https://github.com/UBC-FRESH/irss-expansion.git <scratch>/p4-clean-8b23206
cd <scratch>/p4-clean-8b23206
git rev-parse HEAD
python scripts/dashboard.py
```

Results: `HEAD` resolved to `8b2320646008c90c055ad20d9cc3b3d1e1cb8338`; the
dashboard reported all six gates GREEN with `OVERALL: GREEN. Every gate passed.`
No repository file was modified by the run.

## 5. Live target heads checked

Read on 2026-11-03 with `git ls-remote`, for the P4.2 reconciliation:

| Repository | `main` head |
| --- | --- |
| `UBC-FRESH/femic` | `faf00af` |
| `UBC-FRESH/ws4` | `a86f884` |
| `UBC-FRESH/fhops` | `296e2cf` |
| `UBC-FRESH/ws3` | `b84a0ae` |
| `UBC-FRESH/nemora` | `060c688` |
| `UBC-FRESH/fresh-road` | `df8ad2d` |

These heads match the P3 snapshot. P4.2 records the candidate-level check.

## 6. Limits

- The Pages check is a live external dependency. It returned 200 on the date
  above; a later outage is not evidence of a P4 regression.
- The clean checkpoint is the public `main` commit, not an uncommitted P4
  working tree. The pull request CI run is the evidence for the P4 head.
- The local environment used the repository's existing Python dependencies. A
  dependency-resolution difference in CI would be visible in the PR run.
- No target repository test suite was run. P4 verifies the cited merge and issue
  state, not the target science.

## 7. Final head evidence

The P4 pull request CI run and its head commit are recorded in
`notes/reports/p4-verify.md` and in the P4.3 `CHANGE_LOG.md` entry after the
pull request opens. The report commit is the head that run covers.
