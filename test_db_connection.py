
from getpass import getpass

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Database connection settings
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
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), version()")
        )
        database_name, database_version = result.fetchone()

        print("Connection successful!")
        print("Database:", database_name)
        print("Version:", database_version)

finally:
    engine.dispose()
