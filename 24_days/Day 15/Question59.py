"""
    Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

    Example: If the following n is given as input to the program:

    5
    Output:
    3.55
"""

def compute_seq(n):
    sum = 0.0
    if not isinstance(n,int):
        return "[!]Please enter a number."
    n = int(n)
    if not n>0 :
        return "[!] n must be strictly greater than zero."

    for num in range(n+1):
        sum += num/(num+1)

    return sum


print(f"{compute_seq(5):.2f}")