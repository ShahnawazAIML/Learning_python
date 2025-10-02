to_do = {
    1 : ["Build ",False],
    2 : ["Build something",False],
    3 : ["in python",False],
    4 : ["Build  an to do list",False]
}
total_task = len(to_do)


def add():
    next_id = max(to_do.keys()) + 1
    to_do.update({next_id: ["Hi I'm a new task", False]})
    print("New task added")




def showAll(): 
    for i in range(1, total_task + 1):
        print(f"{i} : {to_do.get(i)[0]} ---> ststus: {to_do.get(i)[1]}")


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
        else:
            print("Invalid value. Try 'show', 'add', or 'exit'.")

ask()