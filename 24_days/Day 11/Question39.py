"""
Write a program to generate and print another tuple whose values are
even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""

print(tuple(filter(lambda x:int(x)%2==0,input("Please enter integers in csv format : ").split(','))))