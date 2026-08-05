import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


# Path credential
SERVICE_ACCOUNT_FILE = "credentials/google-service-account.json"

# Spreadsheet name
SPREADSHEET_NAME = "Job-Intelligence-Tracker"

# Google API scope
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def test_google_sheet_connection():

    try:
        # Authenticate
        credentials = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES
        )

        client = gspread.authorize(credentials)

        print("[PASS] Authentication success")


        # Open spreadsheet
        spreadsheet = client.open(SPREADSHEET_NAME)

        print(f"[PASS] Spreadsheet found: {spreadsheet.title}")


        # Open Latest Jobs worksheet
        worksheet = spreadsheet.worksheet("Latest Jobs")

        print(f"[PASS] Worksheet found: {worksheet.title}")


        # Dummy row sesuai schema Latest Jobs
        test_row = [
            "test-001",                              # job_id
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # scraped_at
            "test",                                  # source
            "Test Company",                          # company
            "Data Engineer",                         # title
            "Jakarta",                               # location
            "Full Time",                             # employment_type
            "Junior",                                # seniority_level
            "Python, SQL, Airflow, Docker",          # required_skills
            "https://example.com/job/test-001",      # detail_url
            "New",                                   # status
            "",                                      # applied_date
            ""                                       # notes
        ]


        # Append dummy row
        worksheet.append_row(test_row)

        print("[PASS] Dummy row inserted successfully")


    except Exception as e:
        print("[FAILED]")
        print(type(e))
        print(repr(e))


if __name__ == "__main__":
    test_google_sheet_connection()