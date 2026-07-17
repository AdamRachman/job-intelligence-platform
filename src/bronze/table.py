from pyiceberg.catalog import NoSuchTableError

from src.iceberg.catalog import catalog
from src.iceberg.namespace import ensure_namespace

from src.bronze.iceberg_schema import build_bronze_schema


TABLE_NAME = "bronze.bronze_jobs"


def get_or_create_table():

    try:

        table = catalog.load_table(TABLE_NAME)

        print("Existing Bronze table loaded.")

        return table

    except NoSuchTableError:

        print("Creating Bronze table...")

        # Equivalent to:
        # CREATE SCHEMA IF NOT EXISTS bronze;
        ensure_namespace(
            catalog=catalog,
            namespace="bronze",
        )

        table = catalog.create_table(
            identifier=TABLE_NAME,
            schema=build_bronze_schema(),
        )

        print("Bronze table created.")

        return table