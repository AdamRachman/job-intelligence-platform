from src.pipeline.ingestion import run_ingestion


# ==========================================================
# CONFIG
# ==========================================================

KEYWORD = "Junior Data AI Engineer Scientist"

MAX_RESULTS = 25


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    jobs = run_ingestion(
        keyword=KEYWORD,
        max_results=MAX_RESULTS
    )

    print()

    print("=" * 60)
    print(f"TOTAL JOBS : {len(jobs)}")
    print("=" * 60)