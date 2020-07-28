"""
You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with
the input order of appearance of the word.

4
bcdef
abcdefg
bcde
bcdef
"""

from collections import Counter
n = int(input("Please enter the number of inputs: "))
li=[]
for num in range(n):
    li.append(input(f"Please enter string {num+1}: "))

print(list(dict(Counter(li)).values()))