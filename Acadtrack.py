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
  print("1. Add task")
