import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}





def extract_detail_metadata(soup):

    job = {}

    # ==========================
    # Job Description
    # ==========================

    desc = soup.find(
        attrs={
            "data-automation": "jobAdDetails"
        }
    )

    if desc:
        job["job_description"] = desc.get_text(
            "\n",
            strip=True
        )
    else:
        job["job_description"] = None

    # ==========================
    # Work Type
    # ==========================

    work_type = soup.find(
        attrs={
            "data-automation": "job-detail-work-type"
        }
    )

    if work_type:
        job["employment_type"] = work_type.get_text(strip=True)
    else:
        job["employment_type"] = None

    # ==========================
    # Salary
    # ==========================

    salary = soup.find(
        attrs={
            "data-automation": "job-detail-salary"
        }
    )

    if salary:
        job["salary"] = salary.get_text(strip=True)
    else:
        job["salary"] = None

    return job