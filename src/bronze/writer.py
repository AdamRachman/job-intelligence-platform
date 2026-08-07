import pandas as pd

from src.bronze.iceberg_schema import build_bronze_schema
from src.iceberg.arrow import dataframe_to_arrow
from src.utils.incremental import filter_incremental

BUSINESS_KEYS = [
    "source",
    "job_id"
]

def enforce_schema(df):

    columns = [
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
        "scraped_at",
    ]


    for col in columns:

        if col in df.columns:
            df[col] = df[col].astype("string")


    return df

def get_table_count(table):

    return (
        table
        .scan()
        .to_arrow()
        .num_rows
    )

def append_to_bronze(table, records):


    # 1. Convert records to dataframe

    df = pd.DataFrame(records)
    # Remove duplicates generated from multi-keyword scraping
    df = df.drop_duplicates(
        subset=BUSINESS_KEYS,
        keep="first",
    )




    # 2. Incremental load with business key

    new_df = filter_incremental(
        df=df,
        table=table,
        business_keys=BUSINESS_KEYS,
    )


    print(
        f"New Bronze Records   : {len(new_df)}"
    )



    if new_df.empty:

        total_records = get_table_count(
            table
        )

        print(
            "Nothing to insert."
        )

        print(
            f"Total Bronze Records: {total_records}"
        )

        return



    # 3. Schema enforcement

    new_df = enforce_schema(
        new_df
    )



    # 4. Pandas -> PyArrow

    arrow_table = dataframe_to_arrow(
        new_df,
        build_bronze_schema(),
    )



    # 5. Append Iceberg

    table.append(
        arrow_table
    )


    total_records = get_table_count(
        table
    )


    print(
        "Bronze ingestion completed."
    )

    print(
        f"Total Bronze Records: {total_records}"
    )