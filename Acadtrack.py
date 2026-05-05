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



