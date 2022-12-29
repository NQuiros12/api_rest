from sqlalchemy import create_engine
import pandas as pd
import seaborn as sns
import numpy as np

file = "../data/books.csv"
rd = pd.read_csv(file)

# Just to keep the columns names consistent with SQL good practices.
rd.columns = list(map(lambda x: x.lower(), rd.columns))
author_name = pd.Series(rd["author"].unique())
author_df = pd.DataFrame(author_name, columns=['author'])
author_df["id_author"] = author_df.index
# Create the database connection
engine = create_engine('mysql+pymysql://root:micolash12@localhost/bookstore')
# Use the built-in function 'to_sql' to write the dataframe to the database
author_df.to_sql('author', engine, if_exists='replace', index=False)


# Copy the df to a book related to preserve the original
book_df = rd.copy()
# Add the id_author foreign key to the book
# replace all the occurences of the author for the value in the author dataframe
book_df['id_author'] = book_df['author'].map(
    author_df.set_index('author')['id_author'])
# Now drop the author dataframe for avoiding to much information
book_df = book_df.drop(columns=["author"])
# Create the database connection
engine = create_engine('mysql+pymysql://root:micolash12@localhost/bookstore')
# Use the built-in function 'to_sql' to write the dataframe to the database
book_df.to_sql('book', engine, if_exists='replace', index=True)
