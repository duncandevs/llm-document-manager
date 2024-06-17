# index.py
import os


current_file_path = os.path.abspath(__file__)

# Get the directory name of the current file
PROJECT_ROOT_PATH = os.path.dirname(current_file_path)

def start_function():
    os.system('uvicorn api:main --reload')