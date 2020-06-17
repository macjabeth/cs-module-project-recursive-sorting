# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end: return -1
    middle = start + (start - end) // 2 # avoid overflow
    value = arr[middle]
    if target == value:
        return middle
    elif target < value:
        return binary_search(arr, target, start, middle - 1)
    else:
        return binary_search(arr, target, middle + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # is the array sorted in descending or ascending order?
    isAscending = arr[0] < arr[-1]
    start, end = 0, len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        value = arr[middle]
        if target == value:
            return middle
        elif target < value:
            if isAscending:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if isAscending:
                start = middle + 1
            else:
                end = middle - 1
    return -1