import zipfile

extracted_dir = 'raw/'
zip_file_path = 'source/archive.zip'

def extract_data_zip(zip_file_path:str,extracted_dir:str) -> None:

    # Open the ZIP file using a context manager.
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all files from the ZIP archive to the specified directory.
        zip_ref.extractall(extracted_dir)

    print(f"Successfully extracted contents to {extracted_dir}")

def main():
    extract_data_zip(zip_file_path,extracted_dir)