from copy import deepcopy

from src.transform.cleaners import clean_text
from src.transform.employment import normalize_employment_type
from src.transform.posted_date import normalize_posted_date


# ==========================================================
# Transform One Job
# ==========================================================

def transform_job(job):

    job = deepcopy(job)

    # ======================================================
    # Clean all string fields
    # ======================================================

    for key, value in job.items():

        if isinstance(value, str):

            job[key] = clean_text(value)

    # ======================================================
    # Preserve raw posted date
    # ======================================================

    job["posted_date_raw"] = job.get(
        "posted_date"
    )

    # ======================================================
    # Normalize posted date
    # ======================================================

    job["posted_date"] = normalize_posted_date(
        job.get("posted_date_raw"),
        job.get("scraped_at")
    )

    # ======================================================
    # Normalize employment type
    # ======================================================

    job["employment_type"] = normalize_employment_type(
        job.get("employment_type")
    )

    return job


# ==========================================================
# Transform Many Jobs
# ==========================================================

def transform_jobs(jobs):

    return [

        transform_job(job)

        for job in jobs

    ]