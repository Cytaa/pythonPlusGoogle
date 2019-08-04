import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
from os import system

class TextMenu:
    def __init__(self):
        self.createTxtMenu()
    
    def createTxtMenu(self):
        print("Welcome!")
        print("press 1 to establishe a connection with google sheets")
        print("press 2 to quit")
        chooser = int(input("Enter a number: "))

        if (chooser == 1):
            system("cls")
            self.connection = connToGoogle()
            print("Connection was established")
            input("Press any key to get back to menu:")

            system("cls")
            self.createTxtMenu()
        elif(chooser == 2):
            sys.exit(0)      
            





class connToGoogle:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)

        self.sheet = client.open("Copy of Legislators 2017").sheet1
    
    def getAllRecords(self):
        print(self.sheet.get_all_records())
        input("Press any key to get back to menu:")
        
        




menu = TextMenu()