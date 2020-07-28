"""
Given a number N.Find Sum of 1 to N Using Recursion
"""

def get_sum(n):
    if n == 0:
        return 0
    else:
        return n+get_sum(n-1)

print(get_sum(5))