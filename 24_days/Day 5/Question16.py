"""
Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.

Input:- 1,2,3,4,5,6,7,8,9
Output :- 1,9,25,49,81
"""

print(','.join
      (map(lambda x: str(x * x),
           (list(filter(lambda x: x % 2 == 1,
                        [int(i) for i in input("Please enter comma separated values:- ").split(',')]
                        )))
           ))
      )
