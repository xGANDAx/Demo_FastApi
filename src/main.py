from fastapi import FastAPI

app = FastAPI()


@app.get("")
@app.get("/")
async def hello_world():
    return {
        "message": "Hello, World!",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
