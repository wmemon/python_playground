"""Please write a program using generator to print the numbers which can be divisible by 5 and 7
between 0 and n in comma separated form while n is input by console."""


def five_n_seven(n):
    num = 0
    while n>=num:
        if num%5 == 0 and num%7==0:
            yield num
        num+=1

answer = []
for i in five_n_seven(100):
    answer.append(str(i))

print(','.join(answer))