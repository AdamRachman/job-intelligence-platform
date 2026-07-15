from copy import deepcopy


JOB_SCHEMA = {

    # ==================================================
    # SOURCE
    # ==================================================

    "source": None,
    "job_id": None,
    "detail_url": None,

    # ==================================================
    # BASIC INFORMATION
    # ==================================================

    "title": None,
    "company": None,
    "location": None,
    "posted_date": None,

    # ==================================================
    # JOB DETAILS
    # ==================================================

    "employment_type": None,
    "salary": None,

    "classification": None,
    "sub_classification": None,

    "seniority_level": None,
    "job_function": None,
    "industry": None,

    # ==================================================
    # DESCRIPTION
    # ==================================================

    "short_description": None,
    "job_description": None,

    "scraped_at": None,
}


def create_job():

    return deepcopy(JOB_SCHEMA)