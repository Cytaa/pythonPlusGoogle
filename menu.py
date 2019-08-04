import sys
from os import system
from connToGoogle import connToGoogle

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
            input("Press any key to continue:")
            system("cls")
            self.createSheetMenu()

            system("cls")
            self.createTxtMenu()
        elif(chooser == 2):
            sys.exit(0)
    
    def createSheetMenu(self):
        print("""press 1 to view all roves
        press 2 to clear all cells in sheet
        press 3 to get back to the main menu
            """)
        chooser = int(input("input the number and press ender to confirm"))

        if chooser == 1:
            system("cls")
            self.connection.printAllRecords()
        elif chooser == 2:
            system("cls")
            self.connection.clearAllRecords()
        elif chooser == 3:
            system("cls")
            self.createTxtMenu()
            
            






        
        




menu = TextMenu()