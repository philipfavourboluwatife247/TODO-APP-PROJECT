#!/usr/bin/python3

# ttd.py by Paul John
"""Terminal ToDo App (TTD) module"""

class Task(object):
    """Terminal ToDo App Task Class"""
    
    def __init__(self, description=None, due_date=None):
        """Initializes a Task in TTD
        Args:
            description - taks description
            due_date - task due date
        """

        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        """Marks task as completed [x]"""
        self.completed = True

    def __repr__(self):
        """string presentantion of tasks"""
        status = "[x]" if self.completed else "[ ]"
        return (f"{status} {self.description} \t| Due: {self.due_date}")


class TTD(object):
    """Terminal ToDo List Class"""

    def __init__(self, task=None):
        """
        Initializes a TTD List
        Args: task - task object
        """

        self.tasks = []

    def add_task(self, task, priority=0):
        """
        Adds a task to ToDo List
        """
        self.tasks.append({'Description': task, 'Priority': priority})
        self.tasks = sorted(self.tasks, key=lambda x: x['Priority'])

    def remove_task(self, task):
        """
        Removes a task from ToDo List
        """
        self.tasks.remove(task)

    def print_tasks(self):
        """Prints sorted tasks"""
        for task in self.tasks:
            print(f"{task['Description'].description:<25} | {task['Description'].due_date:<15} | Priority: {task['Priority']:>1}")

    def __repr__(self):
        return '\n'.join(str(task) for task in self.tasks)


if __name__ == "__main__":
    print("This is a module to be used in main.py script.")
