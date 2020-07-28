"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Input:- hello world! 123
Output:- LETTERS 10
         DIGITS 3
"""

letters = 0
digits = 0
for character in input("Please enter the string:- "):
    try:
        int(character)
        digits+=1
    except ValueError:
        letters+=1

print(f"LETTERS {letters}")
print(f"DIGITS {digits}")