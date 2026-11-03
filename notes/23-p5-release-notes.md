# P5.1 release notes and known gaps

Date: 2026-11-03
Phase: P5 Release and deploy
Parent issue: #30
Task: P5.1
Branch: `feature/p5-release`, created from `main` at `c05d955`
Version: `0.1.0`, as recorded in `CITATION.cff`
Release status: release candidate. No tag and no GitHub release exist yet; P5.3
is blocked on a separate maintainer approval.

## 1. What this release is

This is a public-safe planning release. It carries the IRSS x Silva21 expansion
mine, the candidate register, the validators and tests that protect the register,
and the programme notes. It is not a forest model, a simulator, or a Python
package: there is no `[project]` table in `pyproject.toml`, nothing is published
to a package index, and no DOI is assigned.

The durable output is the queue in `registry/candidates.yaml`, the evidence
behind each candidate, and the roadmap that records what was adopted, deferred,
and rejected.

## 2. What is in the release

| Surface | Contents |
| --- | --- |
| Registry | `registry/candidates.yaml`, 62 candidates in nine workstreams |
| Register | Generated `docs/candidates.md` and the Sphinx register page |
| Validators | `scripts/check_registry.py`, `scripts/check_workflow.py`, `scripts/render_registry.py` |
| Dashboard | `scripts/dashboard.py`, six gates: lint, format, types, tests, validator, docs |
| Tests | `tests/`, with the 95 percent branch-coverage gate over `scripts/` |
| Docs | Sphinx site with the register, the API reference, `llms.txt`, and `docs/candidates.md` |
| Planning | `ROADMAP.md`, `CHANGE_LOG.md`, `notes/`, `handoffs/`, and `notes/reports/` |
| Workflow | Issue templates, CI, and the docs deploy workflow |

Register status at the P5.1 working commit: 62 candidates, of which 17 are
`complete`, 2 `adopted`, 1 `queued`, 14 `shortlisted`, 23 `candidate`, 4
`deferred`, and 1 `rejected`.

## 3. Provenance and method

- The mine covers the public IRSS site, its research index, its research theme
  pages, and its publications page, plus the public Silva21 site, its project
  pages, publications, climate and SilvR21 material, extension notes, and data
  portal description.
- The mining was metadata and abstract level. It is not a full-text systematic
  review, and the readiness scores are integration judgements rather than
  author-confirmed estimates. The limits are carried in
  [`00-source-inventory.md`](00-source-inventory.md) and
  [`04-prioritization.md`](04-prioritization.md).
- Each candidate cites at least one public source with a `ref` and an `http(s)`
  URL, a FRESH target, the gap it fills, a first step, and a risk note.
- Accepted work moves to a parent issue in its target repository, where that
  repository's workflow and quality gates apply. This repository does not
  implement candidates.

## 4. How to reproduce the result

From a fresh clone of the public repository:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/dashboard.py
```

The individual checks are:

```bash
python scripts/check_workflow.py
python scripts/check_registry.py
python scripts/render_registry.py
git diff --exit-code docs/candidates.md
python -m pytest -q
```

P5.2 records the clean-checkout result and the exact commit that it covered in
[`24-p5-clean-checkout-verification.md`](24-p5-clean-checkout-verification.md).

## 5. Licence and citation

The repository is MIT licensed; see `LICENSE`. Citation metadata is in
`CITATION.cff`, which names UBC FRESH Lab, version `0.1.0`, and the repository
URL. Until P5.3 runs, cite the repository and the commit, not a tag or a
release.

## 6. Known gaps

1. **No tag and no release.** `v0.1.0` is a proposed tag, not an existing one.
   P5.3 (#33) is blocked on a separate maintainer approval that names the tag,
   the release title, and each command. No package-index artifact exists.
2. **No DOI.** `CITATION.cff` carries no DOI and no concept DOI. Minting one
   would need an external account and a separate approval.
3. **`GRO-06` is queued, not implemented.** The biomass yield curve family stays
   queued under `UBC-FRESH/femic` P117.2 (#376). The handoff body is
   [`../handoffs/femic-child-biomass-curves-p3.md`](../handoffs/femic-child-biomass-curves-p3.md);
   no target-repository issue, branch, or pull request was created from it.
4. **`CARB-03` is adopted but unmerged.** FHOPS P44 (#380), P44.1 (#381), and
   PR #383 were open with CI green at the P4 check. There is no merge commit, so
   the adoption is recorded as in flight rather than delivered.
5. **The mine is metadata and abstract level.** No paper was read in full, no
   author confirmed a readiness score, and no candidate is a validated
   integration. Readiness is a screening judgement, and the risk note is the
   place to challenge it.
6. **No target-repository science was re-run.** "Complete" and "adopted" mean
   that the cited target issue, pull request, or merge commit exists. They are
   not an independent re-validation of the target implementation or its tests.
7. **External checks are dated snapshots.** The P4 CI, Docs, Pages, and
   live-target checks are a 2026-11-03 snapshot. A later target merge, CI
   change, or site outage is outside that evidence. P5.2 records its own date.
8. **Pages and settings are unchanged.** P5.1 does not change repository
   visibility, Pages configuration, branch protection, or any environment. No
   deployment action is included.
9. **The release is documentation, not software.** There is no wheel, sdist,
   console entry point, or supported installation path beyond the development
   requirements in this repository.
10. **Naming is provisional.** `0.1.0` follows `CITATION.cff`. If the maintainer
    chooses a different tag or version at P5.3, `CITATION.cff`, this note, and
    the release must change together before the tag is created.

## 7. Release actions queued for P5.3

Each action needs its own explicit approval. None has run.

```bash
git tag -a v0.1.0 -m "IRSS x Silva21 Expansion Mine 0.1.0" <approved-main-commit>
git push origin v0.1.0
gh release create v0.1.0 --title "IRSS x Silva21 Expansion Mine 0.1.0" --notes-file notes/23-p5-release-notes.md
```

The tag must target the P5 merge commit on `main`, not the branch head. The
release must use the reviewed notes in this file, with the known gaps intact.
