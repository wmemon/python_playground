"""
With a given tuple (1,2,3,4,5,6,7,8,9,10),
write a program to print the first half values in one line and the last half values in one line.
"""

def print_tup(tup):
    if not isinstance(tup,tuple):
        return "[!]Please enter tuple to print."

    print(tup[:int(len(tup)/2)])
    print(tup[int(len(tup)/2):int(len(tup))])
    return None

print_tup((1,5,7,9,23,45,67,2))