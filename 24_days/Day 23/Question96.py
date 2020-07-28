"""
    You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

    If the following string is given as input to the program:

    Input: ABCDEFGHIJKLIMNOQRSTUVWXYZ
            4

    Output:
            ABCD
            EFGH
            IJKL
            IMNO
            QRST
            UVWX
            YZ
"""

import textwrap
def self_made_wrap(S,W):
    return(textwrap.wrap(S,W))

print('\n'.join(self_made_wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4)))