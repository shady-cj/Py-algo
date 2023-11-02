# selection sort implementation
# The algorithm entails iterating through and array and selecting the smallest and forming an array up till its sorted


def selection_sort(array):
    length = len(array)
    for i in range(length):
        smallest_index = i
        for j in range(i, length):
            # print(j)
            current_value = array[j]
            current_smallest_value = array[smallest_index]
            if current_value < current_smallest_value:
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]

    return array


import random

array = [random.randrange(0, 40) for i in range(40)]
print(array)
selection_sort(array)
print(array)
