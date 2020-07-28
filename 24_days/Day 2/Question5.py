class UpperString:
    def __init__(self):
        pass

    def getString(self):
        string = input("Please enter a string:- ")
        self.string = string
        return None

    def printString(self):
        print(self.string.upper())
        return None

UpperString_new = UpperString()
UpperString_new.getString()
UpperString_new.printString()
