from src.linkedin.connector import LinkedInConnector


KEYWORD = "Data AI Engineer"


def main():

    connector = LinkedInConnector()

    jobs = connector.scrape(
        keyword=KEYWORD,
        location="Indonesia",
        max_results=5
    )

    print()
    print("=" * 60)
    print(f"TOTAL JOBS : {len(jobs)}")
    print("=" * 60)

    if not jobs:

        print("No jobs found.")
        return

    print("\nFirst 5 Jobs")
    print("-" * 60)

    for i, job in enumerate(jobs[:5], start=1):

        print(
            f"{i:02d}. "
            f"{job['title']} | "
            f"{job['company']} | "
            f"{job['posted_date']}"
        )

    print("\n...")

    print("\nLast 5 Jobs")
    print("-" * 60)

    start = max(len(jobs) - 5, 0)

    for i, job in enumerate(jobs[start:], start=start + 1):

        print(
            f"{i:02d}. "
            f"{job['title']} | "
            f"{job['company']} | "
            f"{job['posted_date']}"
        )

    print()

    print("=" * 60)
    print("FIRST JOB DETAIL")
    print("=" * 60)

    first = jobs[0]

    for key, value in first.items():

        print(f"{key:20}: {value}")


if __name__ == "__main__":
    main()