import requests

from bs4 import BeautifulSoup

from src.jobstreet.search_parser import extract_search_metadata


SEARCH_URL = "https://id.jobstreet.com/id/junior-data-engineer-scientist-fresh-graduate-jobs"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}


def test_search_parser():

    response = requests.get(
        SEARCH_URL,
        headers=HEADERS
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    cards = soup.find_all(
        "article",
        attrs={
            "data-testid": "job-card"
        }
    )

    assert len(cards) > 0

    first_card = cards[0]

    job = extract_search_metadata(first_card)

    print("=" * 60)
    print("SEARCH PARSER TEST")
    print("=" * 60)

    for k, v in job.items():
        print(f"{k:<15} : {v}")

    # ===================================
    # Validation
    # ===================================

    assert job["source"] == "jobstreet"

    assert job["job_id"] is not None
    
    assert job["title"] is not None

    # assert job["company"] is not None

    assert job["location"] is not None

    assert job["posted_date"] is not None

    assert job["short_description"] is not None

    assert job["classification"] is not None

    assert job["sub_classification"] is not None

    assert job["detail_url"] is not None

    
    print()

    print("[PASS] source")

    print("[PASS] job_id")

    print("[PASS] title")


    if job["company"]:
        print("[PASS] company")
    else:
        print("[INFO] Anonymous Advertiser")

    print("[PASS] location")

    if job["salary"]:
        print("[PASS] salary")
    else:
        print("[INFO] salary unavailable")

    print("[PASS] posted_date")

    print("[PASS] short_description")

    print("[PASS] classification")

    print("[PASS] sub_classification")

    print("[PASS] detail_url")

    print()


if __name__ == "__main__":

    test_search_parser()