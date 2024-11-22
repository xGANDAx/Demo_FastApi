"""
Module that contains the tests for the task manager application.
"""

from .init import client


def test_create_task():
    """
    Test for the `post` method on the route "/tasks".
    """
    task_data = {"name": "test", "description": "test", "status": "test"}

    response = client.post("/tasks", json=task_data)
    assert response.status_code == 201
    assert response.json() == task_data | {"task_id": 1}
