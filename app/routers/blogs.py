from fastapi import APIRouter, Query, Depends, Form, Path
from fastapi.responses import Response
from fastapi.responses import Response, JSONResponse
# from sqlalchemy import text

from app.models.Blogs import Blogs
from app.models.Categories import Categories
from ..schemas.blogs.BlogsSchema import BlogsSchema

from configs.database import  get_db
from core.api_response.api_response import ApiResponse

# Create your routes here

router = APIRouter(tags=["Blogs"])

# Categories Section

@router.get("/all-category/", description="Get All Category")
async def all_category(
    pg_conn = Depends(get_db)
):
    
    data= pg_conn.query(Categories).all()
    return data
    # response = ApiResponse.response(status_code=200, status="SUCCESS", message="Successful fetch blogs!",
                                   # data= data)
    # return response


@router.post("/post-category/", description="Create New category")
async def post_category(
    name: str = Form(title="Category Name", description="please specify category name"),
    pg_conn = Depends(get_db)
):
    
    new_blog = Categories(name=name)
    pg_conn.add(new_blog)
    pg_conn.commit()
    response = ApiResponse.response(status_code=201, status="SUCCESS", message="Successful create category`!")
    return response
    # response = ApiResponse.response(status_code=200, status="SUCCESS", message="Successful fetch blogs!",
                                   # data= data)
    # return response


# Blogs Section 

@router.get("/all-blogs/<slug>", description="Get All Blogs")
async def all_blogs(
    pg_conn = Depends(get_db)
):

    data= pg_conn.query(Blogs).all()
    return data
    # response = ApiResponse.response(status_code=200, status="SUCCESS", message="Successful fetch blogs!",
                                   # data= data)
    # return response


@router.get("/get-blog/{slug}", description="Get Blog Details")
async def get_blog(
    slug: str = Path(title="Get Path Parameter"),
    pg_conn = Depends(get_db)
):
    
    data= pg_conn.query(Blogs).filter(Blogs.title == slug).all()
    return data
    # response = ApiResponse.response(status_code=200, status="SUCCESS", message="Successful fetch blogs!",
                                   # data= data)
    # return response


@router.post("/blog-post/", description="Create New Blog")
async def blog_post(
    blog_post: BlogsSchema,
    pg_conn = Depends(get_db),
):
    
    new_blog = Blogs(title=blog_post.title, content=blog_post.content, author_id= blog_post.author_id, 
                     category_id=blog_post.category_id)
    
    pg_conn.add(new_blog)
    pg_conn.commit()
    response = ApiResponse.response(status_code=201, status="SUCCESS", message="Successful create blog!")
    return response

