from src.transform.posted_date import (
    normalize_posted_date
)


SCRAPED_AT = "2026-07-13T12:00:00"


def main():

    print("=" * 60)
    print("POSTED DATE TEST")
    print("=" * 60)

    samples = [

        "2026-07-08",

        "5 hari yang lalu",

        "30+ hari yang lalu",

        "12 jam yang lalu",

    ]

    for value in samples:

        result = normalize_posted_date(
            value,
            SCRAPED_AT
        )

        print(
            f"{value:<20} -> {result}"
        )


if __name__ == "__main__":

    main()