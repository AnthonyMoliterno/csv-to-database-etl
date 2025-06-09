import pandas as pd
import os

def file_to_df(path: str) -> pd.DataFrame:
    _, ext = os.path.splitext(path.lower())
    if ext == ".csv":
        return pd.read_csv(path)
    elif ext in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError("File extension not supported")
