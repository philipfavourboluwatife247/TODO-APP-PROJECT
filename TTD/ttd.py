#!/usr/bin/python3

# ttd.py by Paul John
"""Terminal ToDo App (TTD) module"""

class Task(object):
    """Terminal ToDo App Task Class"""
    
    def __init__(self, description=None, due_date=None):
        """Initializes a Task in TTD"""

        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return (f"{status} {self.description} \t| Due: {self.due_date}")


class TTD(object):
    """Terminal ToDo List Class"""

    def __init__(self, task=None):
        """Initializes a TTD List"""
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def print_tasks(self):
        for task in self.tasks:
            print(task)


if __name__ == "__main__":
    # print("This is only to be used as a module for main.py script.")

    task1 = Task("This is my first task", "Today 6am")
    task2 = Task("This is my second task", "Today 9am")
    task3 = Task("This is my last task", "Today Allday")

    # create new Terminal ToDo List
    todo_list = TTD()

    todo_list.add_task(task1)
    todo_list.add_task(task2)
    todo_list.add_task(task3)

    todo_list.print_tasks()
    print()

    task1.mark_completed()

    todo_list.print_tasks()
    print()
    todo_list.remove_task(task1)
    todo_list.print_tasks()
