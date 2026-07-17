import re
from datetime import datetime, timedelta

import pandas as pd

from src.utils.salary import parse_salary
from zoneinfo import ZoneInfo

# ==========================================================
# BASIC CLEANING
# ==========================================================

def clean_text(value):

    if pd.isna(value):
        return None

    value = str(value)

    value = value.strip()

    value = re.sub(r"\s+", " ", value)

    return value if value else None

# ==========================================================
# LOCATION
# ==========================================================

def normalize_location(value):

    if pd.isna(value):
        return None

    value = clean_text(value)

    if value is None:
        return None

    # LinkedIn
    if value.startswith("Greater "):
        value = value.replace("Greater ", "")

    return value

# ==========================================================
# JOB DESCRIPTION
# ==========================================================

def clean_job_description(value):

    if pd.isna(value):
        return None

    value = str(value)

    value = value.replace("\r", "")

    value = re.sub(r"\n{2,}", "\n", value)

    value = re.sub(r"[ \t]+", " ", value)

    return value.strip()


# ==========================================================
# CLASSIFICATION
# ==========================================================

def normalize_classification(value):

    if pd.isna(value):
        return None

    value = str(value)

    value = value.strip()

    value = value.replace("(", "")

    value = value.replace(")", "")

    return value


# ==========================================================
# EMPLOYMENT TYPE
# ==========================================================

EMPLOYMENT_MAPPING = {

    "Full time": "FULL_TIME",

    "Full-time": "FULL_TIME",

    "Part time": "PART_TIME",
    
    "Kontrak/Temporer": "CONTRACT",

    "Contract": "CONTRACT",

    "Internship": "INTERNSHIP",

    "Temporary": "TEMPORARY",

}


def normalize_employment_type(value):

    if pd.isna(value):

        return None

    return EMPLOYMENT_MAPPING.get(

        str(value).strip(),

        str(value).upper()

    )

# ==========================================================
# SENIORITY LEVEL
# ==========================================================

SENIORITY_MAPPING = {

    "Not Applicable": None,
    "Tidak Berlaku": None,
    "Entry level": "Entry Level",
    # "Associate": "Associate",
    "Mid-Senior level": "Mid-Senior Level",
}


def normalize_seniority(value):

    if pd.isna(value):

        return None

    value = clean_text(value)

    if value is None:

        return None

    return SENIORITY_MAPPING.get(
        value,
        value
    )

# ==========================================================
# POSTED DATE
# ==========================================================

def normalize_posted_date_clean(value, scraped_at):

    if pd.isna(value) or pd.isna(scraped_at):
        return None

    value = str(value).strip()

    # ==========================================
    # Base date = waktu scraping
    # ==========================================

    try:
        base_date = datetime.fromisoformat(str(scraped_at))
    except Exception:
        return None

    # ==========================================
    # Absolute Date (LinkedIn)
    # ==========================================

    try:
        parsed = datetime.strptime(value, "%Y-%m-%d")
        return parsed.date().isoformat()
    except ValueError:
        pass

    value = value.lower()

    # ==========================================
    # JobStreet Indonesia
    # ==========================================

    m = re.match(r"(\d+)\s*menit", value)
    if m:
        return base_date.date().isoformat()

    m = re.match(r"(\d+)\s*jam", value)
    if m:
        return base_date.date().isoformat()

    m = re.match(r"(\d+)\s*hari", value)
    if m:
        return (
            base_date - timedelta(days=int(m.group(1)))
        ).date().isoformat()

    if "kemarin" in value:
        return (
            base_date - timedelta(days=1)
        ).date().isoformat()

    # ==========================================
    # LinkedIn Relative Date
    # ==========================================

    m = re.match(r"(\d+)\s*minute", value)
    if m:
        return base_date.date().isoformat()

    m = re.match(r"(\d+)\s*minutes", value)
    if m:
        return base_date.date().isoformat()

    m = re.match(r"(\d+)\s*hour", value)
    if m:
        return base_date.date().isoformat()

    m = re.match(r"(\d+)\s*hours", value)
    if m:
        return base_date.date().isoformat()

    m = re.match(r"(\d+)\s*day", value)
    if m:
        return (
            base_date - timedelta(days=int(m.group(1)))
        ).date().isoformat()

    m = re.match(r"(\d+)\s*days", value)
    if m:
        return (
            base_date - timedelta(days=int(m.group(1)))
        ).date().isoformat()

    if value == "today":
        return base_date.date().isoformat()

    if value == "yesterday":
        return (
            base_date - timedelta(days=1)
        ).date().isoformat()

    return None


# ==========================================================
# MAIN PIPELINE
# ==========================================================

def transform(df):

    now = datetime.now(
        ZoneInfo("Asia/Jakarta")
    )

    df = df.copy()

    string_columns = [

        "title",

        "company",

        "location",

        "salary",

        "short_description",

        "job_description",

        "classification",

        "sub_classification",

        "industry",

        "job_function",

        "seniority_level",

    ]

    for col in string_columns:

        if col in df.columns:

            df[col] = df[col].apply(clean_text)
    
    df["location"] = df["location"].apply(
        normalize_location
    )

    df["classification"] = df["classification"].apply(
        normalize_classification
    )

    df["employment_type"] = df["employment_type"].apply(
        normalize_employment_type
    )

    df["seniority_level"] = df["seniority_level"].apply(
        normalize_seniority
    )

# ==========================================
# Salary Normalization
# ==========================================

    df["salary_raw"] = df["salary"]

    df[
        [
            "salary_min",
            "salary_max"
        ]
    ] = df["salary_raw"].apply(
        lambda x: pd.Series(
            parse_salary(x)
        )
    )

    df["salary_min"] = (
        pd.to_numeric(
            df["salary_min"],
            errors="coerce"
        )
        .astype("Int64")
    )

    df["salary_max"] = (
        pd.to_numeric(
            df["salary_max"],
            errors="coerce"
        )
        .astype("Int64")
    )

    df.drop(
        columns=["salary"],
        inplace=True,
    )

    df["posted_date_raw"] = df["posted_date"]

    df["posted_date_clean"] = df.apply(
        lambda row: normalize_posted_date_clean(
            row["posted_date"],
            row["scraped_at"],
        ),
        axis=1,
    )

    df["job_description_clean"] = df["job_description"].apply(
        clean_job_description
    )

    df["processed_at"] = now.isoformat()

    df = df.drop(columns=["posted_date"])

    return df