from src.transform.employment import (
    normalize_employment_type
)


def main():

    print("=" * 60)
    print("EMPLOYMENT TEST")
    print("=" * 60)

    samples = [

        "Full Time",

        "Full-Time",

        "Kontrak/Temporer",

        "Internship",

        "Part Time",

        None

    ]

    for value in samples:

        print(
            value,
            "->",
            normalize_employment_type(value)
        )


if __name__ == "__main__":

    main()