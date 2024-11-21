"""
Main module that runs the app.

This module contains the following routes:
- / (hello_world)
- /health (health_check)
"""

from fastapi import FastAPI
from web.tasks import task_router

app = FastAPI()

app.include_router(task_router)


@app.get("")
@app.get("/")
async def hello_world():
    """
    Method that returns a welcome message
    """
    return {
        "message": "Hello, World!",
    }


@app.get("/health", status_code=200)
async def health():
    """
    Method that returns a health message.
    """
    return {
        "message": "Health is OK",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
