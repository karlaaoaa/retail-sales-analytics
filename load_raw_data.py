
import pandas as pd
from pathlib import Path
from getpass import getpass

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# 1. Locate and read the original Excel file
file_path = Path("Online Retail.xlsx")

if not file_path.exists():
    raise FileNotFoundError(
        f"Could not find the file: {file_path.resolve()}"
    )

df = pd.read_excel(file_path)

print("Source rows:", len(df))
print("Source columns:", len(df.columns))

# 2. Configure the PostgreSQL connection
password = getpass("Enter your PostgreSQL password: ")

connection_url = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password=password,
    host="localhost",
    port=5432,
    database="retail_sales",
)

engine = create_engine(connection_url)

try:
    # 3. Load the data into PostgreSQL in batches
    df.to_sql(
        name="raw_online_retail",
        con=engine,
        schema="public",
        if_exists="fail",
        index=False,
        chunksize=5_000,
        method=None,
    )

    print("Raw data loaded successfully.")

    # 4. Validate the imported row count
    with engine.connect() as connection:
        imported_rows = connection.exec_driver_sql(
            "SELECT COUNT(*) FROM public.raw_online_retail"
        ).scalar_one()

    print("Source rows:", len(df))
    print("Imported rows:", imported_rows)

    if imported_rows != len(df):
        raise ValueError("Row count mismatch!")

    print("Row count validation passed.")

finally:
    engine.dispose()
