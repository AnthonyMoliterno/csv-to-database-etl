from app.logger import get_logger
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

logger = get_logger(__name__)

def load_to_sql(df: pd.DataFrame, connection_string: str, table_name: str) -> None:
    try:
        logger.info("Connecting to database...")
        engine = sqlalchemy.create_engine(connection_string)
        with engine.begin() as connection:
            df.to_sql(table_name, con=connection, if_exists='replace', index=False)
        logger.info(f"Data loaded to SQL table: {table_name}")
    except SQLAlchemyError as e:
        logger.error(f"Failed to load data to SQL: {e}")
        raise RuntimeError(f"Failed to load data to SQL: {e}")
