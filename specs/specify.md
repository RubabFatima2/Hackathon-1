# Specify — Phase I: Todo CLI App

## User Stories
- As a user, I can add a task with a title and optional description
- As a user, I can view all my tasks with status indicators
- As a user, I can update a task's title or description
- As a user, I can delete a task by its ID
- As a user, I can mark a task as complete or incomplete

## Acceptance Criteria

### Add Task
- Title is required (1–200 characters)
- Description is optional
- Each task gets a unique auto-incremented ID
- New tasks default to incomplete

### View Tasks
- Shows: ID, title, description, status (✓ or ○)
- Shows "No tasks yet" if list is empty

### Update Task
- User provides task ID + new title and/or description
- Error if task ID not found

### Delete Task
- User provides task ID
- Confirmation message shown
- Error if task ID not found

### Mark Complete
- Toggles between complete and incomplete
- Shows current status after toggling