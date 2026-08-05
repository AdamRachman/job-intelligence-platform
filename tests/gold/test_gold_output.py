from src.gold.gold_loader import main


if __name__ == "__main__":

    jobs = main()

    print("=" * 60)
    print("GOLD OUTPUT TEST")
    print("=" * 60)


    print(
        f"Total new jobs: {len(jobs)}"
    )


    for job in jobs[:3]:

        print("\n--- JOB ---")

        print(
            job
        )