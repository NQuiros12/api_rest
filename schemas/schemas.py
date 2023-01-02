""" from pydantic import BaseModel

class Book(BaseModel):
    id : int
    title: str
    author_id: int
    class Config:
        orm_mode = True
class Author(BaseModel):
    id : int
    name : str | None = None
      """