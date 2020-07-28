"""Write a program which accepts a sequence of words separated by whitespace as
input to print the words composed of digits only.

Example: If the following words is given as input to the program:
Input: 2 cats and 3 dogs.
Output: ['2', '3']

Constrains:- Use regex
"""

import re
def get_num(string):
    pattern = re.compile("\d")
    return pattern.findall(string)


