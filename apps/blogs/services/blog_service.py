
from apps.blogs.models.Categories import Categories
from apps.blogs.models.Blogs import Blogs
from apps.blogs.models.Comments import Comments
from sqlalchemy import desc
from core.utils.utils import get_offset, generate_slug, calculate_total_pages


async def get_all_category(pg_conn) -> list:
     data= pg_conn.query(Categories).all()
     return data


async def post_new_category(pg_conn, name: str) -> bool:
    new_blog = Categories(name=name)
    pg_conn.add(new_blog)
    pg_conn.commit()
    return True

async def get_all_blogs(pg_conn, payload:  dict) -> list:
    category_id = payload.get("category_id")
    limit = payload.get("limit", 10)
    page = payload.get("page", 1)
    search = payload.get("search")

    offset = get_offset(limit=limit, page_number=page)

    data = pg_conn.query(
                            Blogs.id,
                            Blogs.title, 
                            Blogs.slug, 
                            Blogs.meta_desc, 
                            Blogs.created_at,
                            Categories.name
                            ).join(Blogs, Categories.id==Blogs.category_id)
    

    if category_id:
        data = data.filter(Blogs.category_id == category_id)

    if search:
        data = data.filter(Blogs.title.ilike(f"%{search}%"))

    total_count = data.count()
    total_page = calculate_total_pages(total_count, limit)

    data = data.order_by(desc("id")).offset(offset).limit(limit)
    all_blogs = [ 
            {
                "id": blog[0],
                "title": blog[1],
                "slug": blog[2],
                "meta_desc": blog[3],
                "created_at": blog[4],
                "category": blog[5]
             } 
             
            for blog in data ]
    

    return {"blogs": all_blogs, "total_page": total_page}


async def get_blog_details(pg_conn, slug: str) -> dict:
    data= pg_conn.query(Blogs).filter(Blogs.slug == slug).all()
    return data


async def post_new_blog(pg_conn, payload: dict) -> bool:
    slug = generate_slug(payload.title)
    new_blog = Blogs(title=payload.title, 
                     content=payload.content, 
                     author_id= payload.author_id, 
                     category_id=payload.category_id,
                     slug=slug,
                     meta_desc=payload.meta_desc
                     )
    
    pg_conn.add(new_blog)
    pg_conn.commit()
    return True


async def post_new_comment(pg_conn, payload: dict) -> bool:
    new_comment = Comments(
                     content=payload.content, 
                     user_id= payload.user_id,  
                     blog_id=payload.blog_id,
                     )
    pg_conn.add(new_comment)
    pg_conn.commit()
    return new_comment.id

async def get_blog_comments(pg_conn, payload: dict) -> list:
     blog_id = payload.get("blog_id")
     limit = payload.get("limit", 5)
     page = payload.get("page", 1)
     offset = get_offset(limit=limit, page_number=page)
     data= pg_conn.query(Comments).filter(Comments.blog_id == blog_id)
     total_count = data.count()
    #  total_page = calculate_total_pages(total_count, limit)
     data = data.order_by(desc("id")).offset(offset).limit(limit)
     comments = [ comment for comment in data ]

     return {"comments": comments, "count":total_count, "total_page": ""}