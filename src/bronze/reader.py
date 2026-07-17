import json
from pathlib import Path


RAW_DIR = Path("data/raw")


def get_latest_raw_files():
    """
    Discover latest raw json file from every source directory.
    """

    latest_files = []

    for source_dir in RAW_DIR.iterdir():

        if not source_dir.is_dir():
            continue

        json_files = list(source_dir.glob("*.json"))

        if not json_files:
            continue


        latest_file = max(
            json_files,
            key=lambda file: file.stat().st_mtime
        )

        latest_files.append(latest_file)


    return latest_files



def read_raw_files():

    records = []

    files = get_latest_raw_files()


    print("Raw files discovered:")

    for file in files:

        print(f"- {file}")

        with open(file, "r", encoding="utf-8") as f:

            data = json.load(f)


        records.extend(data)


    return records