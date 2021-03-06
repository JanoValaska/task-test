# Todo: Alter the complete_tasks method so that it only calls 'complete' on
#           non-completed task.
#       Add a remove_task method that removes only one task by id
#
#       Upon calling complete() on a task, set _value of that task object to the number of occurrences of the
#           string "CCN" (case in-sensitive) that appears in the task's name.
#
#       Fix the Task object id, so that it is unique for each new task.
#       Fix other bugs.

# Note: - you cannot edit/change the TaskManager class
#       - You can create new objects, etc


class Task(object):

    def __init__(self, name):
        self._id = 0
        self._name = name
        self._value = None
        self._completed = False

    def complete(self):
        _completed = True

    @property
    def is_completed(self):
        return self._completed

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value


# This class cannot be edited directly
class TaskManager(object):

    def __init__(self):
        self.tasks = []

    def import_task(self, task):
        self.tasks.append(task)

    def complete_tasks(self):
        if len(self.tasks) > 0:
            if not all([task.is_completed for task in self.tasks]):
                for task in self.tasks:
                    task.complete()
                    print('task {name} completed'.format(name=task.name))

    def remove_tasks(self):
        while len(self.tasks) > 0:
            self.tasks.pop()
