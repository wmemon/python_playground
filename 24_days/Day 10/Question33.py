"""
Define a function which can generate and print a list where the values are square of numbers
between 1 and 20 (both included).
"""

def sq_list():
    print([x*x for x in range(1,21)])
    return None

sq_list()