"""
Module containing the tests for the main application module.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_hello_world():
    """
    Test for the `get` method on the route "/"
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_health_check():
    """
    Test for the `get` method on the route "/health"
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Health is OK"}
