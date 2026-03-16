# Task: T-003

from todo.models import Task
from todo.storage import Storage


def add_task(storage: Storage, title: str, description: str = "") -> str:
    """Add a new task to storage.

    Args:
        storage: Storage instance to add task to
        title: Task title (required, 1-200 characters)
        description: Optional task description

    Returns:
        Success message with task ID, or error message if validation fails
    """
    # Validate title
    if not title or len(title.strip()) == 0:
        return "Error: Title is required"

    if len(title) > 200:
        return "Error: Title must be 200 characters or less"

    # Create and add task
    task = Task(id=0, title=title, description=description)
    added_task = storage.add(task)

    return f"Task added successfully (ID: {added_task.id})"


# Task: T-004

def view_tasks(storage: Storage) -> str:
    """View all tasks with their status.

    Args:
        storage: Storage instance to retrieve tasks from

    Returns:
        Formatted string with all tasks, or "No tasks yet." if empty
    """
    tasks = storage.get_all()

    if not tasks:
        return "No tasks yet."

    result = []
    for task in tasks:
        status = "✓" if task.completed else "○"
        result.append(f"[{task.id}] {status} {task.title}")
        if task.description:
            result.append(f"    {task.description}")

    return "\n".join(result)


# Task: T-005

def update_task(storage: Storage, task_id: int, title: str = "", description: str = "") -> str:
    """Update a task's title and/or description.

    Args:
        storage: Storage instance
        task_id: ID of the task to update
        title: New title (optional)
        description: New description (optional)

    Returns:
        Success message or error if task not found
    """
    task = storage.get(task_id)
    if not task:
        return f"Error: Task {task_id} not found"

    # Validate title if provided
    if title:
        if len(title.strip()) == 0:
            return "Error: Title cannot be empty"
        if len(title) > 200:
            return "Error: Title must be 200 characters or less"
        storage.update(task_id, title=title)

    if description:
        storage.update(task_id, description=description)

    if not title and not description:
        return "Error: No updates provided"

    return f"Task {task_id} updated successfully"


# Task: T-006

def delete_task(storage: Storage, task_id: int) -> str:
    """Delete a task by ID.

    Args:
        storage: Storage instance
        task_id: ID of the task to delete

    Returns:
        Confirmation message with task title, or error if not found
    """
    task = storage.get(task_id)
    if not task:
        return f"Error: Task {task_id} not found"

    task_title = task.title
    success = storage.delete(task_id)

    if success:
        return f"Task '{task_title}' deleted successfully"
    else:
        return f"Error: Failed to delete task {task_id}"


# Task: T-007

def toggle_complete(storage: Storage, task_id: int) -> str:
    """Toggle a task's completion status.

    Args:
        storage: Storage instance
        task_id: ID of the task to toggle

    Returns:
        Message showing new status, or error if not found
    """
    task = storage.get(task_id)
    if not task:
        return f"Error: Task {task_id} not found"

    new_status = not task.completed
    storage.update(task_id, completed=new_status)

    status_text = "✓ complete" if new_status else "○ incomplete"
    return f"Task {task_id} marked as {status_text}"
