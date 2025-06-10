import pytest
import pandas as pd
from sqlalchemy import create_engine
from app.loader import load_to_sql

def test_load_to_sql_invalid_connection():
    df = pd.DataFrame({"col": [1]})
    with pytest.raises(RuntimeError):
        load_to_sql(df, "invalid_connection_string", "test_table")

def test_load_to_sql_valid(tmp_path):
    db_path = tmp_path / "test.db"
    connection_string = f"sqlite:///{db_path}"
    
    df = pd.DataFrame({
        "id": [1, 2],
        "name": ["Alice", "Bob"]
    })

    try:
        load_to_sql(df, connection_string, "users")
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

    engine = create_engine(connection_string)
    with engine.connect() as conn:
        result_df = pd.read_sql("SELECT * FROM users", conn)

    assert result_df.shape == df.shape
    assert list(result_df.columns) == list(df.columns)
