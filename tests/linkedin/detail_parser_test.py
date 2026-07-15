from pprint import pprint

from src.linkedin.connector import LinkedInConnector
from src.linkedin.detail_parser import (
    extract_detail_metadata
)


JOB_ID = "4435506324"


def main():

    connector = LinkedInConnector()

    soup = connector.fetch_detail_page(
        JOB_ID
    )

    print("=" * 60)
    print("LINKEDIN DETAIL PARSER TEST")
    print("=" * 60)

    result = extract_detail_metadata(
        soup
    )

    print()

    pprint(result)

    # ====================================================
    # Validation
    # ====================================================

    print()
    print("=" * 60)
    print("VALIDATION")
    print("=" * 60)

    expected_fields = [

        "job_description",

        "employment_type",

        "seniority_level",

        "job_function",

        "industry",

    ]

    for field in expected_fields:

        assert result[field] is not None

        print(f"[PASS] {field}")


if __name__ == "__main__":

    main()