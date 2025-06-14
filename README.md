<!--hide-->
# Todo's List CLI (Command Line Interface)
<!--endhide-->

<p align="center">
  <img height="200" src="https://github.com/breatheco-de/exercise-todo-list-cli-python/blob/master/preview.gif?raw=true" />
</p>

Create a TODO list application that allows users to add and delete tasks from the command line.

<onlyfor saas="false" withBanner="false">
  
## 🌱  How to start this project

a) Open this link in your browser with [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended) or [Gitpod](https://4geeks.com/lesson/how-to-use-gitpod): https://github.com/codespaces/new/?repo=4GeeksAcademy/python-hello

b) You can clone this repository on your local computer:

```bash
$ git clone https://github.com/4GeeksAcademy/python-hello
```

### Steps

- If working locally, you should have python [installed](https://4geeks.com/how-to/how-to-install-python).

- You should open the terminal on the path of this template and run `$ python3 app.py`, if everything works correctly, it should show `Hello World` on the terminal.

- You can test your code by typing: `$ python3 test.py`.

💡 Important: Remember to create a new repository, update the remote (`git remote set-url origin <your new url>`), and upload the code to your new repository using `add`, `commit` and `push`.

</onlyfor>

## 📝 Instructions

These are the functions you will have to implement:

```python
def add_one_task(title):
def print_list():
def delete_task(number_to_delete):
def save_todos():
def load_todos():
```

- You app needs to work from the the command line [like this](https://4geeks.com/interactive-coding-tutorial/todo-list-cli-python).
- The user should be able to add new tasks
- The user can add as many tasks as he/she wants.
- The user can delete tasks by specifying the task position in the list.
- The user can save the todos to a `todos.csv` file
- The user can retrieve the todos from a `todos.csv` file
- There is no way to update a task, the user will have to delete and create again.
