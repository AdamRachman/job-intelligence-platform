import json

from pathlib import Path
from datetime import datetime


# ==========================================================
# PROJECT PATH
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = (
    PROJECT_ROOT /
    "data" /
    "raw"
)


# ==========================================================
# SAVE RAW JSON
# ==========================================================

def save_raw(
    jobs,
    source
):

    # ------------------------------------------
    # Create source folder
    # ------------------------------------------

    source_dir = (
        RAW_DATA_DIR /
        source
    )

    source_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # ------------------------------------------
    # Generate filename
    # ------------------------------------------

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    scraped_at = datetime.now().strftime(
    "%Y-%m-%dT%H:%M:%S"
)

    filename = (
        f"{source}_{timestamp}.json"
    )

    filepath = (
        source_dir /
        filename
    )

    # ------------------------------------------
    # Save JSON
    # ------------------------------------------
    
    for job in jobs:

        job["scraped_at"] = scraped_at   

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

    return filepath