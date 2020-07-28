"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320

"""


def factorial(num):
    if num == 0:
        return 1
    mul = 1
    while num > 0:
        mul = num * mul
        num -= 1
    return (mul)


def fact_short(num: int) -> int: return 1 if num <= 1 else num * fact_short(num - 1)


print(fact_short(8))
