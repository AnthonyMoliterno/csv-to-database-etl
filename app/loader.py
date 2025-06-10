import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

def load_to_sql(df: pd.DataFrame, connection_string: str, table_name: str) -> None:
    try:
        engine = sqlalchemy.create_engine(connection_string)
        with engine.begin() as connection:
            df.to_sql(table_name, con=connection, if_exists='replace', index=False)
    except SQLAlchemyError as e:
        raise RuntimeError(f"Failed to load data to SQL: {e}")
