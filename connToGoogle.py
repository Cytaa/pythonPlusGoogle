import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date


class connToGoogle:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)

        self.sheet = client.open("Copy of Legislators 2017").sheet1
    
    def printAllRecords(self):
        print(self.sheet.get_all_records())
    
    def clearAllRecords(self):
        self.sheet.clear()
    
    def setACell(self, row, column, data):
        self.sheet.update_cell(row, column, data)
    
    def getCell(self, row, column):
        return self.sheet.cell(row, column)

    def printCell(self, row, column):
        print(self.getCell(row, column))

    def insertData(self, data):
        row = self.nextAvilible()
        self.setACell(row,1,date.today().strftime("%d/%m/%Y"))
        self.setACell(row,2,data)
    
    def nextAvilible(self):
        strList = self.sheet.get_all_records()
        return len(strList) + 2 



