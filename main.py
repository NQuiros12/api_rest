#uvicorn main:app --reload
from fastapi import FastAPI
from config.db import Connector
from pydantic import BaseModel

class Book(BaseModel):
    id : int
    title: str
    author_id: int
    genre : str
    class Config:
        orm_mode = True
class Author(BaseModel):
    id : int
    name : str | None = None
#Instaciate the app
app = FastAPI()
# #Create the connection to the database
conn = Connector("bookstore","localhost","root","micolash12",3306)
conn .connect()
@app.get('/books')
async def books():
   conn.execute("select * from book limit 10;") ##### Modificar esta query
   res = conn.fetchall()
   return res 
@app.get('/author/{author_id}')
async def book_by_author( author_id : str ):
    conn.execute(f"select * from book where id_author = {author_id} ;") ##### Modificar esta query
    rs = conn.fetchall()
    return rs
@app.get("/test")
def test_hi():
   response = ('the API works!', 200)
   return response