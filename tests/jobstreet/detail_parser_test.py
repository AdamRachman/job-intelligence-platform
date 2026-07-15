from src.jobstreet.connector import JobStreetConnector
from src.jobstreet.detail_parser import (
    extract_detail_metadata
)


DETAIL_URL = (
    "https://id.jobstreet.com/id/job/93197408"
)


def main():

    connector = JobStreetConnector()

    soup = connector.fetch_detail_page(
        DETAIL_URL
    )

    print("=" * 60)
    print("DETAIL PARSER TEST")
    print("=" * 60)

    detail = extract_detail_metadata(soup)

    print("employment_type :", detail["employment_type"])
    print("salary          :", detail["salary"])
    print("job_description :")
    print(detail["job_description"][:500])

    print()

    # ==========================
    # Assertions
    # ==========================

    assert detail["job_description"] is not None
    print("[PASS] job_description")

    assert detail["employment_type"] is not None
    print("[PASS] employment_type")

    if detail["salary"] is None:
        print("[INFO] salary unavailable")
    else:
        print("[PASS] salary")

    # ==========================
    # Save HTML
    # ==========================

    with open(
        "sample_detail.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(soup.prettify())

    # ==========================
    # Save Text
    # ==========================

    with open(
        "sample_detail.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(soup.get_text("\n", strip=True))


if __name__ == "__main__":
    main()