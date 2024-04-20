from fastapi import APIRouter
from .routers.blogs import router as blog_router

api_router = APIRouter()

api_router.include_router(blog_router, prefix="/blogs")
