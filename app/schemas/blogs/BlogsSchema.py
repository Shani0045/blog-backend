from pydantic import BaseModel

class BlogsSchema(BaseModel):
    title: str
    content: str
    category_id: int
    author_id: int
    created_at: int
    updated_at: int

