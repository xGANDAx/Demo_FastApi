"""
Module
"""

from fastapi import APIRouter
from service import service
from model.tasks import Task

task_router = APIRouter(prefix="/tasks")


@task_router.post("/create")
async def create_task(task: Task):
    """
    Funtion that create a task.
    """
    return service.create_task(task)