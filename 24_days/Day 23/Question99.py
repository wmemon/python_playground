"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""

def get_symmetric_difference(string_a,string_b):
    set_a = set(string_a.split(' '))
    set_b = set(string_b.split(' '))
    result_list = sorted([int(x) for x in list(set.symmetric_difference(set_a,set_b))])
    for num in result_list:
        print(num)




get_symmetric_difference('2 4 5 9','2 4 11 12')