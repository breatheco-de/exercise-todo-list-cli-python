todos = []
stop = False


def get_todos():
    global todos
    return todos


def add_one_task(title):
    global todos
    todos.append(title)


def print_list():
    global todos
    for index, task in enumerate(todos, start=1):
        print(f"{index}. {task}")


def delete_task(number_to_delete):
    global todos
    number_to_delete = int(number_to_delete)
    del todos[number_to_delete - 1]


def save_todos():
    global todos
    file = open("todos.csv", "w")
    file.write("\n".join(todos))
    file.close()


def load_todos():
    global todos
    file = open("todos.csv", "r")
    file_content = file.read()
    file.close()
    if file_content == "":
        todos = []
        return
    todos = file_content.split("\n")
