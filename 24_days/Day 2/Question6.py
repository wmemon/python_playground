"""
Q = Square root of [(2 * C * D)/H]
C is 50. H is 30
D Input:- 100,150,180
Output:- 18,22,24

"""

import math

#Using map
print(','.join(map(lambda x:(str(int(math.sqrt((2*50*x)/30)))), [int(i) for i in input("Enter comma separated values:- ").split(',')])))

