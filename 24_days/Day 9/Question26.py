"""
Define a function which can compute the sum of two numbers.
Hint:- Define a function with two numbers as arguments.
You can compute the sum in the function and return the value.
"""

def add(*args):
    """
    Take any number of values and add it together to return the result.
    :param args: int or float list
    :return: int or float
    """
    for num in args:
        if not (isinstance(num,int) or isinstance(num,float)):
            return "Only integers can be added. "
        if (num == " " or not num):
            return "Only integers can be added. "

    return sum(args)


print(add(1,2,3,4,5,6,7,8,9))
print(add(None,1,2,3))