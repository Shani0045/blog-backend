from pydantic import BaseModel

class BlogsRequestSchema(BaseModel):
    title: str
    content: str
    meta_desc: str
    category_id: int
    author_id: int


class BlogsResponseSchema(BaseModel):
    title:str|None
    
    
