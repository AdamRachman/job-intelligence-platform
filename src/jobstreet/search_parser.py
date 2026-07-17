from bs4 import BeautifulSoup


def get_text(element):
    """
    Safely extract text from BeautifulSoup Tag.
    """

    if element is None:
        return None

    return element.get_text(strip=True)


def extract_search_metadata(job_card):

    """
    Extract metadata from one JobStreet search result card.

    Parameters
    ----------
    job_card : bs4.element.Tag

    Returns
    -------
    dict
    """

    job = {}

    # =====================================
    # Basic Metadata
    # =====================================

    job["source"] = "jobstreet"

    job["job_id"] = job_card.get("data-job-id")

    # =====================================
    # Title
    # =====================================

    title = job_card.find(
        "a",
        attrs={"data-automation": "jobTitle"}
    )

    job["title"] = get_text(title)

    # =====================================
    # Company
    # =====================================

    company = job_card.find(
        "a",
        attrs={"data-automation": "jobCompany"}
    )

    job["company"] = get_text(company)

    # =====================================
    # Location
    # =====================================

    location = job_card.find(
        attrs={
            "data-automation": "jobLocation"
        }
    )

    job["location"] = get_text(location)

    # =====================================
    # Salary
    # =====================================

    job["salary"] = None

    # =====================================
    # Posted Date
    # =====================================

    posted_date = job_card.find(
        "div",
        attrs={"data-automation": "jobListingDate"}
    )

    job["posted_date"] = get_text(posted_date)

    # =====================================
    # Short Description
    # =====================================

    short_description = job_card.find(
        "span",
        attrs={"data-automation": "jobShortDescription"}
    )

    job["short_description"] = get_text(short_description)

    # =====================================
    # Classification
    # =====================================

    classification = job_card.find(
        "span",
        attrs={"data-automation": "jobClassification"}
    )

    job["classification"] = get_text(classification)

    # =====================================
    # Sub Classification
    # =====================================

    subclassification = job_card.find(
        "span",
        attrs={"data-automation": "jobSubClassification"}
    )

    job["sub_classification"] = get_text(subclassification)

    # =====================================
    # Detail URL
    # =====================================

    link = job_card.find(
        "a",
        attrs={
            "data-automation": "job-list-view-job-link"
        }
    )

    if link:

        href = link.get("href")

        if href.startswith("/"):
            href = "https://id.jobstreet.com" + href

        job["detail_url"] = href

    else:

        job["detail_url"] = None

    # =====================================
    # Raw HTML (Optional)
    # =====================================

    # job["search_card_html"] = str(job_card)

    return job