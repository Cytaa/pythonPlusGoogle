import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date


class connToGoogle:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)

        self.sheet = client.open("Copy of Legislators 2017").sheet1
        
        self.checkTitles()
    
    def printAllRecords(self):
        listOfAll = self.sheet.get_all_records()

        for i in range(len(listOfAll)):
            print(listOfAll[i])
    
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

    def checkTitles(self):
        if self.sheet.cell(1,1) != "Data":
            self.sheet.update_cell(1,1,"Data")
        
        if  self.sheet.cell(1,2) != "Value":
            self.sheet.update_cell(1,2,"Value")
        
            if  self.sheet.cell(1,3) != "Limit":
                self.sheet.update_cell(1,3,"Limit")
    
    def setLimit(self, limit):
        self.setACell(2,3,limit)
    
            
        
        

