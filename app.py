todos = ['Clean all', 'Make the bed', 'Clean my room', 'Pay taxes']
stop = False

def add_one_task():
    global todos
    print("What is your task title?")
    todos.append(input())


def print_list():
    global todos
    print("Your current list of tasks ("+str(len(todos))+"):")
    count = 1
    for t in todos:
        print(" "+str(count)+". "+t)
        count = count + 1

def delete_task():
    global todos
    new_todos = []
    print("What task number you want to delete?")
    number_to_delete = int(input()) - 1
    for i in range(0,len(todos)):
        if str(i) != str(number_to_delete):
            new_todos.append(todos[i])

    todos = new_todos

while stop == False:
    print("""
Choose an option: 
    1. Add one task
    2. Delete a task
    3. Print the current list of tasks
    4. Exit
""")
    response = input()
    if response == "4":
        stop = True
    elif response == "3":
        print_list()
    elif response == "2":
        delete_task()
    elif response == "1":
        add_one_task()
    else:
        print("Invalid response, asking again...")