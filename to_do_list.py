to_do = [
    ["Build ",False],
    ["Build something",False],
    ["in python",False],
    ["Build  an to do list",False]
]


def add():
    try:
        new_task = input("What is your  new Task: ")
        status = False
        add = to_do.append([new_task,status])
        print("Task added")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def delete():
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        if True:
            del to_do[task_id - 1]
            print("Task deleted!")
        else:
            print("Task ID not found!")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def edit():
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        edit_to_do = input("Write new to do here: ")
        to_do[task_id - 1][0] = edit_to_do
        print("Task Edited")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def mark():
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        edit_to_do = input("Have this task done(type -> y/n): ")
        if edit_to_do == "y" or edit_to_do == "n":
            if edit_to_do == "y":
                to_do[task_id - 1][1] = True
                print("Task marked as done")
            else:
                to_do[task_id - 1][1] = False
                print("Task marked as Not done")
        else:
            mark()
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def showAll():
    if not to_do:
        print("No tasks available")
        return
    for idx, task in enumerate(to_do, start=1):
        status = "Done" if task[1] else "Not Done"
        print(f"{idx} : {task[0]} ---> Status : {status}")

def all():
    try:
        to_do.clear()
        print("All tasks Deleted.")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def ask():
    while True:
        user = input("User--> ").strip().lower()
        if user == "show":
            showAll()
        elif user == "add":
            add()
        elif user == "mark":
            mark()
        elif user == "edit":
            edit()
        elif user == "exit":
            print("Exiting...")
            break
        elif user == "delete":
            delete()
        elif user == "delete all":
            all()
        else:
            print("Invalid value. Try 'show', 'add', or 'exit', 'delete'.")

ask()