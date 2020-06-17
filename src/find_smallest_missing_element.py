def find_smallest_missing_element(arr):
    if not arr: return 0

    for i in range(arr[-1]):
        if arr[i] != i:
            return i

    return arr[-1] + 1

print(find_smallest_missing_element([0, 1, 2, 6, 9, 11, 15]))
print(find_smallest_missing_element([1, 2, 3, 4, 6, 9, 11, 15]))
print(find_smallest_missing_element([0, 1, 2, 3, 4, 5, 6]))
print(find_smallest_missing_element([]))