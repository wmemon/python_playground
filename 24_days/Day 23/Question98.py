"""
You are given a date. Your task is to find what the day is on that date.
Input: 08 05 2015
Output: FRIDAY
"""


def get_day_from_date(string):
    day_diction = {1: 'MONDAY', 2: 'TUESDAY', 3: 'WEDNESDAY', 4: 'THURSDAY', 5: 'FRIDAY', 6: 'SATURDAY', 0: 'SUNDAY'}
    li = string.split(' ')
    k = int(li[0])
    m = (int(li[1]) - 2)
    D = int(li[2][2:])
    C = int(li[2][:2])
    if m <= 0:
        m = 12 + m
        D = D - 1
    F = k + ((13 * m - 1) // 5) + D + (D // 4) + (C // 4) - 2 * C
    print(k, m, D, C)

    return f"The day is {day_diction.get(F % 7)}"


def get_day_key_value(string):
    day_diction = {1: 'SUNDAY', 2: 'MONDAY', 3: 'TUESDAY', 4: 'WEDNESDAY', 5: 'THURSDAY', 6: 'FRIDAY', 0: 'SATURDAY'}
    month_dict = {1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5, 7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6}
    century_dict = {17: 4, 18: 2, 19: 0, 20: 6}
    li = string.split(' ')
    year = int(li[2])
    year_first_two = int(li[2][:2])
    year_last_two = int(li[2][2:])
    day_of_month = int(li[0])
    month = int(li[1])
    result = year_last_two // 4
    result = result + day_of_month
    result = result + month_dict.get(month)
    if ((month == 1 or month == 2) and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)):
        result = result - 1

    result = result + century_dict.get(year_first_two)
    result = result + year_last_two

    return day_diction.get(result%7)

print(get_day_key_value('08 05 2015'))