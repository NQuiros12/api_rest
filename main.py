#uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.db import Connector
from pydantic import BaseModel

class Book(BaseModel):
    id : int
    title: str
    author_id: int
    genre : str
    height: int
    publisher: str
    class Config:
        orm_mode = True
class Author(BaseModel):
    id : int | None = None
    name : str | None = None
    last_name: str 
#Instaciate the app
app = FastAPI()
# #Create the connection to the database
conn = Connector("bookstore","localhost","root","micolash12",3306)
conn.connect()
def rows_count(table : str) -> int:
    conn.execute(f"select count(*) from {table};")
    return conn.fetchone()[0]
@app.get('/books')
async def books():
   conn.execute("select * from book limit 10;") ##### Modificar esta query
   res = conn.fetchall()
   return res 
@app.get('/authors')
async def authors():
   conn.execute("select * from author limit 10;") ##### Modificar esta query
   res = conn.fetchall()
   return res 
@app.get('/author/{lastname}')
async def book_by_author_lastname( lastname : str ):
    conn.execute(f"select id_author from author where last_name = '{lastname}';")
    author_id = conn.fetchone()
    #print(author_id)
    conn.execute(f"select * from book where id_author = {author_id[0]} ;") ##### Modificar esta query
    rs = conn.fetchall()
    return rs
@app.post("/author/")
async def add_author(author:Author):
    id = rows_count("author") + 1
    conn.execute(f"insert into author values('{author.name}','{author.last_name}',{id})")
    conn.conn.commit()
    conn.close()
    return {"message": "Author created successfully"}
@app.post('/book/')
async def add_book(book : Book):
    conn.execute(f"""insert into book(index,title,genre,height,publisher,id_author) values(%s,%s,%s,%s)""")
    conn.conn.commit()
    conn.close()
    return {"message": "Book created successfully"}

@app.get("/",response_class=HTMLResponse)
def test_hi():
   response = '<html><h1>the API works!</h1></html>'
   return response