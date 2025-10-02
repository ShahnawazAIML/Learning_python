to_do = [
    ["Build ",False],
    ["Build something",False],
    ["in python",False],
    ["Build  an to do list",False]
]
# task_id = input("Enter task ID to delete: ").strip()
# edit_to_do = input("Write new to do here: ")
# if task_id in to_do.keys():
#     edit_to_do = input("Write new to do here: ")
#     to_do[task_id] = edit_to_do
#     print(f"Updated task: {to_do[task_id]}")
# else:
#     print("Task ID not found.")

# print(to_do[0][1])

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

def edit():
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        edit_to_do = input("Write new to do here: ")
        # to_do.get(task_id) = edit_to_do
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

a = 0
def showAll(): 
    for idx in range(0, len(to_do) + 1):
        print(f"{idx + 1} : {to_do}")

# def showAll():
#     for idx, (task_id, task_data) in enumerate(to_do.items(), start=1):
#         print(f"{idx} : {task_id} ---> Task: {task_data[idx]} | Status: {task_data[1]}")



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