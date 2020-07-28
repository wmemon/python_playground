"""
Define a function that can convert a integer into a string and print it in console.
Hint: Use str() to convert a number to string.
"""

# I will try to use a lambda function here

to_str = lambda x:str(x)
num = int(input("Please enter an integer:- "))
print(f"On converting to string the number would be {to_str(num)}")
print(f"Proof: {type(to_str(num))}")