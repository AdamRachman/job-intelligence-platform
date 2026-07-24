from src.iceberg.catalog import catalog
from src.iceberg.namespace import ensure_namespace

from src.gold.iceberg_schema import build_gold_schema


NAMESPACE = "gold"
TABLE_NAME = "gold_jobs"


def get_or_create_table():

    ensure_namespace(
        catalog,
        NAMESPACE,
    )

    identifier = f"{NAMESPACE}.{TABLE_NAME}"

    try:

        table = catalog.load_table(identifier)

        print("Existing Gold table loaded.")

        return table

    except Exception:

        print("Creating Gold table...")

        table = catalog.create_table(
            identifier=identifier,
            schema=build_gold_schema(),
        )

        print("Gold table created.")

        return table