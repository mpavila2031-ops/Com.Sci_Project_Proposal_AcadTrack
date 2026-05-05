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

task_list = []


def ShowMenu():
    print("\n===== ACADTRACK MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def GetText(msg):
    while True:
        text = input(msg).strip()
        if text == "":
            print("Input cannot be empty. Please try again.")
        else:
            return text

def GetDate():
    while True:
        date_text = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

def GetType():
    while True:
        print("\nChoose task type:")
        print("1. Assignment")
        print("2. Quiz")
        print("3. Project")
        print("4. Exam")

def AddTask():
    print("\n===== ADD TASK =====")
    subject = GetText("Enter subject: ")
    name = GetText("Enter task name: ")
    task_type = GetType()
    due = GetDate()
    
task = {
        "subject": subject,
        "name": name,
        "type": task_type,
        "due": due,
        "status": "Pending"}

task_list.append(task)
    print("Task added successfully.")

def ViewTasks():
    print("\n===== TASK LIST =====")

    if len(task_list) == 0:
        print("No tasks available.")
        return []


     sorted_list = sorted(task_list, key=lambda x: x["due"])

    for i, task in enumerate(sorted_list, 1):
        print(f"\nTask #{i}")
        print(f"Subject : {task['subject']}")
        print(f"Task    : {task['name']}")
        print(f"Type    : {task['type']}")
        print(f"Due     : {task['due']}")
        print(f"Status  : {task['status']}")

    return sorted_list


def MarkDone():
    print("\n===== MARK TASK AS COMPLETED =====")

    if len(task_list) == 0:
        print("No tasks available.")
        return

    sorted_list = ViewTasks()

    while True:
        num = input("\nEnter task number to mark as completed: ").strip()

        if not num.isdigit():
            print("Please enter a valid number.")
            continue

        num = int(num)

        if 1 <= num <= len(sorted_list):
            sorted_list[num - 1]["status"] = "Completed"
            print("Task marked as completed.")
            break
        else:
            print("Task number is out of range.")

def DeleteTask():
    print("\n===== DELETE TASK =====")

    if len(task_list) == 0:
        print("No tasks available.")
        return

    sorted_list = ViewTasks()

    while True:
        num = input("\nEnter task number to delete: ").strip()

        if not num.isdigit():
            print("Please enter a valid number.")
            continue

        num = int(num)

        if 1 <= num <= len(sorted_list):
            task_list.remove(sorted_list[num - 1])
            print("Task deleted successfully.")
            break
        else:
            print("Task number is out of range.")








    



