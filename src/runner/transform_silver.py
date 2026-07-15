from src.pipeline.silver_pipeline import (
    transform_source
)


# ==========================================================
# CONFIG
# ==========================================================

SOURCES = [

    "linkedin",

    "jobstreet",

]


# ==========================================================
# MAIN
# ==========================================================

def main():

    total_jobs = 0

    for source in SOURCES:

        print("=" * 60)
        print(f"TRANSFORM {source.upper()}")
        print("=" * 60)

        jobs = transform_source(
            source
        )

        total_jobs += len(jobs)

        print(
            f"Transformed {len(jobs)} jobs"
        )

        print()

    print("=" * 60)
    print(f"TOTAL SILVER JOBS : {total_jobs}")
    print("=" * 60)


if __name__ == "__main__":

    main()