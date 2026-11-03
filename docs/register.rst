Candidate register
==================

The candidate register is the queue of IRSS and Silva21 outputs that have been screened
against the FRESH stack. The machine-readable source is ``registry/candidates.yaml``. The
browsable register is generated from it and must not be edited by hand.

- Generated register: `docs/candidates.md <https://github.com/UBC-FRESH/irss-expansion/blob/main/docs/candidates.md>`_
- Registry source: ``registry/candidates.yaml``
- Scoring method: `notes/04-prioritization.md <https://github.com/UBC-FRESH/irss-expansion/blob/main/notes/04-prioritization.md>`_
  is the long-form note; the formula is
  ``priority = (impact * readiness) / (effort_points * risk)``.

Validate the registry and print the ranking:

.. code-block:: bash

   python scripts/check_registry.py

Regenerate the browsable register:

.. code-block:: bash

   python scripts/render_registry.py
