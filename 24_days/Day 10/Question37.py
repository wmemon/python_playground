"""
Define a function which can generate and print a tuple where the value are square of numbers
between 1 and 20 (both included).
"""

def sq_tuple():
    print(tuple([x*x for x in range(1,21)]))
    return None

sq_tuple()