"""
Module
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
@router.get("/")
async def hello_world():
    """
    Funtion that returns a "Hello, World!" message.
    """
    return "Hello, World!"
