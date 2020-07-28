"""
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.

"""


def string_max(*args):
    for string in args:
        if not isinstance(string, str):
            return "[!]Please enter a string. "

    return (sorted(args, key=len, reverse=True))


print(string_max("Wasimmemon", "wasim", "whate"))
