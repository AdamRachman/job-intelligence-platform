import json

from pathlib import Path
from datetime import datetime


# ==========================================================
# PROJECT PATH
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SILVER_DATA_DIR = (
    PROJECT_ROOT /
    "data" /
    "silver"
)


# ==========================================================
# SAVE SILVER JSON
# ==========================================================

def save_silver(
    jobs,
    source
):

    # ------------------------------------------------------
    # Create source folder
    # ------------------------------------------------------

    source_dir = (
        SILVER_DATA_DIR /
        source
    )

    source_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # ------------------------------------------------------
    # Generate filename
    # ------------------------------------------------------

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{source}_{timestamp}.json"
    )

    filepath = (
        source_dir /
        filename
    )

    # ------------------------------------------------------
    # Save JSON
    # ------------------------------------------------------

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            jobs,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Saved {len(jobs)} jobs -> {filepath}")

    return filepath