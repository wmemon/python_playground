"""Please write a binary search function which searches an item in a sorted list.
 The function should return the index of element to be searched in the list."""


def binary_search(li, key):
    if not isinstance(li, list):
        return f"[!] The function requires a list to operate. "
    start = 0
    end = len(li) - 1
    mid = (start + end) // 2

    while (start <= end):
        if key < li[mid]:
            end = mid - 1
            mid = (start + end) // 2

        elif key > li[mid]:
            start = mid + 1
            mid = (start + end) // 2


        elif key == li[mid]:
            return f"Key found at index {mid}"

    return f"Key not found."

li=[2,5,7,9,11,17,222]

print(binary_search(li,11))
print(binary_search(li,12))