from app import check_file, file_to_df, transform, load_to_sql

if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    connection_string = ""
    table_name = ""

    try:
        path = check_file(path)
        df = file_to_df(path)
        df = transform(df)
        load_to_sql(df, connection_string, table_name)
        print("ETL successfully completed.")
    except(FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"Error: {e}")