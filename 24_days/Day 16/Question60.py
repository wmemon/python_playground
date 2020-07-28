"""
recursive function with following properties
f(n)=f(n-1)+100 when n>0
and f(0)=0

Input: 5
Output: 500
"""

def calc(num):
    if not isinstance(num,int):
        return "[!] Only an integer is expected as a value."
    if num<0:
        return "[!] The provided integer must be greater than zero. "

    if num == 0:
        return 0

    return calc(num-1)+100


print(calc(5))