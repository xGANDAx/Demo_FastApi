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


def get_one_task(task_id):
    """
    Function that returns a Task.
    """
    return tasks.get_one_task(task_id)


def get_all_task():
    """
    Function that returns a Task.
    """
    return tasks.get_all_task()
