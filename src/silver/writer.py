from src.iceberg.arrow import dataframe_to_arrow
from src.silver.iceberg_schema import build_silver_schema
from src.utils.incremental import filter_incremental
from src.utils.schema import enforce_schema


BUSINESS_KEYS = [
    "source",
    "job_id",
]


def get_table_count(table):

    return table.scan().count()



def append_to_silver(table, df):


    new_df = filter_incremental(
        df=df,
        table=table,
        business_keys=BUSINESS_KEYS,
    )


    print(
        f"New Silver Records   : {len(new_df)}"
    )



    if new_df.empty:

        total_records = get_table_count(
            table
        )

        print(
            "Nothing to insert."
        )

        print(
            f"Total Silver Records : {total_records}"
        )

        return



    new_df = enforce_schema(
        new_df
    )


    arrow_table = dataframe_to_arrow(
        new_df,
        build_silver_schema(),
    )


    table.append(
        arrow_table
    )


    total_records = get_table_count(
        table
    )


    print(
        "Silver ingestion completed."
    )

    print(
        f"Total Silver Records : {total_records}"
    )