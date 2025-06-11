from app.logger import get_logger
import pandas as pd

logger = get_logger(__name__)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting data transformation...")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    required = ['order_id', 'order_date', 'ship_date', 'units_sold', 'unit_price', 'unit_cost', 'country', 'item_type']
    missing = [col for col in required if col not in df.columns]
    if missing:
        logger.error(f"Missing required column(s): {', '.join(missing)}")
        raise ValueError(f"Missing required column(s): {', '.join(missing)}")

    df = df.drop_duplicates()
    df = df.dropna(subset=required)

    df = df[
        (df['units_sold'] > 0) & 
        (df['unit_price'] >= 0) & 
        (df['unit_cost'] >= 0)
    ]

    df['order_id'] = df['order_id'].astype(str)
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')
    df['units_sold'] = df['units_sold'].astype(int)
    df['unit_price'] = df['unit_price'].astype(float)
    df['unit_cost'] = df['unit_cost'].astype(float)

    df['total_revenue'] = df['units_sold'] * df['unit_price']
    df['total_cost'] = df['units_sold'] * df['unit_cost']
    df['total_profit'] = df['total_revenue'] - df['total_cost']

    logger.info(f"Transformation complete. Final shape: {df.shape}")
    return df
