from src.connector.registry import CONNECTOR_REGISTRY
from src.storage.raw_writer import save_raw
import time
import subprocess
import json
import sys


# ==========================================================
# LINKEDIN FALLBACK SUBPROCESS
# ==========================================================

def restart_linkedin_scrape(
    keyword,
    max_results
):

    print(
        "Restarting LinkedIn scraper process..."
    )


    code = f"""
import json

from src.linkedin.connector import LinkedInConnector


connector = LinkedInConnector()


jobs = connector.scrape(
    keyword="{keyword}",
    max_results={max_results}
)


print(json.dumps(jobs))
"""


    result = subprocess.run(

        [
            sys.executable,
            "-c",
            code
        ],

        capture_output=True,

        text=True

    )


    if result.returncode != 0:

        print(
            "LinkedIn subprocess failed."
        )

        print(
            result.stderr
        )

        return []


    try:

        lines = result.stdout.splitlines()


        json_line = lines[-1]


        logs = lines[:-1]


        # tampilkan log subprocess
        for line in logs:
            print(line)


        jobs = json.loads(
            json_line
        )


        print(
            f"LinkedIn subprocess result : {len(jobs)} jobs"
        )


        return jobs


    except Exception:

        print(
            "Failed parsing subprocess output."
        )

        return []



# ==========================================================
# INGESTION PIPELINE
# ==========================================================

def run_ingestion(
    keywords,
    max_results=10
):

    all_jobs = []


    # ==================================================
    # Temporary collector per source
    # ==================================================

    collected_jobs = {

        "linkedin": [],

        "jobstreet": []

    }



    for idx, keyword in enumerate(keywords, start=1):


        print("=" * 60)
        print(f"KEYWORD {idx} : {keyword}")
        print("=" * 60)



        for source, connector in CONNECTOR_REGISTRY.items():


            print("=" * 60)
            print(
                f"SCRAPING {source.upper()}"
            )
            print("=" * 60)



            jobs = connector.scrape(

                keyword=keyword,

                max_results=max_results

            )



            # ==================================================
            # LinkedIn fallback
            # ==================================================

            if (

                source == "linkedin"

                and len(jobs) == 0

            ):

                print(
                    "LinkedIn returned empty result."
                )


                max_try = 3


                for attempt in range(max_try):


                    print(
                        f"LinkedIn fallback attempt "
                        f"{attempt + 1}/{max_try}"
                    )


                    jobs = restart_linkedin_scrape(

                        keyword,

                        max_results

                    )



                    if len(jobs) > 0:


                        print(
                            "LinkedIn fallback succeeded."
                        )

                        break



                    print(
                        "LinkedIn still returned empty result."
                    )


                    if attempt < max_try - 1:

                        print(
                            "Waiting 30 seconds before retry..."
                        )

                        time.sleep(10)



            # ==================================================
            # Collect Raw Data
            # ==================================================

            collected_jobs[source].extend(
                jobs
            )


            all_jobs.extend(
                jobs
            )


            print()



    # ==================================================
    # Save Raw Layer (once per source)
    # ==================================================

    for source, jobs in collected_jobs.items():


        save_raw(

            jobs,

            source

        )



    return all_jobs