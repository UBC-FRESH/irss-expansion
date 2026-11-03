Release notes and known gaps
============================

This page describes the ``0.1.0`` release of the IRSS x Silva21 Expansion
Mine. The release is a public-safe planning artefact: the candidate register,
the validators and tests that protect it, and the programme notes. It is not a
forest model or a Python package.

Release status: **released as ``v0.1.0`` on 2026-11-03**. The annotated tag
``v0.1.0`` points at the P5 merge commit ``d3d5ce2``. The GitHub release is
``IRSS x Silva21 Expansion Mine 0.1.0``. No package-index artifact and no DOI
exist.

Tag and release page:
<https://github.com/UBC-FRESH/irss-expansion/releases/tag/v0.1.0>.

What the release contains
-------------------------

- ``registry/candidates.yaml``: 62 candidates in nine workstreams, each with
  public sources, a FRESH target, a gap, a first step, scores, and a risk note.
- The generated register ``docs/candidates.md`` and this documentation site.
- ``scripts/check_registry.py``, ``scripts/check_workflow.py``, and
  ``scripts/render_registry.py``.
- ``scripts/dashboard.py``, which runs lint, format, strict types, tests with the
  coverage gate, the workflow validator, and the docs build.
- The roadmap, changelog, planning notes, handoff drafts, and close-out reports.

The register currently has 17 ``complete``, 2 ``adopted``, 1 ``queued``, 14
``shortlisted``, 23 ``candidate``, 4 ``deferred``, and 1 ``rejected`` candidate.

Reproduce the result
--------------------

.. code-block:: bash

   python -m venv .venv
   . .venv/bin/activate
   python -m pip install -r requirements-dev.txt
   python scripts/dashboard.py

The full release note, with provenance, method, and the complete known-gaps
list, is `notes/23-p5-release-notes.md
<https://github.com/UBC-FRESH/irss-expansion/blob/main/notes/23-p5-release-notes.md>`_.

Known gaps
----------

- No package-index artifact and no DOI exist. The release is the annotated tag
  ``v0.1.0`` and its GitHub release page only.
- ``GRO-06`` is queued, not implemented, under ``femic`` P117.2 (#376).
- ``CARB-03`` is adopted but unmerged in FHOPS P44.
- The mine is metadata and abstract level, not a full-text systematic review.
  Readiness scores are integration judgements, not author-confirmed estimates.
- No target-repository implementation or test suite was re-run. Completion
  claims cite the live target record, not a re-validation of the science.
- External CI, Pages, and live-target checks are dated snapshots, not continuous
  guarantees.
