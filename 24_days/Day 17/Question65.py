"""Please write assert statements to verify that every number in the list [2,4,6,8] is even."""

def assert_even(li):
    if not isinstance(li,list):
        return "[!] This function only takes list."

    for num in li:
        try:
            assert num%2 == 0, f"{num} is not an even integer."
        except (AssertionError,TypeError):
            return f"[!] {num} is not an even integer. "
    return f"Check complete."

print(assert_even([2,4,'wasim',6]))
print(assert_even([2,4,6,8]))
print(assert_even([2,3,4,5]))