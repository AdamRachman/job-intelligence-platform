import requests
from bs4 import BeautifulSoup

SEARCH_URL = "https://id.jobstreet.com/id/junior-data-engineer-scientist-fresh-graduate-jobs"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}


def test_discovery():

    response = requests.get(
        SEARCH_URL,
        headers=HEADERS
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    job_cards = soup.find_all(
        "article",
        attrs={
            "data-testid": "job-card"
        }
    )

    print("=" * 60)
    print("JOBSTREET DISCOVERY TEST")
    print("=" * 60)

    print("Job Cards :", len(job_cards))

    assert len(job_cards) > 0

    print("[PASS] Job cards discovered")

    first_card = job_cards[0]

    assert first_card.has_attr("data-job-id")

    print("[PASS] Job ID Found")

    link = first_card.find(
        "a",
        attrs={
            "data-automation": "job-list-view-job-link"
        }
    )

    assert link is not None

    print("[PASS] Detail URL Found")


if __name__ == "__main__":
    test_discovery()