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
    
<<<<<<< HEAD
    
    
=======
>>>>>>> e8790cbcbb20da7741d54b4de075e2878fbc198a
    def createSheetMenu(self):
        print("""press 1 to view all roves: 
press 2 to inesrt new row into the base: 
press 3 to clear all cells: 
press 4 to set a limit to your operations:
press 5 to get back to main menu: 
            """)
        chooser = int(input("input the number and press ender to confirm: "))

        if chooser == 1:
            system("cls")
            self.connection.printAllRecords()
            input("press enter to procede")
            system("cls")
            self.createSheetMenu()
        elif chooser == 2:
            system("cls")
            data = input("insert data: ")
            
            try:
                self.connection.insertData(float(data))    
            except ValueError:
                print("Data must be a number")
<<<<<<< HEAD
            
            #self.budget()
            
            system("cls")
            self.createSheetMenu()

=======

            
>>>>>>> e8790cbcbb20da7741d54b4de075e2878fbc198a
            input("your data was inserted correctly press enter to proceed")
            system("cls")
            self.createSheetMenu()
        elif chooser == 3:
            system("cls")
            self.connection.clearAllRecords()
            input("All cells have been cleared press enter to proceed")
            system("cls")
        elif chooser == 4:
            limit = input("Insert a numeric value: ")
<<<<<<< HEAD
            try:
                float(limit)
            except ValueError:
                print("input is not a numeric value")
            system("cls")
            input("press enter to proceed")
=======
>>>>>>> e8790cbcbb20da7741d54b4de075e2878fbc198a
            
            try:
                self.connection.setLimit(float(limit))
            except ValueError:
                print("data must be a number")     
            self.createSheetMenu()
                
        elif chooser == 5:
            self.createTxtMenu()
<<<<<<< HEAD

    def budget(self):
        #does not work yet!!!!!!!
        if connection.overBudget() == True:
            print("you are over your budget") 
        system("cls")          
=======
            
>>>>>>> e8790cbcbb20da7741d54b4de075e2878fbc198a
            






        
        




menu = TextMenu()