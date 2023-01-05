from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

#Old connector support
class Connector(object):
  #Create a constructor
  def __init__(self,database:str,host:str,user:str,password:str,port:int):
    self.database = database
    self.host = host
    self.user = user
    self.password = password
    self.port = port
  #Create a method to connect to the database
  def connect(self):
    self.conn = mysql.connector.connect(
      host = self.host,
      user = self.user,
      password = self.password,
      database = self.database,
      port = self.port
    )
    self.cursor = self.conn.cursor()
    if(self.cursor):
      print("Connected successfully!")
      
  #Execute a query in the database
  def execute(self, query):
    try:
      self.cursor.execute(query)
    except mysql.connector.Error as e:
      print("Error reading data from MySQL table", e)
  #Fetch the result but only return the first result
  def fetchone(self):
    return self.cursor.fetchone()
  #Fetch the result and return all the set.
  def fetchall(self):
    return self.cursor.fetchall()
  #Close the db connection.
  def close(self):
    self.cursor.close()
    if(False == self.cursor):
      print("Closed successfully!")
  def create_post(self,title: str, content: str) -> None:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='mydatabase',
                                            user='user',
                                            password='password')
        cursor = connection.cursor()
        insert_query = "INSERT INTO posts (title, content) VALUES (%s, %s)"
        cursor.execute(insert_query, (title, content))
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into posts table")
    except Error as error:
        print("Error:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
#Instance the class
# db = Connector("bookstore","localhost","root","micolash12",3306)
# db.connect()
# db.execute("select * from book limit 1")
# print(db.fetchall())
