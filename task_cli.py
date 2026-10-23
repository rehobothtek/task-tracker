import json
from pathlib import Path
from datetime import datetime

TASKS_FILE = Path("tasks.json")


def load_tasks():
    if not TASKS_FILE.exists() or TASKS_FILE.stat().st_size == 0:
        TASKS_FILE.write_text("[]")

    with TASKS_FILE.open("r") as file:
        return json.load(file)



def add_task(description):
    tasks = load_tasks()

    if not description.strip():
        print("Error: Task description cannot be empty.")
        return

    task_id = max((task["id"] for task in tasks), default=0) + 1
    now = datetime.now().isoformat(timespec="seconds")

    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)

    with TASKS_FILE.open("w") as file:
        json.dump(tasks, file, indent=4)

    print(f"Task added successfully (ID: {task_id})")


def list_tasks(status=None):
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        print("No tasks found with that status.")
        return

    for task in tasks:
        print(f'ID: {task["id"]}')
        print(f'Description: {task["description"]}')
        print(f'Status: {task["status"]}')
        print(f'Created: {task["createdAt"]}')
        print(f'Updated: {task["updatedAt"]}')
        print("-" * 30)

def update_task(task_id, new_description):
    tasks = load_tasks()

    if not new_description.strip():
        print("Error: Task description cannot be empty.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat(timespec="seconds")

            with TASKS_FILE.open("w") as file:
                json.dump(tasks, file, indent=4)

            print(f"Task {task_id} updated successfully.")
            return

    print(f"Error: Task {task_id} not found.")


def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            with TASKS_FILE.open("w") as file:
                json.dump(tasks, file, indent=4)

            print(f"Task {task_id} deleted successfully.")
            return

    print(f"Error: Task {task_id} not found.")


def mark_task(task_id, status):
    if status not in ("todo", "in-progress", "done"):
        print("Error: Invalid task status.")
        return

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat(timespec="seconds")

            with TASKS_FILE.open("w") as file:
                json.dump(tasks, file, indent=4)

            print(f"Task {task_id} marked as {status}.")
            return

    print(f"Error: Task {task_id} not found.")


import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 task_cli.py <command>")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print('Usage: python3 task_cli.py add "task description"')
            return

        description = " ".join(sys.argv[2:])
        add_task(description)

    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)

    elif command == "update":
        if len(sys.argv) < 4:
            print('Usage: python3 task_cli.py update <id> "new description"')
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be a number.")
            return

        description = " ".join(sys.argv[3:])
        update_task(task_id, description)

    elif command == "delete":
        if len(sys.argv) != 3:
            print("Usage: python3 task_cli.py delete <id>")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be a number.")
            return

        delete_task(task_id)

    elif command in ("mark-in-progress", "mark-done"):
        if len(sys.argv) != 3:
            print(f"Usage: python3 task_cli.py {command} <id>")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be a number.")
            return

        status = "in-progress" if command == "mark-in-progress" else "done"
        mark_task(task_id, status)

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
