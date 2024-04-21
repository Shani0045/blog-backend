from pydantic import BaseModel

class BlogsRequestSchema(BaseModel):
    title: str
    content: str
    category_id: int
    author_id: int


class BlogsResponseSchema(BaseModel):
    status: str
    message: str
    data: list|dict
    
