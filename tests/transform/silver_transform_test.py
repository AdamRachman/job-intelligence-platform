from pprint import pprint

from src.transform.silver_transform import (
    transform_job
)


def main():

    print("=" * 60)
    print("SILVER TRANSFORM TEST")
    print("=" * 60)

    raw_job = {

        "source": "jobstreet",

        "title": "Data Engineer",

        "company": "PT ABC",

        "classification": "(Teknologi Informasi & Komunikasi)",

        "employment_type": "Kontrak/Temporer",

        "posted_date": "5 hari yang lalu",

        "job_description": "Hello\n\nWorld\xa0",

        "scraped_at": "2026-07-13T12:00:00"

    }

    silver = transform_job(
        raw_job
    )

    pprint(silver)

    print()

    assert silver["employment_type"] == "contract"

    assert silver["posted_date"] == "2026-07-08"

    assert silver["posted_date_raw"] == "5 hari yang lalu"

    assert (
        silver["classification"]
        ==
        "Teknologi Informasi & Komunikasi"
    )

    assert (
        silver["job_description"]
        ==
        "Hello World"
    )

    print("[PASS]")


if __name__ == "__main__":

    main()