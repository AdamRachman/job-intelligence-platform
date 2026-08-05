import gspread

from google.oauth2.service_account import Credentials

from src.config.settings import (
    SERVICE_ACCOUNT_FILE,
    SPREADSHEET_NAME,
    WORKSHEET_NAME,
    SCOPES,
)

# ======================
# Google Sheet Connection
# ======================

def get_sheet():

    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    spreadsheet = client.open(SPREADSHEET_NAME)

    worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

    return worksheet