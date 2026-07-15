from urllib.parse import urlparse

from bs4 import BeautifulSoup


def extract_job_id(url):
    """
    Extract LinkedIn job id from job URL.

    Example:
    https://www.linkedin.com/jobs/view/data-engineer-4437326656
    -> 4437326656
    """

    if not url:
        return None

    try:
        path = urlparse(url).path

        # /jobs/view/data-engineer-4437326656/
        job_id = path.rstrip("/").split("-")[-1]

        return job_id

    except Exception:
        return None


def extract_search_metadata(job_card):

    """
    Extract metadata from LinkedIn search card.

    Input:
        BeautifulSoup Tag
        <div class="base-search-card">

    Output:
        Dictionary metadata
    """

    # ==========================================
    # Detail URL + Job ID
    # ==========================================

    link_tag = job_card.find(
        "a",
        class_="base-card__full-link"
    )

    detail_url = None
    job_id = None

    if link_tag and link_tag.get("href"):

        detail_url = (
            link_tag["href"]
            .split("?")[0]
        )

        job_id = extract_job_id(
            detail_url
        )


    # ==========================================
    # Title
    # ==========================================

    title_tag = job_card.find(
        "span",
        class_="sr-only"
    )

    title = (
        title_tag.get_text(strip=True)
        if title_tag
        else None
    )


    # ==========================================
    # Company
    # ==========================================

    company = None

    company_tag = job_card.find(
        "h4",
        class_="base-search-card__subtitle"
    )

    if company_tag:

        company_link = company_tag.find("a")

        if company_link:
            company = company_link.get_text(
                strip=True
            )

        else:
            company = company_tag.get_text(
                strip=True
            )


    # ==========================================
    # Location
    # ==========================================

    location = None

    location_tag = job_card.find(
        "span",
        class_="job-search-card__location"
    )

    if location_tag:

        location = location_tag.get_text(
            strip=True
        )


    # ==========================================
    # Posted Date
    # ==========================================

    posted_date = None

    date_tag = job_card.find(
        "time",
        class_="job-search-card__listdate"
    )

    if date_tag:

        posted_date = date_tag.get(
            "datetime"
        )


    return {

        "source": "linkedin",

        "job_id": job_id,

        "detail_url": detail_url,

        "title": title,

        "company": company,

        "location": location,

        "posted_date": posted_date,
    }