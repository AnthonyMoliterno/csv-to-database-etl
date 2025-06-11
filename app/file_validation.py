from app.logger import get_logger
import os

logger = get_logger(__name__)
ALLOWED_EXTENSIONS = {'.xlsx', '.xls', '.csv'}

def check_file(path: str) -> str:
    if not os.path.isfile(path):
        logger.error(f"File not found: {path}")
        raise FileNotFoundError(f"File not found: {path}")
    
    _, ext = os.path.splitext(path.lower())
    if ext not in ALLOWED_EXTENSIONS:
        logger.error(f"File extension not supported: {ext}")
        raise ValueError(f"File extension not supported: {ext}")
    
    logger.info(f"File validated: {path}")
    return path
