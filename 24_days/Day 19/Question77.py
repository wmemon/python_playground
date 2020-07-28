"""Please write a program to print the running time of execution of "1+1" for 100 times."""

from timeit import timeit

print(timeit("1+1",number=100))

