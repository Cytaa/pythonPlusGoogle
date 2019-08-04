import gspread
from oauth2client.service_account import ServiceAccountCredentials



class connToGoogle:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)

        self.sheet = client.open("Copy of Legislators 2017").sheet1
    
    def getAllRecords(self):
        print(self.sheet.get_all_records())
        input("Press any key to get back to menu:")