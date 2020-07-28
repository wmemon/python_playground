"""
Define a function that can accept two strings as input and concatenate
them and then print it in console.
"""

concat = lambda x,y : str(x)+str(y)

string1 = input("Please enter string 1: ")
string2 = input("Please enter string 2: ")
print(concat(string1,string2))