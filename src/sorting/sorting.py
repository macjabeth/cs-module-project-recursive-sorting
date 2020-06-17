# TO-DO: complete the helper function below to merge 2 sorted arrays
# [5], [3] = [5, 3]
def merge(left_array, right_array):
    left_len, right_len = len(left_array), len(right_array)
    elements = left_len + right_len
    merged_arr = [0] * elements
    # merged_arr = [0 for i in range(elements)]
    left_index = right_index = 0

    # current_index = 0
    # while left_index < left_len and right_index < right_len:
    #     if left_array[left_index] < right_array[right_index]:
    #         merged_arr[current_index] = left_array[left_index]
    #         left_index += 1
    #     else:
    #         merged_arr[current_index] = right_array[right_index]
    #         right_index += 1
    #     current_index += 1
    
    # for idx in range(left_index, left_len):
    #     merged_arr[current_index] = left_array[idx]
    #     current_index += 1
    
    # for idx in range(right_index, right_len):
    #     merged_arr[current_index] = right_array[idx]
    #     current_index += 1

    for i in range(elements):
        if left_index == left_len:
            merged_arr[i] = right_array[right_index]
            right_index += 1
        elif right_index == right_len:
            merged_arr[i] = left_array[left_index]
            left_index += 1
        elif left_array[left_index] < right_array[right_index]:
            merged_arr[i] = left_array[left_index]
            left_index += 1
        else:
            merged_arr[i] = right_array[right_index]
            right_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1: return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    if len(arr) <= 1: return arr
    
    mid = l + (r - l) // 2

    merge_sort_in_place(arr, l, mid)
    merge_sort_in_place(arr, mid + 1, r)

    merge_in_place(arr, l, mid, r)