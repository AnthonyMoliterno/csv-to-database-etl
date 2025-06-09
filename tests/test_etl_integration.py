import pytest
import pandas as pd
from app.file_validation import check_file
from app.file_to_dataframe import file_to_df
from app.data_transformation import transform
from app.loader import load_to_sql

def test_full_etl(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text(
        "order_id,order_date,ship_date,units_sold,unit_price,unit_cost,country,item_type\n"
        "1,2023-01-01,2023-01-02,10,5.0,3.0,USA,Beverages"
    )
    path = str(file)

    path_checked = check_file(path)
    df_loaded = file_to_df(path_checked)
    df_transformed = transform(df_loaded)
    
    with pytest.raises(RuntimeError):
        load_to_sql(df_transformed, "invalid_connection_string", "orders")
