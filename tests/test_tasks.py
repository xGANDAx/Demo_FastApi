"""
Module that contains the tests for the task manager application.
"""

from .init import client


class TestTasks:

    task_data = {"name": "test", "description": "test", "status": "test"}

    def test_create_task(self):
        """
        Test for the `post` method on the route "/tasks".
        """
        response = client.post("/tasks", json=self.task_data)
        assert response.status_code == 201
        assert response.json() == self.task_data | {"task_id": 1}

    def test_get_one_task(self):
        """
        Test for the `get` method on the route "/tasks/{id}".
        """
        response_get = client.get("/tasks/1")
        assert response_get.status_code == 200
        assert response_get.json() == self.task_data | {"task_id": 1}

    def test_get_all_tasks(self):
        """
        Test for the `get` method on the route "/tasks".
        """
        response_get = client.get("/tasks")
        assert response_get.status_code == 200
        assert response_get.json() == [self.task_data | {"task_id": 1}]
