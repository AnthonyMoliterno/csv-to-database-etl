import pandas as pd

def transform(df):
    expected_columns = ['order_id', 'order_date', 'units_sold', 'unit_price', 'unit_cost', 'country']
    missing_cols = [col for col in expected_columns if col not in df.columns]

    if missing_cols:
        raise ValueError(f"Missing required column(s): {', '.join(missing_cols)}")
        return
    
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    df = df.drop_duplicates(keep="first")
    df = df.drop_duplicates(subset="order_id")

    df = df[
        (df['Units Sold'] > 0) &
        (df['Unit Price'] >= 0) &
        (df['Unit Cost'] >= 0)
    ]

    df['Order Id'] = df['Order Id'].astype(str)
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
    df['Units Sold'] = df['Units Sold'].astype(int)
    df['Unit Price'] = df['Unit Price'].astype(float)
    df['Unit Cost'] = df['Unit Cost'].astype(float)




