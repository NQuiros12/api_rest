import mysql.connector

class Connector(object):
  #Create a constructor
  def __init__(self,database:str,host:str,user:str,password:str):
    self.database = database
    self.host = host
    self.user = user
    self.password = password
  #Create a method to connect to the database
  def connect(self):
    self.conn = mysql.connector.connect(
      host = self.host,
      user = self.user,
      password = self.password,
      database = self.database
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
  
""" con = Connector("paises","localhost","root","micolash12")
con.connect()
con.execute("select * from pais limit 4")
print(con.fetchall())
print(con.close()) """