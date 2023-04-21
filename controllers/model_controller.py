from fastapi import APIRouter, HTTPException, types

model_router = APIRouter()


@model_router.get("/api/v1/hello")
async def get_hello():
    return {"message": "Hello World!"}