"""
Define a function which can generate a list where the values are square of numbers between 1 and 20
(both included). Then the function needs to print the last 5 elements in the list.
"""

def sq_list__last_five():
    print([x*x for x in range(1,21)][-5:])
    return None

sq_list__last_five()