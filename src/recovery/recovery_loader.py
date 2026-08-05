from pathlib import Path
import pandas as pd

from pyiceberg.exceptions import NoSuchTableError

from src.iceberg.catalog import catalog
from src.bronze.iceberg_schema import build_bronze_schema
from src.iceberg.namespace import ensure_namespace
from src.iceberg.arrow import dataframe_to_arrow


# =========================
# CONFIG
# =========================

TABLE_NAME = "bronze.bronze_jobs"

RECOVERY_DIR = Path(
    "src/recovery/output"
)


BUSINESS_KEYS = [
    "source",
    "job_id"
]


# =========================
# FIND LATEST RECOVERY CSV
# =========================

def get_latest_recovery_file():

    files = sorted(
        RECOVERY_DIR.glob(
            "recovery_*.csv"
        ),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )


    if not files:

        raise Exception(
            "No recovery file found"
        )


    return files[0]



# =========================
# DROP TABLE IF EXISTS
# =========================

def drop_existing_table():


    try:

        catalog.load_table(
            TABLE_NAME
        )


        print(
            "Existing bronze table found."
        )


        catalog.drop_table(
            TABLE_NAME
        )


        print(
            "Bronze table dropped."
        )


    except NoSuchTableError:


        print(
            "Bronze table does not exist."
        )



# =========================
# CREATE BRONZE TABLE
# =========================

def create_bronze_table():


    ensure_namespace(
        catalog=catalog,
        namespace="bronze"
    )


    table = catalog.create_table(
        identifier=TABLE_NAME,
        schema=build_bronze_schema()
    )


    print(
        "Bronze table recreated."
    )


    return table



# =========================
# VALIDATE SCHEMA
# =========================

def validate_schema(df):


    required_columns = [

        "source",
        "job_id",
        "detail_url",
        "title",
        "company",
        "location",
        "posted_date",
        "employment_type",
        "salary",
        "classification",
        "sub_classification",
        "seniority_level",
        "job_function",
        "industry",
        "short_description",
        "job_description",
        "scraped_at"

    ]


    missing = (
        set(required_columns)
        -
        set(df.columns)
    )


    if missing:

        raise Exception(
            f"Missing columns: {missing}"
        )



# =========================
# SCHEMA ENFORCEMENT
# =========================

def enforce_schema(df):


    for col in df.columns:

        df[col] = (
            df[col]
            .astype("string")
        )


    return df



# =========================
# MAIN
# =========================

def main():


    print("="*60)
    print("BRONZE RECOVERY")
    print("="*60)



    # 1. Find CSV

    recovery_file = (
        get_latest_recovery_file()
    )


    print(
        "Using:",
        recovery_file
    )



    # 2. Read CSV

    df = pd.read_csv(
        recovery_file
    )


    print(
        "Total Recovery Rows:",
        len(df)
    )



    # 3. Validate

    validate_schema(
        df
    )



    # 4. Drop old bronze

    drop_existing_table()



    # 5. Create new bronze

    table = create_bronze_table()



    # 6. Schema enforcement

    df = enforce_schema(
        df
    )



    # 7. Pandas -> Arrow

    arrow_table = dataframe_to_arrow(
        df,
        build_bronze_schema()
    )



    # 8. Append Iceberg

    table.append(
        arrow_table
    )


    print(
        "Recovery append completed."
    )



    # 9. Validation

    refreshed_table = catalog.load_table(
        TABLE_NAME
    )


    recovered_count = (
        refreshed_table
        .scan()
        .to_arrow()
        .num_rows
    )


    print(
        "Bronze count:",
        recovered_count
    )


    if recovered_count != len(df):

        raise Exception(
            "Recovery validation failed"
        )


    print("="*60)
    print("RECOVERY SUCCESS")
    print("="*60)



if __name__ == "__main__":

    main()