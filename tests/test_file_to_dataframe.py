import pytest
import pandas as pd
from app.file_to_dataframe import file_to_df
import tempfile

def test_read_csv(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text("col1,col2\n1,2\n3,4")
    df = file_to_df(str(file))
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["col1", "col2"]

def test_unsupported_extension(tmp_path):
    file = tmp_path / "data.unsupported"
    file.write_text("data")
    with pytest.raises(ValueError):
        file_to_df(str(file))
