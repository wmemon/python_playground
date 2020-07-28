"""By using list comprehension, please write a program to print the list after removing the 0th,
 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]"""

li = [12, 24, 35, 70, 88, 120, 155]

li2 = [li[x] for x in range(len(li)) if x % 2 != 0]
print(li2)
