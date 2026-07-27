import re
import pandas as pd
from src.ai.enrich import enrich_job
import time

WFH_KEYWORDS = [

    "remote",
    "wfh",
    "work from home",
    "remotely"
]

HYBRID_KEYWORDS = [

    "hybrid"
]

WFO_KEYWORDS = [

    "onsite",
    "on-site",
    "office",
    "wfo",
    "work from office"

]

def is_empty(value):

    return (
        pd.isna(value)
        or str(value).strip() == ""
        or str(value).lower() == "none"
    )


def get_work_arrangement(row):

    text = " ".join(

        filter(None, [
            row.get("title"),
            row.get("short_description"),
            row.get("job_description_clean"),
        ])

    ).lower()

    for keyword in WFH_KEYWORDS:

        if keyword in text:

            return "WFH"

    for keyword in HYBRID_KEYWORDS:

        if keyword in text:

            return "HYBRID"

    for keyword in WFO_KEYWORDS:

        if keyword in text:

            return "WFO"

    return "WFO"


def transform(df):

    df = df.copy()


    # ======================================================
    # Business Enrichment
    # ======================================================

    df["work_arrangement"] = df.apply(
        get_work_arrangement,
        axis=1,
    )


    # ======================================================
    # AI Enrichment
    # ======================================================

    if "required_skills" not in df.columns:

        df["required_skills"] = None


    for index, row in df.iterrows():

        need_ai = (

            is_empty(row["seniority_level"])

            or

            is_empty(row["required_skills"])

        )


        if not need_ai:

            continue


        time.sleep(3)


        result = enrich_job(

            title=row["title"],

            description=row["job_description_clean"],

        )


        if is_empty(row["seniority_level"]):

            df.at[index, "seniority_level"] = result.seniority_level


        if is_empty(row["required_skills"]):

            df.at[index, "required_skills"] = result.required_skills


    return df