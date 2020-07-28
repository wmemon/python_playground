"""
Fibonacci sequence:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Input: 7
Output: 13
"""

def fib_recur(num):
    if not isinstance(num,int):
        return "[!] Only an integer is expected as a value."
    if num<0:
        return "[!] The provided integer must be greater than zero. "

    if num<2:
        return num

    return fib_recur(num-1)+fib_recur(num-2)

print(fib_recur(7))
