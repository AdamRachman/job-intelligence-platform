from src.bronze.table import get_or_create_table as get_bronze_table
from src.silver.table import get_or_create_table as get_silver_table
from src.silver.transform import transform
from src.silver.writer import append_to_silver


def main():

    print("=" * 60)

    print("SILVER TRANSFORMATION")

    print("=" * 60)

    bronze = get_bronze_table()

    silver = get_silver_table()

    print()

    print("Reading Bronze...")

    arrow = bronze.scan().to_arrow()

    df = arrow.to_pandas()

    print(f"Bronze records : {len(df)}")

    if df.empty:

        print("Nothing to process.")

        return

    print("Transforming...")

    df = transform(df)

    append_to_silver(
        silver,
        df,
    )

    print()

    print("Silver transformation completed.")


if __name__ == "__main__":

    main()