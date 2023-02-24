from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

# Old connector support


class Connector(object):
    # Create a constructor
    def __init__(self, database: str, host: str, user: str, password: str, port: int):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port
    # Create a method to connect to the database

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                port = self.port
            )
            self.cursor = self.conn.cursor()

            if (self.cursor):
                print("Connected successfully!")
        except mysql.connector.Error as error:
            print("Error:", error)

    # Execute a query in the database

    def execute(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as e:
            print("Error: ", e)
        finally:
            self.conn.close()
    # Fetch the result but only return the first result

    def fetchone(self):
        return self.cursor.fetchone()
    # Fetch the result and return all the set.

    def fetchall(self):
        return self.cursor.fetchall()
    # Close the db connection.

    def close(self):
        self.cursor.close()
        if (False == self.cursor):
            print("Closed successfully!")
# Instance the class
# db = Connector("bookstore","localhost","root","micolash12",3306)
# db.connect()
# db.execute("select * from book limit 1")
# print(db.fetchall())
