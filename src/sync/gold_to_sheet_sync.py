from src.sheets.client import get_sheet
from src.trino.client import get_trino_connection


# ======================
# Get Existing Rows
# (Debug / Information)
# ======================

def get_existing_rows(sheet):

    values = sheet.get_all_values()

    rows = values[1:]  # Skip header

    return rows


# ======================
# Get Existing Job IDs
# (Incremental Sync)
# ======================

def get_existing_job_ids(sheet):

    values = sheet.get_all_values()

    rows = values[1:]  # Skip header

    job_ids = set()

    for row in rows:

        if row and row[0]:

            job_ids.add(str(row[0]))

    return job_ids


# ======================
# Fetch New Jobs
# ======================

def fetch_new_jobs(existing_job_ids):

    conn = get_trino_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        source,
        job_id,
        detail_url,
        title,
        company,
        location,
        posted_date_clean,
        seniority_level,
        required_skills,
        scraped_at

    FROM iceberg.gold.gold_jobs

    ORDER BY
    posted_date_clean DESC,
    scraped_at DESC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    new_jobs = []

    for row in rows:

        (
            source,
            job_id,
            detail_url,
            title,
            company,
            location,
            posted_date_clean,
            seniority_level,
            required_skills,
            scraped_at

        ) = row

        # Skip existing jobs
        if str(job_id) in existing_job_ids:
            continue

        skills = ", ".join(required_skills) if required_skills else ""

        new_jobs.append(
            [
                job_id,
                scraped_at,
                posted_date_clean,
                source,
                company,
                title,
                location,
                seniority_level,
                skills,
                detail_url,
                "Unapplied",   # Action
                "",            # Applied Date
                ""             # Progress
            ]
        )

    cursor.close()
    conn.close()

    return new_jobs


# ======================
# Sync Gold -> Google Sheet
# ======================

def sync_gold_to_sheet():

    sheet = get_sheet()

    print("[PASS] Connected to Google Sheet")

    existing_rows = get_existing_rows(sheet)

    print(
        f"[INFO] Existing rows: {len(existing_rows)}"
    )

    existing_job_ids = get_existing_job_ids(sheet)

    print(
        f"[INFO] Existing job IDs: {len(existing_job_ids)}"
    )

    new_jobs = fetch_new_jobs(existing_job_ids)

    print(
        f"[INFO] New jobs found: {len(new_jobs)}"
    )

    if not new_jobs:

        print("[INFO] Nothing to sync")

        return

    sheet.insert_rows(
        new_jobs,
        row=2,
    )

    print(
        f"[PASS] Inserted {len(new_jobs)} new jobs"
    )

    total_rows = len(
        get_existing_rows(sheet)
    )

    print(
        f"[INFO] Total rows after sync: {total_rows}"
    )

if __name__ == "__main__":
    sync_gold_to_sheet()