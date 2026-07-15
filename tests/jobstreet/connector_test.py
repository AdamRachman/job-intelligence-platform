from src.jobstreet.connector import JobStreetConnector
from pprint import pprint

KEYWORD = "Junior AI Data Engineer Scientist"


def main():

    connector = JobStreetConnector()

    jobs = connector.scrape(
        keyword=KEYWORD,
        max_pages=1
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
    
    pprint(jobs[0])


if __name__ == "__main__":
    main()