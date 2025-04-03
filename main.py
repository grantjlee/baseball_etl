from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data_to_postgres

def main():
    print("Starting ETL pipeline...")
    df = extract_data(2024)  # Extract data
    df_transformed = transform_data(df) # Transform data, i.e. only grab relevant data
    load_data_to_postgres(df_transformed) # Load data into local Postgres db
    print(df_transformed.head())
    print("Finished process.")

if __name__ == "__main__":
    main()
