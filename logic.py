from etl.common.db import Connector
from models.author import Author
from models.book import Book
import logging
import pymysql

# Create a logger instance
logger = logging.getLogger(__name__)

# Configure the logger
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
file_handler = logging.FileHandler("log_logic.txt")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# #Create the connection to the database

conn = Connector()
conn.get_connection()
# This function tell the number of rows in the table,
#  this is much needed in the different endpoints of this API


def rows_count(table: str) -> int:
    conn.execute(f"select count(*) from {table};")
    return conn.fetchone()[0]


def read_books():
    conn.execute("select * from book limit 10;")  # Modificar esta query
    res = conn.fetchall()
    return res


def book_by_genre(genre: str):
    genre = genre.lower()
    conn.execute("select * from book where genre = '%s' limit 5;" % (genre))
    res = conn.fetchall()
    if len(res) == 0:
        return {"message": f"No books were found for '{genre}'"}
    return res


def read_authors():
    conn.execute("select * from author limit 10;")  # Modificar esta query
    res = conn.fetchall()
    return res


def author_by_name(name: str):
    conn.execute("select * from author where name = '%s';" % name)
    res = conn.fetchall()
    return res


def book_by_lastname(last_name: str):
    conn.execute(
        "select id_author from author where last_name = '%s';" % (last_name))
    author_id = conn.fetchone()
    conn.execute(f"select * from book where id_author = {author_id[0]} ;")
    rs = conn.fetchall()
    return rs


def add_author(author: Author):
    id = rows_count("author") + 1
    try:
        conn.execute(
            "insert into author values (%s, %s, %s)" %
            (author.name, author.last_name, id)
        )
        conn.conn.commit()
        conn.close()
        logger.info("Author created successfully")
        return {"message": "Author created successfully"}
    except pymysql.err.IntegrityError as e:
        conn.rollback()
        logger.error(f"Error adding author: {str(e)}")
        return {"message": "Error adding author"}


def add_book(book: Book):
    try:
        conn.execute("""insert into book(title,genre,height,publisher,id_author) values('%sbook.title}',
                                                                            '%sbook.genre.capitalize()}',
                                                                            %sbook.height},
                                                                            '%sbook.publisher}',
                                                                            %sbook.author_id})""" % (book.title, 
                                                                                                     book.genre,
                                                                                                     book.publisher,
                                                                                                     book.id))
        conn.conn.commit()
        conn.close()
        logger.info("Book created successfully")
        return {"message": "Book created successfully"}
    except:
        conn.rollback()


def delete_book(title: str):
    try:
        # Esto podria hacerse tal vez mas
        conn.execute("delete from book where title = '%s';" % (title))
        # eficiente si usaramos el id como parametro para filtrar.
        conn.conn.commit()
        conn.close()
        logger.info("Book deleted successfully")
        return {"message": "Book deleted successfully"}
    except:
        conn.rollback()


def delete_author_by_lastname(last_name: str):
    try:
        # Esto podria hacerse tal vez mas
        conn.execute("delete from author where last_name = '%s';" % (last_name))
        # eficiente si usaramos el id como parametro para filtrar.
        conn.conn.commit()
        conn.close()
        logger.info("Author deleted by lastname successfully")
        return {"message": "Author deleted successfully"}
    except:
        conn.rollback()


def delete_author_by_id(id: int):
    try:
        # Esto podria hacerse tal vez mas
        # eficiente si usaramos el id como parametro para filtrar.
        conn.execute("delete from author where id = %s;"% (id,))
        conn.conn.commit()
        conn.close()
        logger.info("Author deleted by id successfully")
        return {"message": "Author deleted successfully"}
    except:
        conn.rollback()
