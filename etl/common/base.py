from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
import re
import csv
# Create the database connection
import configparser

# Read the config file
config = configparser.ConfigParser()
config.read('common/database.ini')

# Get the database host
DB_HOST = config['mysql_local']['host']

# Get the database port
DB_PORT = config['mysql_local']['port']

# Get the database name
DATABASE = config['mysql_local']['database']

# Get the database user
DB_USER = config['mysql_local']['user']

# Get the database password
DB_PASSWORD = config['mysql_local']['password']

connect_string = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}?charset=utf8'
engine = create_engine(connect_string)
session = Session(engine)
Base = declarative_base()