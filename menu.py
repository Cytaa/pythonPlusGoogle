import gspread
from oauth2client.service_account import ServiceAccountCredentials

class TextMenu:
    def __init__(self):
        self.createTxtMenu()
    
    def createTxtMenu(self):
        print("Welcome!")
        print("press 1 to establishe a connection with google sheets")
        print("press 2 to quit")
        self.chooser = int(input("Enter a number: "))
    
    def estabAConnect(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)

        self.sheet = client.open("Copy of Legislators 2017").sheet1

    def showAllRecords(self):
        print(self.sheet.get_all_records())
        




menu = TextMenu()