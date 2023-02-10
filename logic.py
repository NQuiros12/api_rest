from config.db import Connector
from models.author import Author
from models.book import Book
# #Create the connection to the database
conn = Connector("bookstore", "localhost", "root", "micolash12", 3306)
conn.connect()
# This function tell the number of rows in the table, this is much needed in the different endpoints of this API


def rows_count(table: str) -> int:
    conn.execute(f"select count(*) from {table};")
    return conn.fetchone()[0]


def read_books():
    conn.execute("select * from book limit 10;")  # Modificar esta query
    res = conn.fetchall()
    return res


def book_by_genre(genre: str):
    genre = genre.lower()
    conn.execute(f"select * from book where genre = '{genre}' limit 5;")
    res = conn.fetchall()
    if len(res) == 0:
        return {"message": f"No books were found for '{genre}'"}
    return res


def read_authors():
    conn.execute("select * from author limit 10;")  # Modificar esta query
    res = conn.fetchall()
    return res


def author_by_name(name: str):
    conn.execute(f"select * from author where name = '{name}';")
    res = conn.fetchall()
    return res


def book_by_lastname(last_name: str):
    conn.execute(
        f"select id_author from author where last_name = '{last_name}';")
    author_id = conn.fetchone()
    conn.execute(f"select * from book where id_author = {author_id[0]} ;")
    rs = conn.fetchall()
    return rs


def add_author(author: Author):
    id = rows_count("author") + 1
    try:
        conn.execute(
            f"insert into author values('{author.name}','{author.last_name}',{id})")
        conn.conn.commit()
        conn.close()
        return {"message": "Author created successfully"}
    except:
        conn.rollback()


def add_book(book: Book):
    try:
        conn.execute(f"""insert into book(title,genre,height,publisher,id_author) values('{book.title}',
                                                                            '{book.genre.capitalize()}',
                                                                            {book.height},
                                                                            '{book.publisher}',
                                                                            {book.author_id})""")
        conn.conn.commit()
        conn.close()
        return {"message": "Book created successfully"}
    except:
        conn.rollback()


def delete_book(title: str):
    try:
        # Esto podria hacerse tal vez mas
        conn.execute(f"delete from book where title = '{title}';")
        # eficiente si usaramos el id como parametro para filtrar.
        conn.conn.commit()
        conn.close()
        return {"message": "Book deleted successfully"}
    except:
        conn.rollback()


def delete_author_by_lastname(last_name: str):
    try:
        # Esto podria hacerse tal vez mas
        conn.execute(f"delete from author where last_name = '{last_name}';")
        # eficiente si usaramos el id como parametro para filtrar.
        conn.conn.commit()
        conn.close()
        return {"message": "Author deleted successfully"}
    except:
        conn.rollback()
def delete_author_by_id(last_name: str):
    try:
        # Esto podria hacerse tal vez mas
        conn.execute(f"delete from author where id = '{id}';")
        # eficiente si usaramos el id como parametro para filtrar.
        conn.conn.commit()
        conn.close()
        return {"message": "Author deleted successfully"}
    except:
        conn.rollback()
