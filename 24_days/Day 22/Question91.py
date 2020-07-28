"""


    Please write a program which accepts a string from console and print it in reverse order.

    Example: If the following string is given as input to the program:*
    rise to vote sir

    Output: ris etov ot esir

"""

string_list = list(input("Please enter a string: "))
string_list.reverse()
print(''.join(string_list))
