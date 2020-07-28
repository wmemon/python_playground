"""
Write a program to compute the frequency of the words from the input.
 The output should output after sorting the key alphanumerically.

Input : New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Output:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
#Use pprint to display dictionaries already sorted.

from collections import Counter


li = input("Please enter the string:- ").split(' ')
li =(sorted(Counter(li).items()))

for tup in li:
    print(f"{tup[0]}:{tup[1]}")