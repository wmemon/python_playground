"""
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that
is an integral number between 1 and n (both included).
and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
"""


def create_dict(num):
    num = int(num)
    if not isinstance(num, int):
        return "Only integers are allowed"
    return {x: x * x for x in range(num + 1)}

inp_num = input("Please enter a number :- ")
print(create_dict(inp_num))