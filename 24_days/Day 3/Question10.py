"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after
removing all duplicate words and sorting them alphanumerically.

Input:- hello world and practice makes perfect and hello world again
Output:- again and hello makes perfect practice world
"""

print(' '.join(sorted(list(set(input("Please Enter a string:- ").split(' '))))))
