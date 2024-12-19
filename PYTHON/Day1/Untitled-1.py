def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def add_task(todo_list):
    task_desc = input("Enter the task description: ").strip()
    if not task_desc:
        print("Task description cannot be empty!")
        return
    task = {"Description": task_desc, "Completed": False}
    todo_list.append(task)
    print(f"Task '{task_desc}' added successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list!")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(todo_list, start=1):
        status = "Completed" if task["Completed"] else "Not Completed"
        print(f"{idx}. {task['Description']} - {status}")

def mark_task_completed(todo_list):
    if not todo_list:
        print("No tasks available to mark as completed!")
        return
    view_tasks(todo_list)
    try:
        task_no = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]["Completed"] = True
            print(f"Task '{todo_list[task_no - 1]['Description']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(todo_list):
    if not todo_list:
        print("No tasks available to delete!")
        return
    view_tasks(todo_list)
    try:
        task_no = int(input("Enter the task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            removed_task = todo_list.pop(task_no - 1)
            print(f"Task '{removed_task['Description']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_task_completed(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()