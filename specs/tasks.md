# Tasks — Phase I: Todo CLI App

## Status Legend
- [ ] Not started
- [x] Complete

---

### T-001: Create Task dataclass
- Description: Define the Task model with all required fields
- Input: nothing (just a class definition)
- Output: src/todo/models.py
- File: src/todo/models.py
- Spec ref: §Add Task (specify.md)

---

### T-002: Create in-memory Storage class
- Description: Build the Storage class that holds a list of Task objects and manages IDs
- Input: nothing at init
- Output: src/todo/storage.py with add, get, get_all, update, delete methods
- File: src/todo/storage.py
- Spec ref: §Plan Component 2

---

### T-003: Implement add_task command
- Description: Function that validates title, creates a Task, adds to storage, returns confirmation
- Input: storage instance, title (str), description (str)
- Output: success message with new task ID, or error if title empty
- File: src/todo/commands.py
- Spec ref: §Add Task acceptance criteria (specify.md)

---

### T-004: Implement view_tasks command
- Description: Function that returns formatted list of all tasks with ID, status icon, title, description
- Input: storage instance
- Output: formatted string — table of tasks, or "No tasks yet." if empty
- File: src/todo/commands.py
- Spec ref: §View Tasks acceptance criteria (specify.md)

---

### T-005: Implement update_task command
- Description: Function that finds a task by ID and updates title and/or description
- Input: storage instance, task_id (int), new title (str), new description (str)
- Output: success message, or error if ID not found
- File: src/todo/commands.py
- Spec ref: §Update Task acceptance criteria (specify.md)

---

### T-006: Implement delete_task command
- Description: Function that removes a task by ID from storage
- Input: storage instance, task_id (int)
- Output: confirmation message with deleted task title, or error if ID not found
- File: src/todo/commands.py
- Spec ref: §Delete Task acceptance criteria (specify.md)

---

### T-007: Implement toggle_complete command
- Description: Function that flips a task's completed status between True and False
- Input: storage instance, task_id (int)
- Output: message showing new status (✓ complete / ○ incomplete), or error if ID not found
- File: src/todo/commands.py
- Spec ref: §Mark Complete acceptance criteria (specify.md)

---

### T-008: Build the CLI menu loop
- Description: Interactive menu that prints options, reads input, calls command functions, loops until exit
- Input: storage instance
- Output: src/todo/cli.py with start_cli(storage) function
- File: src/todo/cli.py
- Spec ref: §Plan Component 4

Menu options:
  1. Add task
  2. View all tasks
  3. Update task
  4. Delete task
  5. Toggle complete
  6. Exit

---

### T-009: Create entry point and package init files
- Description: Wire everything together — main.py creates Storage, calls start_cli. Add __init__.py files.
- Input: all previous tasks complete
- Output: main.py, src/todo/__init__.py, src/__init__.py
- File: main.py
- Spec ref: §Plan Component 5

---

### T-010: Create README and CLAUDE.md
- Description: Write setup instructions and Claude Code instructions
- Input: completed working app
- Output: README.md with UV setup steps, CLAUDE.md pointing to AGENTS.md
- File: README.md, CLAUDE.md
- Spec ref: Hackathon deliverables requirement