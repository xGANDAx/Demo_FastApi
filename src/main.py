"""
Main module that runs the app.

This module contains the following routes:
- / (hello_world)
- /health (health_check)
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("")
@app.get("/")
async def hello_world():
    """
    Method that returns a welcome message.
    """
    return {
        "message": "Hello, World!",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
