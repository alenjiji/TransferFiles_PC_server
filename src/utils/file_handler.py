import os

def read_file(file_path):
    """Read the contents of a file."""
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    """Write data to a file."""
    with open(file_path, 'wb') as file:
        file.write(data)

def file_exists(file_path):
    """Check if a file exists."""
    return os.path.isfile(file_path)

def delete_file(file_path):
    """Delete a file."""
    if file_exists(file_path):
        os.remove(file_path)