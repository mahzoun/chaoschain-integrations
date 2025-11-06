"""
Minimal BaseTool stub to satisfy imports from CrewAI integrations.
"""

from typing import Any


class BaseTool:
    """Base interface for tool implementations used by agents."""

    name: str = "base_tool"
    description: str = ""
    args_schema: Any = dict

    def __call__(self, *args, **kwargs):
        return self._run(*args, **kwargs)

    def _run(self, *args, **kwargs):
        raise NotImplementedError("Tool execution not implemented in stub.")

