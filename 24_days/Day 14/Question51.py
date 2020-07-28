"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def divide_by_zero_func():
    try:
        5/0
    except ZeroDivisionError:
        print("Can not divide by zero. ")
    except :
        print("Any other error.")

divide_by_zero_func()