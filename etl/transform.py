import csv
from common.base import session, Base
from common.tables import User
from sqlalchemy import text
#TODO: 
# * Create a function to calculate the mean
def read_csv(filename:str):
	# Open the CSV file using a context manager.
	with open(filename, mode='r', newline='',encoding='latin-1') as csv_file:
	# Create a CSV reader object.
		csv_reader = csv.reader(csv_file,delimiter=";")
		_ = next(csv_reader)  # Skips the headers if any
		rows = list(csv_reader) 
	return rows
def split_location(row:list[str])->list[str]:
	row[1] = row[1].strip().split(",")
	return [item for sublist in row for item in (sublist if isinstance(sublist, list) else [sublist])]
def replace_null(cell:str)->str:
	cell = cell if cell.upper() != "NULL" else 30
	return cell
def format_pk(rows:list[str])->list[str]:
	for i in range(len(rows)):
		rows[i][0] = i
	return rows

def truncate_table(table:str)->None:
    """
    Ensure that the table is always in empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text(f"TRUNCATE TABLE {table};")
    )
    session.commit()
def transform_new_data(rows:list[str]) -> None:
	"""
	Apply all transformations for each row in the .csv file before saving it into database
	"""
	users_objects = []
	for row in rows:
			# Apply transformations and save as Users object
			users_objects.append(
				User(
					user_id = int(row[0]),
					location = row[1],
					age = int(row[2]) if row[2] != "NULL" else 30
				)
			)
		# Bulk save all new processed objects and commit
	session.bulk_save_objects(users_objects)
	session.commit()


def main():
	rows = format_pk(read_csv("./raw/books_data/users.csv"))
	#truncate_table("users")
	transform_new_data(rows)