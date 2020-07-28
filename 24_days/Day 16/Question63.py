"""
    Please write a program using generator to print the even numbers between
    0 and n in comma separated form while n is input by console.
    Example: If the following n is given as input to the program:
    10
    Output:
    0,2,4,6,8,10

"""

def even_num(n):
    num = 0
    while n>=num:
        if num%2 == 0:
            yield num
        num+=1

answer = []
for i in even_num(10):
    answer.append(str(i))

print(','.join(answer))