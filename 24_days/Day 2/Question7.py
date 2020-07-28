"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i * j.
Input:- 3,5
Output :- [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""


def get_arr(rows, columns):
    result_arr = []
    for row in range(rows):
        column_arr = []
        for column in range(columns):
            column_arr.append(row * column)
        result_arr.append(column_arr)
    return result_arr


print(get_arr(3, 5))
# We could also have used list comprehension.
