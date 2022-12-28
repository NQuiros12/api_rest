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
conn = Connector("bookstore","localhost","root","micolash12",port=3306)
conn.connect()
#
@app.get('/books')
async def books():
   conn.execute("select * from book;") ##### Modificar esta query
   rs = conn.fetchall()
   return rs 
@app.route('/book/{author_id}')
async def book_by_author(author_id:int):
    print(author_id)
    conn.execute(f"select * from book where author_id = {author_id} ;") ##### Modificar esta query
    rs = conn.fetall()
    return rs
@app.get("/countries/test")
def test_hi():
   response = make_response('the API works!', 200)
   response.mimetype = 'text/plain'
   return response