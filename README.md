# Todo List CLI in Python

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/exercise-todo-list-cli-python/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

You have joined the internal tools team at a small logistics company. Operations coordinators currently track pending tasks in chat messages and sticky notes, and they keep losing important follow-ups between shifts. Your product manager asked for a lightweight command-line tool that any team member can run quickly in the terminal to manage daily tasks.

The tool should let coordinators register new tasks as they come in, review the full list at any time, and remove completed tasks by selecting their list position. Since teams may close and reopen terminals throughout the day, they also need to store tasks in a local file and reload them later without losing progress.

> Your product manager shared this functional brief:
>
> ### Required behavior
>
> - Add one new task by title
> - Display all pending tasks with their numeric position
> - Delete one task by its position in the list
> - Save tasks into a `todos.csv` file
> - Load tasks back from `todos.csv`
> - No task editing flow is needed for this version; users should delete and recreate tasks instead

Build the first usable version so the operations team can test it this week.

<how-to-start>

## 🌱 How to Start the Project

- Open this link in your browser using [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended): `https://github.com/codespaces/new/?repo=4GeeksAcademy/python-hello`
- Or clone the starter template locally:

```bash
git clone https://github.com/4GeeksAcademy/python-hello
```

- If you work locally, make sure Python is [installed](https://4geeks.com/how-to/how-to-install-python)
- Run `python3 app.py` to verify your environment works
- Run `python3 test.py` to execute the tests
- Create your own GitHub repository for delivery and update remote URL with `git remote set-url origin <your-new-url>`
- Follow the full project bootstrap guide here: [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project)

</how-to-start>

## 💻 What You Need to Do

- [ ] Implement `add_one_task(title)` to add a new task to the in-memory task list
- [ ] Implement `print_list()` to show all tasks with clear numeric positions
- [ ] Implement `delete_task(number_to_delete)` to remove one task using its list position
- [ ] Implement `save_todos()` to persist tasks into `todos.csv`
- [ ] Implement `load_todos()` to read tasks from `todos.csv` back into memory
- [ ] Ensure users can add as many tasks as needed in the same run
- [ ] Ensure the app runs entirely from the command line and behaves like the provided preview

⚠️ **IMPORTANT:** Use only Python standard library tools for file I/O and CLI interaction in this project version.

---

## ✅ What We Will Evaluate

- [ ] `add_one_task(title)` correctly appends new tasks to the active list
- [ ] `print_list()` outputs tasks in order with positions users can reference
- [ ] `delete_task(number_to_delete)` removes the intended task and handles list updates correctly
- [ ] `save_todos()` writes current tasks into `todos.csv` in a reusable format
- [ ] `load_todos()` reconstructs tasks from `todos.csv` correctly
- [ ] CLI behavior is consistent with the required flow: create, list, delete, save, and load

> Note: Task editing (update-in-place) is out of scope for this exercise.

---

## 📦 How to Submit

Push your solution to your own GitHub repository and share the repository URL according to your instructor's instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/exercise-todo-list-cli-python/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
