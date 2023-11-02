# Implementing merge sort


def merge_sort(array):
    length = len(array)
    if length <= 1:
        return array

    mid = length // 2

    # divide array into two
    left = merge_sort(array[0:mid])
    right = merge_sort(array[mid:])

    l_index = 0
    r_index = 0
    new_array = []
    while l_index < len(left) and r_index < len(
        right
    ):  # Combine the two arrays accordingly (Merging)
        if left[l_index] < right[r_index]:
            new_array.append(left[l_index])
            l_index += 1
        else:
            new_array.append(right[r_index])
            r_index += 1

    new_array = new_array + left[l_index:] + right[r_index:]
    return new_array


import random

array = [random.randrange(0, 40) for i in range(40)]
print(array)
print(merge_sort(array))
