"""
Define a function that can receive two integer numbers in string
form and compute their sum and then print it in console.
"""

add_func = lambda x,y:(int(x)+int(y))
num1 = input("Please enter num1: ")
num2 = input("Please enter num2: ")
print(f"The result is : {add_func(num1,num2)}")