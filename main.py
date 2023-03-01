# uvicorn main:app --reload
from fastapi import FastAPI
from config.db import Connector
from fastapi.responses import HTMLResponse
from logic import rows_count, read_books, book_by_genre, read_authors, author_by_name, book_by_lastname, add_author, add_book, delete_author_by_id, delete_book,delete_author_by_lastname
from models.author import Author
from models.book import Book
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# configure CORS middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=["*"]  # or specific headers that your client may send
)

@app.get('/books')
async def books():
    return read_books()


@app.get('/books_genre/{genre}')
async def books_genre(genre: str):
    return book_by_genre(genre)


@app.get('/authors')
async def authors():
    return read_authors()


@app.get('/author/{name}')
async def author(name: str):
    return author_by_name(name)


@app.get('/author_books/{last_name}')
async def books_by_author_lastname(last_name: str):
    return book_by_lastname(last_name)


@app.post("/author/")
async def add_author(author: Author):
    return add_author(author)


@app.post('/book/')
async def add_book(book: Book):
    return add_book(book)


@app.delete("/book/{title}")
async def delete_book(title: str):
    return delete_book(title)

@app.delete("/author/{title}")
async def delete_author(last_name: str):
    return delete_author_by_lastname(last_name)


@app.get("/", response_class=HTMLResponse)
def test_hi():
    return FileResponse("template/index.html")
