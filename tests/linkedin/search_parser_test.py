from bs4 import BeautifulSoup
from pprint import pprint

from src.linkedin.search_parser import extract_search_metadata


# ====================================================
# Sample LinkedIn Search Card
# ====================================================

HTML = """

<div class="base-search-card">

    <a 
        class="base-card__full-link"
        href="https://www.linkedin.com/jobs/view/data-engineer-4437326656">
    </a>


    <span class="sr-only">
        Data Engineer
    </span>


    <h4 class="base-search-card__subtitle">
        <a>
            PT Example Technology Indonesia
        </a>
    </h4>


    <div class="base-search-card__metadata">

        <span class="job-search-card__location">
            Jakarta, Indonesia
        </span>


        <time 
            class="job-search-card__listdate"
            datetime="2026-07-01">
            1 day ago
        </time>

    </div>

</div>

"""


def main():

    soup = BeautifulSoup(
        HTML,
        "html.parser"
    )


    job_card = soup.find(
        "div",
        class_="base-search-card"
    )


    result = extract_search_metadata(
        job_card
    )


    print("=" * 60)
    print("LINKEDIN SEARCH PARSER TEST")
    print("=" * 60)


    pprint(result)


    print()
    print("=" * 60)
    print("VALIDATION")
    print("=" * 60)


    assert result["source"] == "linkedin"

    assert result["job_id"] == "4437326656"

    assert (
        result["detail_url"]
        ==
        "https://www.linkedin.com/jobs/view/data-engineer-4437326656"
    )

    assert result["title"] == "Data Engineer"

    assert (
        result["company"]
        ==
        "PT Example Technology Indonesia"
    )

    assert (
        result["location"]
        ==
        "Jakarta, Indonesia"
    )

    assert (
        result["posted_date"]
        ==
        "2026-07-01"
    )


    print("PASS")


if __name__ == "__main__":
    main()