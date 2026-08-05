from src.bronze.table import get_or_create_table
from src.bronze.reader import read_raw_files
from src.bronze.writer import append_to_bronze



def main():

    print("=" * 60)
    print("BRONZE INGESTION")
    print("=" * 60)


    table = get_or_create_table()


    records = read_raw_files()


    print()

    print(f"Input Raw Records : {len(records)}")


    if not records:

        print("No raw data found.")
        return


    append_to_bronze(
        table,
        records
    )


if __name__ == "__main__":
    main()