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


def update_task(task_id: int, task_info: Task):
    """
    Function that update a Task.
    """
    task = get_one_task(task_id).model_dump()
    new_task_info = task_info.model_dump()

    for field in new_task_info:
        if new_task_info[field] is not None:
            task[field] = new_task_info[field]

    return tasks.update_task(task)
