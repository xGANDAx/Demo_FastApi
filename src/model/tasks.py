"""
Module that defines the application's data model.
"""

from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    """
    Task attributes model.
    """

    task_id: Optional[int] = None
    name: str
    description: str
    status: str
