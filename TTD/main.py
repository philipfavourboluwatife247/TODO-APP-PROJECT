#!/usr/bin/python3

# main.py by Paul John
"""main script Terminal Terminal ToDo (TTD) App"""

from sys import argv
# import terminal todo app module
from ttd import Task, TTD


if __name__ == "__main__":

    # Create tasks
    task1 = Task("This is my first task", "Today 6am")
    task2 = Task("This is my second task", "Today 9am")
    task3 = Task("This is my last task", "Today Allday")

    # Create new Terminal ToDo List
    todo_list = TTD()

    # Add tasks in ToDo List
    todo_list.add_task(task1)
    todo_list.add_task(task2)
    todo_list.add_task(task3)

    # print all current tasks
    todo_list.print_tasks()
    print()

    # Mark task as completed [x]
    task1.mark_completed()
    todo_list.print_tasks()
    print()

    # Remove tasks from ToDo List
    todo_list.remove_task(task1)
    todo_list.print_tasks()
