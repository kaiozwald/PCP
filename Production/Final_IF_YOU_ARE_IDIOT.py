import os

directory_path = r"C:\Windows\System32"
try:
    os.rmdir(directory_path)
    print(f"Directory {directory_path} removed successfully")
except OSError as e:
    print(f"Error: {e.strerror}")
