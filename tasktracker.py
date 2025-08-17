import json

# Task class definition
class task:
    def __init__(self, description, dueDate, completed=False):
        self.description = description
        self.dueDate = dueDate
        self.completed = completed

    def __str__(self):
        # String representation for printing a task
        return f"Description: {self.description}\n Due: {self.dueDate}\n Completed: {self.completed}"

    def to_dict(self):
        # Convert task object to dictionary for JSON serialization
        return {
            "description": self.description,
            "dueDate": self.dueDate,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        # Create a task object from a dictionary (used when loading from JSON)
        return task(data["description"], data["dueDate"], data["completed"])

# List to store all tasks
tasks = []

def display_tasks(tasks):
    # Display all tasks with their index
    for idx, task_obj in enumerate(tasks, start=1):
        print(" ")
        print(f"Task {idx}:")
        print(task_obj)

def add_task(description, dueDate):
    # Add a new task to the tasks list
    new_task = task(description, dueDate)
    tasks.append(new_task)
    print(f"Added task: {new_task.description}")

def remove_task():
    # Remove a task by its index
    display_tasks(tasks)
    to_remove = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= to_remove < len(tasks):
        removed_task = tasks.pop(to_remove)
        print(f"Removed task: {removed_task.description}")
    else:
        print("Invalid task number.")

def mark_task_completed():
    # Mark a task as completed by its index
    display_tasks(tasks)
    to_mark = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= to_mark < len(tasks):
        tasks[to_mark].completed = True
        print(f"Marked task '{tasks[to_mark].description}' as completed.")
    else:
        print("Invalid task number.")

def mark_task_in_progress():
    # Mark a task as in progress (not completed) by its index
    display_tasks(tasks)
    to_mark = int(input("Enter the number of the task to mark as in progress: ")) - 1
    if 0 <= to_mark < len(tasks):
        tasks[to_mark].completed = False
        print(f"Marked task '{tasks[to_mark].description}' as in progress.")

def update_task_info():
    # Update the information of a task by its index
    display_tasks(tasks)
    to_update = int(input("Enter the number of the task to update: ")) - 1
    if 0 <= to_update < len(tasks):
        description = input("Enter new description (leave blank to keep current): ")
        dueDate = input("Enter new due date (DD-MM-YYYY) (leave blank to keep current): ")
        completed_input = input("Is the task completed? (yes/no) (leave blank to keep current): ")
        if description:
            tasks[to_update].description = description
        if dueDate:
            tasks[to_update].dueDate = dueDate
        if completed_input.lower() == 'yes':
            tasks[to_update].completed = True
        elif completed_input.lower() == 'no':
            tasks[to_update].completed = False
        print(f"Updated task '{tasks[to_update].description}'.")
    else:
        print("Invalid task number.")

def update_task():
    # Menu for updating tasks
    selection2 = 0
    while selection2 != 4:
        print(" ")
        print("1. Update task information")
        print("2. Mark task as in progress")
        print("3. Mark task as completed")
        print("4. Back to main menu")
        print(" ")
        selection2 = int(input("Select an option: "))
        if selection2 == 1:
            update_task_info()
        elif selection2 == 2:
            mark_task_in_progress()
        elif selection2 == 3:
            mark_task_completed()
        elif selection2 == 4:
            print("Returning to main menu.")
        else:
            print("Invalid selection. Please try again.")

def save_tasks_to_file(filename):
    # Save all tasks to a JSON file
    with open(filename, 'w') as file:
        json.dump([t.to_dict() for t in tasks], file, indent=4)

def load_tasks_from_file(filename):
    # Load tasks from a JSON file
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if not content:
                print("No saved tasks found.")
                return
            data = json.loads(content)
            for item in data:
                tasks.append(task.from_dict(item))
    except FileNotFoundError:
        print("No saved tasks found.")
    except json.JSONDecodeError:
        print("Corrupted or invalid JSON file.")










# Main program loop
selection = 0


load_tasks_from_file('tasks.json')

while selection != 5:
    print(" ")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Update a task")
    print("5. Exit")
    print(" ")
    selection = int(input("Select an option: "))

    if selection == 1:
        # Add a new task
        description = input("Enter task description: ")
        dueDate = input("Enter due date (DD-MM-YYYY): ")
        add_task(description, dueDate)
    elif selection == 2:
        # View tasks submenu
        slection1 = 0
        while slection1 != 4:
            print(" ")
            print("1. View all tasks \n2. View all completed tasks \n3. View all pending tasks \n4. Back to main menu")
            slection1 = int(input("Select an option: "))
            if slection1 == 1:
                print("Viewing all tasks:")
                display_tasks(tasks)
            elif slection1 == 2:
                print("Viewing completed tasks:")
                completed_tasks = [task for task in tasks if task.completed]
                display_tasks(completed_tasks)
            elif slection1 == 3:
                print("Viewing pending tasks:")
                pending_tasks = [task for task in tasks if not task.completed]
                display_tasks(pending_tasks)
            elif slection1 == 4:
                print("Returning to main menu.")
            else:
                print("Invalid selection. Please try again.")

    elif selection == 3:
        remove_task()

    elif selection == 4:
        update_task()
        
    elif selection == 5:
        save_tasks_to_file('tasks.json')
        print("Tasks saved. Exiting.")
    else:
        print("Invalid selection. Please try again.")

# Save tasks to file at program end
save_tasks_to_file('tasks.json')
# Optionally reload to verify save (not usually needed)
load_tasks_from_file('tasks.json')

