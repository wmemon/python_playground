"""
Define a function which can print a dictionary where the keys are numbers between 1 and 20
(both included) and the values are square of keys.

"""

def sq_dict():
    print({x:x*x for x in range(1,21)})
    return None

sq_dict()