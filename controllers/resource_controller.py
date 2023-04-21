from fastapi import APIRouter, HTTPException, types

resource_router = APIRouter()


@resource_router.get("/api/v1/hello")
async def get_hello():
    return {"message": "Hello World!"}