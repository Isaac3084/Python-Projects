def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks(tasks)

def delete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number to delete: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def to_do_list():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
to_do_list()
