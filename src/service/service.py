"""
Module with the business logic of the task manager.
"""

from data import tasks
from model.tasks import Task


def create_task(task: Task):
    """
    Function that creates a Task.
    """
    return tasks.create_task(task)
