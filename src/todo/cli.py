# Task: T-008

from todo.storage import Storage
from todo.commands import add_task, view_tasks, update_task, delete_task, toggle_complete


def start_cli(storage: Storage) -> None:
    """Start the interactive CLI menu loop.

    Args:
        storage: Storage instance to use for all operations
    """
    while True:
        print("\n=== Todo CLI ===")
        print("1. Add task")
        print("2. View all tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Toggle complete")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        match choice:
            case "1":
                title = input("Enter title: ").strip()
                description = input("Enter description (optional): ").strip()
                result = add_task(storage, title, description)
                print(result)

            case "2":
                result = view_tasks(storage)
                print(result)

            case "3":
                try:
                    task_id = int(input("Enter task ID: ").strip())
                    title = input("Enter new title (leave empty to skip): ").strip()
                    description = input("Enter new description (leave empty to skip): ").strip()
                    result = update_task(storage, task_id, title, description)
                    print(result)
                except ValueError:
                    print("Error: Invalid task ID")

            case "4":
                try:
                    task_id = int(input("Enter task ID: ").strip())
                    confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").strip().lower()
                    if confirm == "y":
                        result = delete_task(storage, task_id)
                        print(result)
                    else:
                        print("Delete cancelled")
                except ValueError:
                    print("Error: Invalid task ID")

            case "5":
                try:
                    task_id = int(input("Enter task ID: ").strip())
                    result = toggle_complete(storage, task_id)
                    print(result)
                except ValueError:
                    print("Error: Invalid task ID")

            case "6":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please enter 1-6.")
