from app.logger import get_logger
import pandas as pd
import os

logger = get_logger(__name__)

def file_to_df(path: str) -> pd.DataFrame:
    _, ext = os.path.splitext(path.lower())
    logger.info(f"Reading file: {path}")
    
    try:
        if ext == ".csv":
            df = pd.read_csv(path, delimiter=",")
        elif ext == ".xlsx":
            df = pd.read_excel(path, engine="openpyxl")
        elif ext == ".xls":
            df = pd.read_excel(path, engine="xlrd")
        else:
            logger.error(f"Unsupported file extension: {ext}")
            raise ValueError("File extension not supported")
    except Exception as e:
        logger.error(f"Failed to read file: {e}")
        raise

    logger.info(f"Loaded DataFrame with shape: {df.shape}")
    return df
