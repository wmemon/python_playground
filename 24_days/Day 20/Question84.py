"""By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0."""

three_d = [[[0 for i in range(8)] for j in range(5)] for k in range(3)]
print(three_d)