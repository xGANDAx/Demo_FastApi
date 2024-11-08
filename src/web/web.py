from fastapi import APIRouter

router = APIRouter() 

@router.get("")
@router.get("/")
async def hello_world():
    return "Hello, World!"

