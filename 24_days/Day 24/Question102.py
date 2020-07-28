"""Write a Python program that accepts a string and calculate the number of digits and letters."""

def get_digits(string):
    digits = 0
    for alpha in string:
        if alpha.isdecimal():
            digits+=1
    return digits

def get_letters(string):
    letters = 0
    for alpha in string:
        if alpha.isalpha():
            letters+=1
    return letters

string = input("Please enter a string: ")
print(f"Digits: {get_digits(string)}")
print(f"Letters: {get_letters(string)}")