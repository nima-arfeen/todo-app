class TodoApp:
    def __init__(self):
        #dictionary structure 
        self.todo_list = {}

    # function to add a task
    # input: task description and priority
    # step 1) if priority is not a valid positive integer -> notify and return
    # step 2) if the priority already exists -> overwrite the task and notify user
    # step 3) then -> add the task and notify user
    def add_item(self):
        task = input("Enter description for task: ").strip()
        priority_input = input("Enter priority as positive integer: ").strip()
        # 1)
        if not priority_input.isdigit() or int(priority_input) <= 0:
            print("Invalid, enter priority as positive integer.")
            return
        priority = int(priority_input)
        # 2)
        if priority in self.todo_list:
            print(f"A task already exists with priority {priority}. Overwriting it.")
        # 3)
        self.todo_list[priority] = task
        print("Task added!")

    # function to delete a task
    # input: priority of the task to delete
    # step 1) if input isnt an integer -> notify user and return
    # step 2) if task with priority exists -> delete it and notify deleted
    # step 3) else (task doesnt exist) -> notify user
    def delete_item(self):
        priority_input = input("Enter priority of task to delete: ").strip()
        # 1)
        if not priority_input.isdigit():
            print("Invalid input.")
            return
        priority = int(priority_input)
        # 2)
        if priority in self.todo_list:
            del self.todo_list[priority]
            print(f"Task with priority {priority} deleted.")
        # 3)
        else:
            print("No task found with that priority.")

    # function to list all tasks
    # if no tasks exist -> notify user and return
    # else -> list (sort by priority)
    def list_items(self):
        if not self.todo_list:
            print("No tasks yet.")
            return
        print("\nCurrent ToDo List:")
        for priority in sorted(self.todo_list):
            print(f"[Priority {priority}] {self.todo_list[priority]}")

    # function to show missing priorities
    # if no tasks exist -> notify user and return
    # else -> find missing ones and list for user
    def missing_priorities(self):
        if not self.todo_list:
            print("No tasks yet.")
            return
        existing = sorted(self.todo_list.keys())
        missing = []

        # highest_priority is used to find missing priorities
        highest_priority = max(existing) 
        for i in range(1, highest_priority):
            if i not in self.todo_list:
                missing.append(i)

        if missing:
            missing_string_form = map(str, missing)
            print("Missing priorities:", ', '.join(missing_string_form))
        else:
            print("No missing priorities.")

    # main loop
    def run(self):
        while True:
            print("\n--- TODO APP OPTIONS ---")
            print("1. Add item")
            print("2. Delete item")
            print("3. List items")
            print("4. Show missing priorities")
            print("5. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.delete_item()
            elif choice == "3":
                self.list_items()
            elif choice == "4":
                self.missing_priorities()
            elif choice == "5":
                print("Bye!")
                break
            else:
                print("Invalid, try again.")


if __name__ == "__main__":
    app = TodoApp()
    app.run()

