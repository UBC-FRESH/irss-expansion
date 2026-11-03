# P5.2 clean-checkout verification

Date: 2026-11-03
Phase: P5 Release and deploy
Parent issue: #30
Task: P5.2
Branch: `feature/p5-release`
Verified commit: `2f013b3e4a8504182937b0f51dab367e2718785f` (`2f013b3`, P5.1)
Public `main` at check time: `c05d955718e7bd0ac9b478bdae21c2232d108d6f` (`c05d955`)
Scope: a fresh clone of the public repository, a fresh virtual environment, the
local gates, the public files, and the Pages site

## Purpose and method

This note records the P5.2 verification. A fresh clone of the public repository
was made outside the working tree, the P5 branch was fetched, and the P5.1
commit was checked out. A new virtual environment installed
`requirements-dev.txt` from scratch. Every command below ran from that clone, not
from the development working tree.

No tag, release, package-index artifact, repository setting, or target-repository
record was created or changed. `main` was not modified.

## 1. Clone and checkout

```bash
git clone https://github.com/UBC-FRESH/irss-expansion.git <scratch>/p5-clean-checkout
cd <scratch>/p5-clean-checkout
git fetch origin feature/p5-release
git checkout 2f013b3
git rev-parse HEAD
```

Results:

- `HEAD` resolved to `2f013b3e4a8504182937b0f51dab367e2718785f`.
- The working tree was clean after checkout.
- `git ls-remote` reported `main` at `c05d955718e7bd0ac9b478bdae21c2232d108d6f`
  and `feature/p5-release` at
  `2f013b3e4a8504182937b0f51dab367e2718785f`.

The clone shows the public files the roadmap names:

| Public file | Present |
| --- | --- |
| `registry/candidates.yaml` | yes |
| `docs/candidates.md` | yes |
| `scripts/check_workflow.py` | yes |
| `.github/workflows/ci.yml` | yes |
| `.github/workflows/docs.yml` | yes |

## 2. Environment

Built with the system Python, not the development environment:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

| Component | Version |
| --- | --- |
| Python | 3.12.3 |
| Sphinx | 9.1.1 |
| pytest | 9.2.0 |
| ruff | 0.17.3 |
| mypy | 2.4.1 |
| pre-commit | 4.7.0 |

## 3. Local gates in the clean clone

```bash
python scripts/check_workflow.py
python scripts/check_registry.py
python scripts/render_registry.py
git diff --exit-code docs/candidates.md
python -m pytest -q
python scripts/dashboard.py
```

| Command | Result |
| --- | --- |
| `python scripts/check_workflow.py` | `0 error(s), 0 warning(s)` |
| `python scripts/check_registry.py` | 62 candidates valid; 17 `complete`, 2 `adopted`, 1 `queued`, 14 `shortlisted`, 23 `candidate`, 4 `deferred`, 1 `rejected` |
| `python scripts/render_registry.py` | wrote `docs/candidates.md`; `git diff --exit-code` exited 0 with no diff |
| `python -m pytest -q` | `186 passed`; 100% branch coverage of `scripts/` (817 statements, 346 branches) |
| `python scripts/dashboard.py` | all six gates GREEN: lint, format, types, tests, validator, docs; `OVERALL: GREEN. Every gate passed.` |

The clean dependency resolution matched the CI environment closely enough that
no gate changed status.

## 4. Public repository and Pages

The public repository was checked through the clone and the GitHub API. The
Pages site was checked with an HTTP client following redirects on 2026-11-03:

| URL | HTTP status | Note |
| --- | ---: | --- |
| <https://ubc-fresh.github.io/irss-expansion/> | 200 | deployed `main` |
| <https://ubc-fresh.github.io/irss-expansion/register.html> | 200 | deployed `main` |
| <https://ubc-fresh.github.io/irss-expansion/candidates.md> | 200 | deployed `main` |
| <https://ubc-fresh.github.io/irss-expansion/llms.txt> | 200 | deployed `main` |
| <https://ubc-fresh.github.io/irss-expansion/releases.html> | 404 | expected: the P5 page is on the unmerged branch |

The Pages site reflects `main` at `c05d955`, not the P5 branch. `releases.html`
will exist only after the P5 pull request merges and the docs deploy workflow
runs. That deployment is outside P5.2 and is not claimed here.

## 5. Release state at check time

- `git tag --list` and `git ls-remote --tags origin` returned no tags.
- `gh release list` returned no releases.
- No package-index artifact exists.

`v0.1.0` therefore remains a proposed tag. P5.3 (#33) is the only task that would
create it, and it is blocked on a separate maintainer approval.

## 6. Limits

- The clean checkout is the P5.1 commit `2f013b3`, not the final P5 head. The
  P5.2 commit and the pull request CI run are the final-head evidence.
- Pages is a live external dependency. The 200 responses are a 2026-11-03
  snapshot; a later outage is not a P5 regression.
- The fresh environment used the same requirements file as CI, but it is not the
  CI runner. The pull request CI run remains the authoritative final-head gate.
- No target repository, model, or dataset was cloned or tested. P5 verifies the
  public planning surfaces, not target science.
- The `releases.html` 404 is expected before the merge; it is recorded rather
  than hidden because it marks the boundary of what P5.2 can verify.

## 7. Final head evidence

Pull request #34 CI run
[41729549516](https://github.com/UBC-FRESH/irss-expansion/actions/runs/41729549516)
passed Quality gates, Green dashboard summary, and Pre-commit parity on
`c03dc78`. A later documentation-only commit that records this run is covered by
the pull request CI run triggered by that commit; the substantive gates were the
ones above, run in the clean clone and on `c03dc78`.
