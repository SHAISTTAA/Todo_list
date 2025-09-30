import os

# Define the file where tasks will be saved
TODO_FILE = "todos.txt"
todo_list = []

def load_tasks():
    """Loads tasks from the file (if it exists) into the todo_list."""
    global todo_list
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            # Read each line, remove the newline character, and add to the list
            todo_list = [line.strip() for line in f.readlines()]
        print(f"Tasks loaded from {TODO_FILE}.")
    else:
        print("No existing task file found. Starting fresh!")

def save_tasks():
    """Saves the current todo_list to the file."""
    with open(TODO_FILE, 'w') as f:
        # Write each task on a new line
        for task in todo_list:
            f.write(task + '\n')

def view_tasks():
    """Displays all tasks with their index number."""
    if not todo_list:
        print("\nYour To-Do List is EMPTY! 🎉")
    else:
        print("\n--- Your To-Do List ---")
        # Loop through the list and print the index (starting from 1) and the task
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")
        print("-----------------------\n")

def add_task():
    """Prompts the user for a new task and adds it to the list."""
    task = input("Enter the new task: ").strip()
    if task:
        todo_list.append(task)
        save_tasks()
        print(f"✅ Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def delete_task():
    """Prompts for an index and deletes the corresponding task."""
    view_tasks()
    if todo_list:
        try:
            # Get the task number from the user
            task_num = int(input("Enter the NUMBER of the task to delete: "))
            
            # Convert the user's number (1-based) to a list index (0-based)
            task_index = task_num - 1
            
            # Check if the index is valid
            if 0 <= task_index < len(todo_list):
                removed_task = todo_list.pop(task_index)
                save_tasks()
                print(f"❌ Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """The main function that runs the application loop."""
    load_tasks() # Load tasks when the app starts
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit and Save")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            save_tasks() # Save one last time before exiting
            print("To-Do list saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Standard way to run the main function when the script is executed
if __name__ == "__main__":
    main()