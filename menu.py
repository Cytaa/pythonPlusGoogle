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
            input("Press any key to get back to menu:")

            system("cls")
            self.createTxtMenu()
        elif(chooser == 2):
            sys.exit(0)      
            






        
        




menu = TextMenu()