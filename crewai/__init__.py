"""
Lightweight stub implementations of key CrewAI classes used in the project.

This stub allows the Genesis Studio demo to run in environments where the
real `crewai` package is unavailable. It intentionally keeps behaviour
minimal and routes execution to existing fallback logic in the agents.
"""

from dataclasses import dataclass, field
from typing import Any, Iterable, List, Optional


@dataclass
class Agent:
    """Simple container for CrewAI agent configuration."""

    role: str
    goal: str
    backstory: str = ""
    tools: List[Any] = field(default_factory=list)
    verbose: bool = False
    allow_delegation: bool = False


@dataclass
class Task:
    """Represents a CrewAI task description and the associated agent."""

    description: str
    expected_output: Optional[str] = None
    agent: Optional[Agent] = None


class Crew:
    """
    Minimal stand-in for CrewAI's Crew.

    The real Crew class orchestrates LLM-powered task execution. Here we simply
    raise an informative error so the existing fallback paths can handle the
    work via custom tools.
    """

    def __init__(
        self,
        agents: Iterable[Agent],
        tasks: Iterable[Task],
        verbose: bool = False,
    ):
        self.agents = list(agents)
        self.tasks = list(tasks)
        self.verbose = verbose

    def kickoff(self, *args, **kwargs):
        raise RuntimeError(
            "CrewAI stub in use — relying on project-specific fallback execution."
        )

