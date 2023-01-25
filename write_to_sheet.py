import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from dotenv import load_dotenv


load_dotenv()


scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scopes=scope
)
client = gspread.authorize(credentials)


def csv_to_sheet():
    sheet = client.open("parse olx").sheet1

    df = pd.read_csv("apartmens.csv")
    df = df.fillna('')

    sheet.update(df.values.tolist())


if __name__ == '__main__':
    """
    For creation sheet and share with you
    """
    sheet = client.create("parse olx")
    sheet.share(os.environ.get("OWNER_EMAIL"), perm_type="user", role="writer")
