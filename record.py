import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_creds.json', scope)
sheet = gspread.authorize(creds).open('Crypto交易紀錄').sheet1

def record_to_google_sheets(data):
    sheet.append_row([
        data.get('timestamp'),
        data.get('symbol'),
        data.get('side'),
        data.get('entry_price'),
        data.get('exit_price'),
        data.get('profit'),
        data.get('strategy')
    ])