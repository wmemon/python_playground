"""
Write a program which accepts a string as input to print "Yes" if the string is
"yes" or "YES" or "Yes", otherwise print "No".
"""
# My use case will have some extra yes combinations.

if input("Please enter the string : ").upper() == "YES":
    print("Yes")
else:
    print("No")
