# Canonical Solution — Todo List CLI (Python)

This folder contains the canonical reference solution for the `todo-list-cli-python` project.

## Solution structure

- `solution.py`: Complete implementation of the core functions required by the project:
  - `add_one_task(title)`
  - `print_list()`
  - `delete_task(number_to_delete)`
  - `save_todos()`
  - `load_todos()`

## Key implementation decisions

- **In-memory state**: Uses a global `todos` list because the starter project and tests expect shared mutable state.
- **Delete behavior**: Converts input to `int` and deletes by one-based position (`position - 1`) because the CLI shows task numbers starting at 1.
- **Persistence format**: Stores tasks in `todos.csv` as one task per line, matching what the test suite reads and writes.
- **Load behavior**: Replaces the in-memory list with file contents, and handles empty files by resetting to an empty list.

## How files connect

- Student-facing runtime entry point is `app.py`.
- This solution mirrors the same function logic in `solution.py` as a clean reference implementation for comparison.
- The tests (`test.py`) validate behavior against this expected flow:
  1. Add tasks
  2. Delete by position
  3. Save to `todos.csv`
  4. Load from `todos.csv`

## Indicative examples (expected behavior)

### Example 1: Add and list tasks

Input flow:

```python
add_one_task("Make the bed")
add_one_task("Clean kitchen")
print_list()
```

Expected stdout:

```text
1. Make the bed
2. Clean kitchen
```

### Example 2: Delete by position

Given:

```python
todos = ["Make the bed", "Make lunch", "Clean kitchen"]
delete_task(2)
```

Expected in-memory list:

```python
["Make the bed", "Clean kitchen"]
```

### Example 3: Save and load

Given:

```python
todos = ["jump", "run", "roll"]
save_todos()
todos = []
load_todos()
```

Expected in-memory list after load:

```python
["jump", "run", "roll"]
```

Expected `todos.csv` content:

```text
jump
run
roll
```
