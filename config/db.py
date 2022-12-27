from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
#URL for the database connection
SQLALCHEMY_DATABASE_URL = "mysql://root:micolash12@localhost:3306/bookstore"
#Create the engine, with this we can connect
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
#
#Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
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
    self.cursor.execute(query)
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
