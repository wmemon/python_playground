"""By using list comprehension,
 please write a program to print the list after removing
 the value 24 in [12,24,35,24,88,120,155]."""

li = [12,24,35,24,88,120,155]
print([num for num in li if num!=24])