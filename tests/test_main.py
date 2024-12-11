"""
Module containing the tests for the main application module.
"""

from .init import client


class TestMain:
    """
    Class that contains the test of the main route.
    """
    
    def test_get_hello_world(self):
        """
        Test for the `get` method on the route "/".
        """
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}

    def test_get_health_check(self):
        """
        Test for the `get` method on the route "/health"
        """
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"message": "Health is OK"}
