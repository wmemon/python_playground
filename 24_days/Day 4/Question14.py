"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Input:- Hello world!
Output:-
UPPER CASE 1
LOWER CASE 9
"""

def count_letter_case(string):
    upper = 0
    lower = 0
    if not isinstance(string,str):
        return "The input must be a string."
    else:
        for char in string:
            if char.isupper():
                upper+=1
            elif char.islower():
                lower+=1
    print(f"UPPER CASE {upper}")
    print(f"LOWER CASE {lower}")

    return None

count_letter_case('Hello world!')