

class TextMenu:
    def __init__(self):
        self.createTxtMenu()
    
    def createTxtMenu(self):
        print("Witaj w menu")
        print("press 1 to establishe a connection with google sheets")
        print("press 2 to quit")
        self.chooser = int(input("Enter a number")) 


menu = TextMenu()