from bs4 import BeautifulSoup


# ==========================================================
# JOB CRITERIA LABELS
# ==========================================================

JOB_CRITERIA = {

    "employment_type": [
        "employment type",
        "jenis pekerjaan",
    ],

    "seniority_level": [
        "seniority level",
        "tingkat senioritas",
    ],

    "job_function": [
        "job function",
        "fungsi pekerjaan",
    ],

    "industry": [
        "industry",
        "industri",
    ],
}


# ==========================================================
# MAIN
# ==========================================================

def extract_detail_metadata(soup):

    result = {

        "job_description": extract_description(soup)

    }

    for field, labels in JOB_CRITERIA.items():

        result[field] = extract_job_criteria(
            soup,
            labels
        )

    return result


# ==========================================================
# JOB DESCRIPTION
# ==========================================================

def extract_description(soup):

    description_div = soup.find(
        "div",
        class_=lambda x:
            x and "show-more-less-html__markup" in x
    )

    if description_div is None:
        return None

    return description_div.get_text(
        separator="\n",
        strip=True
    )


# ==========================================================
# GENERIC JOB CRITERIA
# ==========================================================

def extract_job_criteria(soup, labels):

    headers = soup.find_all(
        "h3",
        class_="description__job-criteria-subheader"
    )

    for header in headers:

        text = header.get_text(
            strip=True
        ).lower()

        if any(label in text for label in labels):

            value = header.find_next(
                "span",
                class_="description__job-criteria-text description__job-criteria-text--criteria"
            )

            if value:
                return value.get_text(strip=True)

    return None