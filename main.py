from app import check_file, file_to_df


path = input("Enter file path: ")


if __name__ == "__main__":
    try:
        path = check_file(path)
        df = file_to_df(path)
        
    except(FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")