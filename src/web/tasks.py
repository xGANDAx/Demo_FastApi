"""
Module
"""

from fastapi import APIRouter
from service import service
from model.tasks import Task

task_router = APIRouter(prefix="/tasks")


@task_router.post("", status_code=201)
@task_router.post("/", status_code=201)
async def create_task(task: Task):
    """
    Funtion that create a task.
    """
    return service.create_task(task)


@task_router.get("/{task_id}", status_code=200)
async def get_one_task(task_id):
    """
    Function that return a task.
    """
    return service.get_one_task(task_id)


@task_router.get("", status_code=200)
@task_router.get("/", status_code=200)
async def get_all_tasks():
    """
    Function that return a task.
    """
    return service.get_all_task()
