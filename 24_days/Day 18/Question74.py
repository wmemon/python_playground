"""
Please write a program to randomly generate a list with 5 numbers,
which are divisible by 5 and 7 , between 1 and 1000 inclusive.
"""

from random import sample

def gen_func(n1,n2):
    for num in range(n1,n2):
        if (num%5==0 and num%7==0):
            yield num

print(sample([i for i in range(1,1001) if (i%5==0 and i%7==0)],5))
print(sample(list(gen_func(1,1001)),5))