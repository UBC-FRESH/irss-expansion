``refresh_sources``
===================

The source-refresh checker. It reads every unique public URL in the registry,
follows redirects, and classifies the response as ``ok``, ``blocked``, or
``broken``. It never edits the registry and it is not a CI gate.

.. automodule:: refresh_sources
   :members:
   :show-inheritance:
