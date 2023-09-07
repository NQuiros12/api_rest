from sqlalchemy import create_engine
import re
import csv
# Create the database connection
import configparser

# Read the config file
config = configparser.ConfigParser()
config.read('database.ini')

# Get the database host
DB_HOST = config['database']['host']

# Get the database port
DB_PORT = config['database']['port']

# Get the database name
DATABASE = config['database']['database']

# Get the database user
DB_USER = config['database']['user']

# Get the database password
DB_PASSWORD = config['database']['password']

file = "etl/data/books.csv"

connect_string = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}?charset=utf8'
engine = create_engine(connect_string)