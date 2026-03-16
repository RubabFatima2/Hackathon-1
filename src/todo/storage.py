# Task: T-002

from todo.models import Task


class Storage:
    """In-memory storage for Task objects with auto-incrementing IDs."""

    def __init__(self):
        """Initialize empty task list and ID counter."""
        self._tasks: list[Task] = []
        self._next_id: int = 1

    def add(self, task: Task) -> Task:
        """Add a task with auto-incremented ID.

        Args:
            task: Task object (ID will be overwritten)

        Returns:
            The task with assigned ID
        """
        task.id = self._next_id
        self._next_id += 1
        self._tasks.append(task)
        return task

    def get(self, task_id: int) -> Task | None:
        """Get a task by ID.

        Args:
            task_id: The task ID to retrieve

        Returns:
            Task object or None if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def get_all(self) -> list[Task]:
        """Return all tasks.

        Returns:
            List of all Task objects
        """
        return self._tasks.copy()

    def update(self, task_id: int, **kwargs) -> bool:
        """Update task fields.

        Args:
            task_id: The task ID to update
            **kwargs: Fields to update (title, description, completed)

        Returns:
            True if task was found and updated, False otherwise
        """
        task = self.get(task_id)
        if task is None:
            return False

        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)

        return True

    def delete(self, task_id: int) -> bool:
        """Remove a task by ID.

        Args:
            task_id: The task ID to delete

        Returns:
            True if task was found and deleted, False otherwise
        """
        task = self.get(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True
