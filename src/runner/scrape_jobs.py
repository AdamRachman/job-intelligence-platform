from src.pipeline.ingestion import run_ingestion


# ==========================================================
# CONFIG
# ==========================================================

KEYWORD = "Data Engineer"

MAX_RESULTS = 5


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