``check_maintenance``
=====================

The maintenance checker. It validates the cadence in
``registry/maintenance.yaml``, checks that ``docs/candidates.md`` matches the
registry, and checks that every active candidate names a target record. Pass
``--due`` for the manual review check that fails after a next date has passed.

.. automodule:: check_maintenance
   :members:
   :show-inheritance:
