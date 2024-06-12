# index.py
def start_function():
    import os
    os.system('uvicorn api:main --reload')