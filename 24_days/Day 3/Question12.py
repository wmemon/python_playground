"""
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


# Using functions

def check_str_even(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if int(str_num[i]) % 2 == 0:
            pass
        else:
            return False

    return num


def main():
    for i in range(1000, 3001):
        res = check_str_even(i)
        if res:
            print(res, end=" ")


if __name__ == "__main__":
    main()