from datetime import datetime, timedelta
import re


# ==========================================================
# Normalize Posted Date
# ==========================================================

def normalize_posted_date(
    posted_date_raw,
    scraped_at_raw
):

    if posted_date_raw is None:
        return None

    posted_date_raw = posted_date_raw.strip()

    # ======================================================
    # Parse scraped_at
    # ======================================================

    scraped_at = datetime.fromisoformat(
        scraped_at_raw
    )

    # ======================================================
    # LinkedIn
    # Example:
    # 2026-07-08
    # ======================================================

    try:

        return datetime.strptime(
            posted_date_raw,
            "%Y-%m-%d"
        ).strftime("%Y-%m-%d")

    except ValueError:

        pass

    text = posted_date_raw.lower()

    # ======================================================
    # JobStreet
    # Example:
    # 5 hari yang lalu
    # 30+ hari yang lalu
    # ======================================================

    if "hari" in text:

        match = re.search(
            r"(\d+)",
            text
        )

        if match:

            days = int(
                match.group(1)
            )

            date = (
                scraped_at -
                timedelta(days=days)
            )

            return date.strftime(
                "%Y-%m-%d"
            )

    # ======================================================
    # JobStreet
    # Example:
    # 12 jam yang lalu
    # 3 jam yang lalu
    # ======================================================

    if "jam" in text:

        match = re.search(
            r"(\d+)",
            text
        )

        if match:

            hours = int(
                match.group(1)
            )

            date = (
                scraped_at -
                timedelta(hours=hours)
            )

            return date.strftime(
                "%Y-%m-%d"
            )

    return None