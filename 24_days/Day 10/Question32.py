"""
Define a function which can generate a dictionary where the keys are numbers between 1 and 20
(both included) and the values are square of keys. The function should just print the keys only.
"""

def sq_dict_keys():
    print({x:x*x for x in range(1,21)}.keys())
    return None

sq_dict_keys()