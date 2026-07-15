# ==========================================================
# Employment Type Mapping
# ==========================================================

EMPLOYMENT_MAPPING = {

    # Full Time
    "full time": "full_time",
    "full-time": "full_time",
    "fulltime": "full_time",
    "tetap": "full_time",

    # Part Time
    "part time": "part_time",
    "part-time": "part_time",

    # Contract
    "contract": "contract",
    "kontrak": "contract",
    "kontrak/temporer": "contract",
    "temporary": "contract",
    "temporer": "contract",

    # Internship
    "internship": "internship",
    "intern": "internship",
    "magang": "internship",
}


# ==========================================================
# Normalize Employment Type
# ==========================================================

def normalize_employment_type(value):

    if value is None:
        return None

    value = value.strip().lower()

    return EMPLOYMENT_MAPPING.get(
        value,
        value
    )