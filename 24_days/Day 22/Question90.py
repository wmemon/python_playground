"""


    Please write a program which count and print the numbers of each character in a string input by console.

    Example: If the following string is given as input to the program:

"""
from collections import Counter
string_list = list(input("Please enter a string: "))
for k,v in dict(Counter(string_list)).items():
    print(f'{k} : {v}')