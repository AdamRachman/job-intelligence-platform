import json

from pathlib import Path

from src.transform.silver_transform import transform_jobs
from src.storage.silver_writer import save_silver


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
# Load Latest Raw File
# ==========================================================

def load_latest_raw(source):

    source_dir = (
        RAW_DATA_DIR /
        source
    )

    files = sorted(
        source_dir.glob("*.json")
    )

    if not files:

        raise FileNotFoundError(
            f"No raw file found for {source}"
        )

    latest_file = files[-1]

    with open(
        latest_file,
        "r",
        encoding="utf-8"
    ) as file:

        jobs = json.load(file)

    return jobs


# ==========================================================
# Transform One Source
# ==========================================================

def transform_source(source):

    raw_jobs = load_latest_raw(
        source
    )

    silver_jobs = transform_jobs(
        raw_jobs
    )

    save_silver(
        silver_jobs,
        source
    )

    return silver_jobs