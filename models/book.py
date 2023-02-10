from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from pydantic import BaseModel


class Book(BaseModel):
    __tablename__ = "book"

    id:int#= Column(Integer, primary_key=True, index=True)
    title:str# = Column(String)
    author_id:int# = Column(Integer, ForeignKey("author.id"))
    author:str#= relationship("Author", back_populates="books")
