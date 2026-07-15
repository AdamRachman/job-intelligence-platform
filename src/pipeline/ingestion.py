from src.connector.registry import CONNECTOR_REGISTRY
from src.storage.raw_writer import save_raw


# ==========================================================
# INGESTION PIPELINE
# ==========================================================

def run_ingestion(
    keyword,
    max_results=10
):

    all_jobs = []

    for source, connector in CONNECTOR_REGISTRY.items():

        print("=" * 60)
        print(f"SCRAPING {source.upper()}")
        print("=" * 60)

        jobs = connector.scrape(
            keyword=keyword,
            max_results=max_results
        )

        save_raw(
            jobs,
            source
        )

        all_jobs.extend(jobs)

        print()

    return all_jobs