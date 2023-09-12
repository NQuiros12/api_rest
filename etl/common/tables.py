from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer,String,ForeignKey
from common.base import engine

Base = declarative_base()

class Rating(Base):
    __tablename__ = "ratings"
    rating_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    ISBN = Column(String(255),ForeignKey("books.ISBN"))
    book_rating = Column(Integer)

class Book(Base):
    __tablename__ = "books"

    ISBN = Column(String(255),primary_key=True)
    book_title =  Column(String(255))
    book_author = Column(String(255))
    year_of_publication = Column(Integer)
    publisher = Column(String(255))
    image_url_s = Column(String(255))
    image_url_m = Column(String(255))
    image_url_l = Column(String(255))
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    location = Column(String(255))
    age = Column(Integer)
Base.metadata.create_all(engine)