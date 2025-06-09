import pytest
import pandas as pd
from app.data_transformation import transform

def test_missing_required_columns():
    df = pd.DataFrame({"wrong_col": [1]})
    with pytest.raises(ValueError):
        transform(df)

def test_successful_transformation():
    data = {
        "order_id": ["1"],
        "order_date": ["2023-01-01"],
        "ship_date": ["2023-01-02"],
        "units_sold": [10],
        "unit_price": [5.0],
        "unit_cost": [3.0],
        "country": ["USA"],
        "item_type": ["Beverages"]
    }
    df = pd.DataFrame(data)
    result = transform(df)
    assert "total_revenue" in result.columns
    assert result.loc[0, "total_revenue"] == 50.0

def test_transform_with_negative_values():
    data = {
        "order_id": ["1"],
        "order_date": ["2023-01-01"],
        "ship_date": ["2023-01-02"],
        "units_sold": [-5],
        "unit_price": [5.0],
        "unit_cost": [3.0],
        "country": ["USA"],
        "item_type": ["Beverages"]
    }
    df = pd.DataFrame(data)
    result = transform(df)
    assert result.empty  # Should filter out negative units_sold

def test_transform_with_bad_dates():
    data = {
        "order_id": ["1"],
        "order_date": ["bad_date"],
        "ship_date": ["also_bad"],
        "units_sold": [5],
        "unit_price": [5.0],
        "unit_cost": [3.0],
        "country": ["USA"],
        "item_type": ["Beverages"]
    }
    df = pd.DataFrame(data)
    result = transform(df)
    assert pd.isnull(result["order_date"].iloc[0])
    assert pd.isnull(result["ship_date"].iloc[0])

def test_transform_with_nulls_in_required_columns():
    data = {
        "order_id": [None],
        "order_date": ["2023-01-01"],
        "ship_date": ["2023-01-02"],
        "units_sold": [10],
        "unit_price": [5.0],
        "unit_cost": [3.0],
        "country": ["USA"],
        "item_type": ["Beverages"]
    }
    df = pd.DataFrame(data)
    result = transform(df)
    assert result.empty

def test_transform_with_empty_dataframe():
    df = pd.DataFrame(columns=[
        "order_id", "order_date", "ship_date", "units_sold", 
        "unit_price", "unit_cost", "country", "item_type"
    ])
    result = transform(df)
    assert result.empty
