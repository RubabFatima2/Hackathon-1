# Plan — Phase I: Todo CLI App

## Architecture Overview
Single-process in-memory Python CLI app.
No database, no files, no network. Data lives only while the program runs.

## Component Breakdown

### 1. Task Model (src/todo/models.py)
A dataclass representing one todo item.
Fields:
- id: int — auto-incremented, starts at 1
- title: str — required
- description: str — optional, defaults to ""
- completed: bool — defaults to False

### 2. Storage (src/todo/storage.py)
A class that holds the task list in memory.
Responsibilities:
- Store tasks in a plain Python list
- Generate next available ID
- Add, get, update, delete tasks
- Return all tasks

### 3. Commands (src/todo/commands.py)
Pure functions — one per feature.
Each function takes a Storage instance + user input, returns a result string.
Functions:
- add_task(storage, title, description) → str
- view_tasks(storage) → str
- update_task(storage, task_id, title, description) → str
- delete_task(storage, task_id) → str
- toggle_complete(storage, task_id) → str

### 4. CLI (src/todo/cli.py)
The interactive menu loop.
- Prints a numbered menu
- Reads user input
- Calls the right command function
- Prints the result
- Loops until user chooses Exit
- Uses match/case for menu routing

### 5. Entry Point (main.py)
Creates a Storage instance and starts the CLI loop.

## Data Flow
User input → cli.py → commands.py → storage.py → Task model
                    ↑_____________result string______________↓

## Error Handling Strategy
- Invalid task ID → friendly message, no crash
- Empty title → reject with message
- Invalid menu choice → "Invalid option, try again"
- All errors caught inside command functions, never in CLI loop