class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the To-Do list.")

    def mark_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task '{self.tasks[index]['task']}' marked as completed.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("Your To-Do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i + 1}. {task['task']} - {status}")

    def clear_list(self):
        self.tasks = []
        print("To-Do list cleared.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Clear To-Do List")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_as_completed(index)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            todo_list.clear_list()
        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
