"""You are given an integer, N. Your task is to print an alphabet rangoli of size N.
 (Rangoli is a form of Indian folk art based on creation of patterns.)"""


def print_rangoli(n):
    for num in range(1, n + 1):
        for alpha in range(1, num + 1):
            print(chr(97 + n - alpha), end='-')
        print()


print_rangoli(5)
