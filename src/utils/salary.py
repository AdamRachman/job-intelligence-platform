import re


def parse_salary(salary_raw):
    """
    Parse salary text into numeric minimum and maximum salary.

    Examples
    --------
    Rp 5.800.000 – Rp 7.000.000 per month
        -> (5800000, 7000000)

    Rp 8.000.000 per month
        -> (8000000, 8000000)

    None
        -> (None, None)
    """

    if salary_raw is None:
        return None, None

    salary_raw = str(salary_raw).strip()

    if salary_raw == "":
        return None, None

    # Normalize different dash characters
    salary_raw = (
        salary_raw
        .replace("–", "-")
        .replace("—", "-")
    )

    # Extract every numeric value
    numbers = re.findall(
        r"\d[\d\.]*",
        salary_raw
    )

    if not numbers:
        return None, None

    values = [
        int(num.replace(".", ""))
        for num in numbers
    ]

    if len(values) == 1:
        return values[0], values[0]

    return min(values), max(values)