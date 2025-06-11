from app import check_file, file_to_df, transform, load_to_sql
from app.logger import get_logger

logger = get_logger("main")

if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    connection_string = (
        "mssql+pyodbc://@ANTTYWOAH\\SQLEXPRESS/sales_data"
        "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    table_name = "orders"

    try:
        logger.info("Starting ETL process...")
        path = check_file(path)
        df = file_to_df(path)
        df = transform(df)
        load_to_sql(df, connection_string, table_name)
        logger.info("ETL process completed successfully.")
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        logger.error(f"ETL process failed: {e}")
