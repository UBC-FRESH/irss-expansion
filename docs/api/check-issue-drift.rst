``check_issue_drift``
=====================

The issue/registry drift checker. It reads the active target records named in
``registry/maintenance.yaml`` with ``gh`` and compares their live state with the
recorded expectation. It does not edit a target repository.

.. automodule:: check_issue_drift
   :members:
   :show-inheritance:
