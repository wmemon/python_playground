"""
You are given a string.Your task is to
count the frequency of letters of the string and print the letters in descending order of frequency.

Input: aabbbccde

"""

from collections import Counter

string = input("Please enter a string: ")
for k,v in Counter(string).items():
    print(k,v)