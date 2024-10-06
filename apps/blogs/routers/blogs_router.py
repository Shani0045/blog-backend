from fastapi import APIRouter, Query, Depends, Form, Path
from fastapi.responses import Response
from fastapi.responses import Response, JSONResponse
# from sqlalchemy import text

from configs.database import  get_db
from core.api_response.api_response import ApiResponse
from core.utils import utils
import json

from apps.blogs.models.Blogs import Blogs
from apps.blogs.models.Categories import Categories
from ..schemas.BlogsSchema import (BlogsRequestSchema, 
                                    BlogsResponseSchema
                                    )

from ..services.blog_service import (get_all_category, 
                                        post_new_category, 
                                        get_all_blogs,
                                        get_blog_details,
                                        post_new_blog
                                        )


# ------------------------------- Create your routes here ------------------------------------

router = APIRouter(tags=["Blogs"])

# ------------------------------- Categories Section -----------------------------------------

@router.get("/all-category/", description="Get All Category")
async def all_category(
    pg_conn = Depends(get_db)
):
    data = await get_all_category(pg_conn)
    return ApiResponse.response(status_code=200, 
                                    status="SUCCESS", 
                                    message="Successful fetch blogs!",
                                    data= data
                                   )
  

@router.post("/post-category/", description="Create New category")
async def post_category(
    name: str = Form(title="Category Name", description="please specify category name"),
    pg_conn = Depends(get_db)
):
    created = await post_new_category(pg_conn, name)
    return ApiResponse.response(status_code=201, 
                                    status="SUCCESS", 
                                    message="Successful create category"
                                    )
   
# ------------------------------- Blogs Section -----------------------------------------------

@router.get("/all-blogs/", description="Get All Blogs")
async def all_blogs(
    pg_conn = Depends(get_db),
    page: int = Query(title="page", default=1, gt=0),
    limit: int = Query(title="Limit", default=10, gt=0),
    category_id: int = Query(title="Category Id", default=None, gte=0),
    search: str = Query(title="Search", default=None, max_length=50),
):
    payload = {"limit": limit, "page": page}

    if category_id:
        payload["category_id"] = category_id
    if search:
        payload["search"] = search
    
    all_blogs = await get_all_blogs(pg_conn, payload)

    return ApiResponse.response(status_code=200, 
                                    status="SUCCESS", 
                                    message="Successful fetch blogs!",
                                    data=all_blogs
                                   )
 
@router.get("/blog-details/{slug}", description="Get Blog Details")
async def get_blog(
    slug: str = Path(title="path parameter"),
    pg_conn = Depends(get_db)
): 
    data = await get_blog_details(pg_conn, slug)
    return ApiResponse.response(status_code=200, 
                                    status="SUCCESS", 
                                    message="Successful fetch blogs!",
                                    data= data
                                   )
   

@router.post("/blog-post/", description="Create New Blog")
async def blog_post(
    blog_post: BlogsRequestSchema,
    pg_conn = Depends(get_db),
):
    created = await post_new_blog(pg_conn, payload=blog_post)
    return ApiResponse.response(status_code=201, 
                            status="SUCCESS", 
                            message="Successful create blog!"
                            )
