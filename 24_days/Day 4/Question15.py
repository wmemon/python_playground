"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Input:- 9
Output:- 11106
"""


def calculate_a(num):
    if not isinstance(num, int):
        return "[!]The given number must be an integer."

    sum = 0

    for i in range(1, 5):
        sum += int(str(num) * i)
    return sum

print(f"Answer is :- {calculate_a(9)}")
