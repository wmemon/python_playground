"""Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print
 "Male" for Male class and "Female" for Female class."""

class Person:
    pass

class Male(Person):

    def getGender(self):
        print("Male")

class Female(Person):

    def getGender(self):
        print("Female")


m1 = Male()
m1.getGender()

f1 = Female()
f1.getGender()
