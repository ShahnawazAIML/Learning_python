to_do = {
    1 : ["Build ",False],
    2 : ["Build something",False],
    3 : ["in python",False],
    4 : ["Build  an to do list",False]
}

def add():
    task_text = input("Enter your task: ").strip()
    if not task_text:
        print("Task cannot be empty!")
        return
    next_id = max(to_do.keys(), default=0) + 1
    to_do[next_id] = [task_text, False]
    print("Task added!")

def delete():
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        if task_id in to_do:
            del to_do[task_id]
            print("Task deleted!")
        else:
            print("Task ID not found!")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")


def showAll(): 
    for i in range(1, len(to_do) + 1):
        print(f"{i} : {to_do.get(i)[0]} ---> status: {to_do.get(i)[1]}")


def ask():
    while True:
        user = input("User--> ").strip().lower()
        if user == "show":
            showAll()
        elif user == "add":
            add()
        elif user == "exit":
            print("Exiting...")
            break
        elif user == "delete":
            delete()
        else:
            print("Invalid value. Try 'show', 'add', or 'exit', 'delete'.")

ask()