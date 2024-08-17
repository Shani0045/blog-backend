
from apps.blogs.models.Categories import Categories
from apps.blogs.models.Blogs import Blogs
from core.utils import utils


async def get_all_category(pg_conn) -> list:
     data= pg_conn.query(Categories).all()
     return data


async def post_new_category(pg_conn, name: str) -> bool:
    new_blog = Categories(name=name)
    pg_conn.add(new_blog)
    pg_conn.commit()
    return True

async def get_all_blogs(pg_conn):
     data = pg_conn.query(
                            Blogs.id,
                            Blogs.title, 
                            Blogs.slug, 
                            Blogs.meta_desc, 
                            Blogs.created_at,
                            Categories.name
                            ).join(Blogs, Categories.id==Blogs.category_id)

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

     return all_blogs


async def get_blog_details(pg_conn, slug: str) -> dict:
    data= pg_conn.query(Blogs).filter(Blogs.slug == slug).all()
    return data


async def post_new_blog(pg_conn, payload: dict) -> bool:
    slug = utils.generate_slug(payload.title)
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
