from copy import deepcopy


JOB_SCHEMA = {

    # ==========================================
    # SOURCE
    # ==========================================

    "source": None,
    "job_id": None,
    "detail_url": None,

    # ==========================================
    # BASIC INFORMATION
    # ==========================================

    "title": None,
    "company": None,
    "location": None,

    "posted_date_raw": None,
    "posted_date_clean": None,

    # ==========================================
    # JOB DETAILS
    # ==========================================

    "employment_type": None,

    # Original salary text
    "salary_raw": None,

    # Normalized salary
    "salary_min": None,
    "salary_max": None,

    "classification": None,
    "sub_classification": None,

    "seniority_level": None,
    "job_function": None,
    "industry": None,

    # ==========================================
    # DESCRIPTION
    # ==========================================

    "short_description": None,

    "job_description_clean": None,

    "job_description": None,

    # ==========================================
    # METADATA
    # ==========================================

    "scraped_at": None,

    "processed_at": None,
}


def create_job():

    return deepcopy(JOB_SCHEMA)