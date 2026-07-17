from pyiceberg.catalog import NoSuchTableError

from src.iceberg.catalog import catalog
from src.iceberg.namespace import ensure_namespace

from src.silver.iceberg_schema import build_silver_schema


TABLE_NAME = "silver.silver_jobs"


def get_or_create_table():

    try:

        table = catalog.load_table(TABLE_NAME)

        print("Existing Silver table loaded.")

        return table

    except NoSuchTableError:

        print("Creating Silver table...")

        ensure_namespace(
            catalog=catalog,
            namespace="silver",
        )

        table = catalog.create_table(
            identifier=TABLE_NAME,
            schema=build_silver_schema(),
        )

        print("Silver table created.")

        return table