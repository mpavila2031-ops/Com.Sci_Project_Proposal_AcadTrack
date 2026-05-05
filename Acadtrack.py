"""
project Title: Acadtrack - A Student Academic Deadline Tracker
group Members:
- Mhai Princess Kayeshea Avila
- Liam Isaac Sudario
- Alfonso Ace Magdaluyo

Brief description: 
AcadTrack is a simple Python Program that helps students track their
academic tasks such as assignments, quizzes, projects, and exams.
It allows the user to add tasks, view tasks, mark tasks as completed, 
and delete tasks.
"""

from datetime import datetime

# This list stores all tasks entered by the user
task_list = []


# This function displays the main menu
def ShowMenu():
    print("\n===== ACADTRACK MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# This function gets non-empty text input from the user
def GetText(msg):
    while True:
        text = input(msg).strip()
        if text == "":
            print("Input cannot be empty. Please try again.")
        else:
            return text

# This function gets and validates the due date
def GetDate():
    while True:
        date_text = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


# This function lets the user choose a valid task type
def GetType():
    while True:
        print("\nChoose task type:")
        print("1. Assignment")
        print("2. Quiz")
        print("3. Project")
        print("4. Exam")
        
         choice = input("Enter choice (1-5): ").strip()

        # Decision statements for task type selection
        if choice == "1":
            return "Assignment"
        elif choice == "2":
            return "Quiz"
        elif choice == "3":
            return "Project"
        elif choice == "4":
            return "Exam"
        elif choice == "5":
            return "Other"
        else:
            print("Invalid choice. Please try again.")

# This function adds a new task to the task list
def AddTask():
    print("\n===== ADD TASK =====")

    # Get task details from the user
    subject = GetText("Enter subject: ")
    name = GetText("Enter task name: ")
    task_type = GetType()
    due = GetDate()

# Create a dictionary for one task
task = {
        "subject": subject,
        "name": name,
        "type": task_type,
        "due": due,
        "status": "Pending"}

# Add the task to the main list
task_list.append(task)
    print("Task added successfully.")

# This function displays all tasks sorted by due date
def ViewTasks():
    print("\n===== TASK LIST =====")

    # Check if there are no tasks yet
    if len(task_list) == 0:
        print("No tasks available.")
        return []

    # Sort tasks by due date
     sorted_list = sorted(task_list, key=lambda x: x["due"])

    # Display each task with numbering
    for i, task in enumerate(sorted_list, 1):
        print(f"\nTask #{i}")
        print(f"Subject : {task['subject']}")
        print(f"Task    : {task['name']}")
        print(f"Type    : {task['type']}")
        print(f"Due     : {task['due']}")
        print(f"Status  : {task['status']}")

    return sorted_list


# This function marks a selected task as completed
def MarkDone():
    print("\n===== MARK TASK AS COMPLETED =====")

    # Check if there are tasks available
    if len(task_list) == 0:
        print("No tasks available.")
        return
    
    # Show sorted task list first
    sorted_list = ViewTasks()

    while True:
        num = input("\nEnter task number to mark as completed: ").strip()

        # Validate if input is a number
        if not num.isdigit():
            print("Please enter a valid number.")
            continue

        num = int(num)

        # Check if the chosen number is within range
        if 1 <= num <= len(sorted_list):
            sorted_list[num - 1]["status"] = "Completed"
            print("Task marked as completed.")
            break
        else:
            print("Task number is out of range.")

# This function deletes a selected task
def DeleteTask():
    print("\n===== DELETE TASK =====")

    # Check if there are tasks available
    if len(task_list) == 0:
        print("No tasks available.")
        return

    # Show sorted task list first
    sorted_list = ViewTasks()

    while True:
        num = input("\nEnter task number to delete: ").strip()

        # Validate if input is a number
        if not num.isdigit():
            print("Please enter a valid number.")
            continue

        num = int(num)

        # Check if the chosen number is within range
        if 1 <= num <= len(sorted_list):
            task_list.remove(sorted_list[num - 1])
            print("Task deleted successfully.")
            break
        else:
            print("Task number is out of range.")

# This is the main function that runs the whole program
def Main():
    print("Welcome to AcadTrack")

    # Main loop of the program
    while True:
        ShowMenu()
        choice = input("Enter your choice (1-5): ").strip()

        # Menu choices
        if choice == "1":
            AddTask()
        elif choice == "2":
            ViewTasks()
        elif choice == "3":
            MarkDone()
        elif choice == "4":
            DeleteTask()
        elif choice == "5":
            print("Thank you for using AcadTrack.")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")

# Start the program
Main()




    



