
from app.models.Categories import Categories
from app.models.Blogs import Blogs
from core.utils import utils


async def get_all_category(pg_conn) -> list:
     data= pg_conn.query(Categories).all()
     return data


async def post_new_category(pg_conn, name) -> bool:
    new_blog = Categories(name=name)
    pg_conn.add(new_blog)
    pg_conn.commit()
    return True


async def get_all_blogs(pg_conn) -> list:
     data = pg_conn.query(Blogs).all()
     return data


async def get_blog_details(pg_conn, slug) -> dict:
    data= pg_conn.query(Blogs).filter(Blogs.slug == slug).all()
    return data


async def post_new_blog(pg_conn, payload) -> bool:
    slug = utils.generate_slug(payload.title)
    new_blog = Blogs(title=payload.title, 
                     content=payload.content, 
                     author_id= payload.author_id, 
                     category_id=payload.category_id,
                     slug=slug
                     )
    
    pg_conn.add(new_blog)
    pg_conn.commit()
    return True
