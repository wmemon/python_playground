"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.
Input: 5
2 3 6 6 5

Output: 5

"""

def get_runner_up(string):
    set_li = list(set(string.split(' ')))
    set_li.sort(reverse=True)
    return set_li[(set_li.index(max(set_li)))+1]


print(get_runner_up("2 3 6 6 5"))