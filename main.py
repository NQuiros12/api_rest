#uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.db import Connector
from pydantic import BaseModel
from starlette.responses import FileResponse 
class Book(BaseModel):
    id : int | None = None
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
#This function tell the number of rows in the table, this is much needed in the different endpoints of this API
def rows_count(table : str) -> int:
    conn.execute(f"select count(*) from {table};")
    return conn.fetchone()[0]
#This gets the first 10 books.
@app.get('/books')
async def books():
   conn.execute("select * from book limit 10;") ##### Modificar esta query
   res = conn.fetchall()
   return res 
@app.get('/books_genre/{genre}')
async def books_genre(genre : str):
    genre = genre.lower()
    conn.execute(f"select * from book where genre = '{genre}' limit 5;") 
    res = conn.fetchall()
    if len(res) == 0:
        return {"message": f"No books were found for '{genre}'"}
    return res 

@app.get('/authors')
async def authors():
   conn.execute("select * from author limit 10;") ##### Modificar esta query
   res = conn.fetchall()
   return res
@app.get('/author/{name}')
async def author(name:str):
   conn.execute(f"select * from author where name = '{name}';") ##### Modificar esta query
   res = conn.fetchall()
   return res 
@app.get('/author_books/{last_name}')
async def books_by_author_lastname( last_name : str ):
    conn.execute(f"select id_author from author where last_name = '{last_name}';")
    author_id = conn.fetchone()
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
    conn.execute(f"""insert into book(title,genre,height,publisher,id_author) values('{book.title}',
                                                                        '{book.genre.capitalize()}',
                                                                        {book.height},
                                                                        '{book.publisher}',
                                                                        {book.author_id})""")
    conn.conn.commit()
    conn.close()
    return {"message": "Book created successfully"}
@app.delete("/book/{title}")
async def delete_book(title:str):
    conn.execute(f"delete from book where title = {title};")
    conn.conn.commit()
    conn.close()
    return {"message": "Book deleted successfully"}
@app.get("/",response_class=HTMLResponse)
def test_hi():
   return FileResponse("template/index.html")