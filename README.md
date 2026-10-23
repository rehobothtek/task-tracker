# Task Tracker CLI

A simple command-line application built with Python to manage daily tasks. It allows users to add, update, delete, and track tasks using a JSON file for storage.

## Features

- Add new tasks.
- Update existing tasks.
- Delete tasks.
- Mark tasks as in progress.
- Mark tasks as done.
- List all tasks.
- List tasks by status: `todo`, `in-progress`, or `done`.
- Store tasks in a JSON file.
- Generate unique task IDs and timestamps.
- Handle invalid commands and task IDs.

## Requirements

- Python 3
- No external libraries required.

## Installation

1. Clone or download the project.
2. Open a terminal in the project directory.
3. Run the application using Python 3.

## Usage

### Add a task

```bash
python3 task_cli.py add "Buy groceries"
```

### List all tasks

```bash
python3 task_cli.py list
```

### List tasks by status

```bash
python3 task_cli.py list done
python3 task_cli.py list todo
python3 task_cli.py list in-progress
```

### Update a task

```bash
python3 task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python3 task_cli.py delete 1
```

### Mark a task as in progress

```bash
python3 task_cli.py mark-in-progress 1
```

### Mark a task as done

```bash
python3 task_cli.py mark-done 1
```

## Data Storage

Tasks are stored in `tasks.json` in the current project directory.

Each task contains:

- `id`: Unique task identifier.
- `description`: Task description.
- `status`: Current task status.
- `createdAt`: Date and time the task was created.
- `updatedAt`: Date and time the task was last updated.

## Technologies

- Python 3
- JSON
- Python standard library

## License

This project was created for learning and practice.
