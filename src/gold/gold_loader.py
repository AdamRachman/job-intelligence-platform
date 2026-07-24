from src.silver.table import get_or_create_table as get_silver_table
from src.gold.table import get_or_create_table as get_gold_table

from src.gold.transform import transform

from src.utils.schema import enforce_schema
from src.utils.incremental import filter_incremental

from src.gold.iceberg_schema import build_gold_schema
from src.iceberg.arrow import dataframe_to_arrow


BUSINESS_KEYS = [

    "source",
    "job_id",

]


def main():

    print("=" * 60)
    print("GOLD ENRICHMENT")
    print("=" * 60)

    silver = get_silver_table()

    gold = get_gold_table()

    print()

    print("Reading Silver...")

    df = silver.scan().to_arrow().to_pandas()

    print(f"Silver records : {len(df)}")

    if df.empty:

        print("Nothing to process.")

        return

    print("Business Enrichment...")

    df = transform(df)

    df = filter_incremental(
        df=df,
        table=gold,
        business_keys=BUSINESS_KEYS,
    )

    print(f"New records : {len(df)}")

    if df.empty:

        print("Nothing to insert.")

        return

    df = enforce_schema(df)

    arrow_table = dataframe_to_arrow(
        df,
        build_gold_schema(),
    )

    gold.append(arrow_table)

    print()
    print("Gold enrichment completed.")


if __name__ == "__main__":

    main()