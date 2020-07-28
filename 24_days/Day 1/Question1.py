# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between a and b  (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def seven_not_five(a, b):
    a = int ( a )
    b = int ( b )
    for num in range ( a, b + 1 ):
        if num % 7 == 0 and num % 5 != 0:
            print ( num, end="," )
    print ( "\b" )


seven_not_five ( 2000, 3200 )
