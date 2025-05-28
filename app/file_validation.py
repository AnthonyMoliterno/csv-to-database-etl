import os

def check_file(path):
    ALLOWED_EXTENSIONS = {'.xlsx', '.xls', '.csv'}

    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")
    _, ext = os.path.splitext(path.lower())
    
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"File extension not supported: {ext}")\
        
    return path