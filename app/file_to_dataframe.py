import pandas as pd
import os

def file_to_df(path):
    _, ext = os.path.splitext(path.lower())

    if ext == ".csv":
        return pd.read_csv(path)
    elif ext == ".xlsx" or ext == ".xls":
        return pd.read_excel(path)
    else:
        raise ValueError("File extension not supported")
    
