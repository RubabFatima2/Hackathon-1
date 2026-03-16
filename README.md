# Task: T-010

# Todo CLI App

A simple command-line todo application built with Python.

## Features

- Add tasks with title and optional description
- View all tasks with status indicators
- Update task title and description
- Delete tasks
- Toggle task completion status
- Interactive CLI menu

## Requirements

- Python 3.13+
- UV package manager

## Setup

1. Install UV if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:
```bash
git clone <repository-url>
cd hack1
```

3. Install dependencies (if any):
```bash
uv sync
```

## Usage

Run the application:
```bash
uv run python main.py
```

Or with Python directly:
```bash
python main.py
```

## Menu Options

1. **Add task** - Create a new task with title and optional description
2. **View all tasks** - Display all tasks with their status
3. **Update task** - Modify an existing task's title or description
4. **Delete task** - Remove a task (with confirmation)
5. **Toggle complete** - Mark a task as complete or incomplete
6. **Exit** - Quit the application

## Project Structure

```
hack1/
├── main.py              # Entry point
├── src/
│   └── todo/
│       ├── models.py    # Task dataclass
│       ├── storage.py   # In-memory storage
│       ├── commands.py  # Command functions
│       └── cli.py       # Interactive CLI
├── specs/               # Specifications
└── AGENTS.md           # Agent instructions
```

## Development

This project follows Spec-Driven Development (SDD). See AGENTS.md for development guidelines.
