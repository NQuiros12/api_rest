from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
class Author(BaseModel):
    __tablename__ = "author"
    id:int = Column(Integer, primary_key=True, index=True)
    name:str = Column(String)
    books:list = relationship("Book", back_populates="author")
