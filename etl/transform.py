import csv

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
def replace_null(row:list[str])->list[str]:
    row[-1] = row[-1] if row[-1].upper() != "NULL" else 30
    return row
print(replace_null(read_csv("./raw/books_data/users.csv")[0]))
#def main():
