# Task: T-001

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a todo task with title, description, and completion status."""

    id: int
    title: str
    description: str = ""
    completed: bool = False
