tasks = []
def add_task(task):
    tasks.append(task)

def view_tasks():
    for task in tasks:
        print(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found in the list.")

while True:
    print("\n1. Add a task.")
    print("2. View Tasks.")
    print("3. Remove a task.")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task = input("Enter the task you want to remove: ")
        remove_task(task)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option. ") 
