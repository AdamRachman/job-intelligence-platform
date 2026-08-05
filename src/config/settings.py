import os


REQUEST_TIMEOUT = 30

REQUEST_DELAY_MIN = 1.5

REQUEST_DELAY_MAX = 3.0

DEFAULT_SORT_MODE = "ListedDate"

DEFAULT_MAX_PAGES = None


# ======================
# Google Sheets
# ======================

SERVICE_ACCOUNT_FILE = (
    "credentials/google-service-account.json"
)

SPREADSHEET_NAME = (
    "Job-Intelligence-Tracker"
)

WORKSHEET_NAME = (
    "Latest Jobs"
)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


# ======================
# Trino
# ======================

TRINO_HOST = os.getenv(
    "TRINO_HOST",
    "localhost",
)

TRINO_PORT = int(
    os.getenv(
        "TRINO_PORT",
        "8080",
    )
)

TRINO_USER = os.getenv(
    "TRINO_USER",
    "admin",
)


TRINO_CATALOG = os.getenv(
    "TRINO_CATALOG",
    "iceberg",
)

TRINO_SCHEMA = os.getenv(
    "TRINO_SCHEMA",
    "gold",
)

# ======================
# ntfy
# ======================

NTFY_BASE_URL = os.getenv(
    "NTFY_BASE_URL",
    "http://ntfy:80"
)

NTFY_TOPIC = os.getenv(
    "NTFY_TOPIC",
    "job-intelligence-adam"
)

NTFY_TIMEOUT = int(
    os.getenv(
        "NTFY_TIMEOUT",
        "10"
    )
)