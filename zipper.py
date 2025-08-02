import zipfile
import os

def compress_files(file_paths, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in file_paths:
            arcname = os.path.basename(file)
            zipf.write(file, arcname)

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
