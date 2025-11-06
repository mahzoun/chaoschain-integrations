"""Backward-compatible Eigen compute adapter alias.

The agents and demos historically imported ``EigenComputeAdapter`` from
``chaoschain_integrations.compute.eigencompute``.  The implementation now
resides inside ``chaoschain_integrations.compute.eigen.adapter``, so this
module simply re-exports the adapter to keep existing imports working.
"""

from chaoschain_integrations.compute.eigen.adapter import EigenComputeAdapter

__all__ = ["EigenComputeAdapter"]
