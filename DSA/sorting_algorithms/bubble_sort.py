# Implementing bubble sort


# The algorithm entails the largest value in the array to the last (bubbling to the top)


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - 1):
            current = array[j]
            next = array[j + 1]
            if current > next:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


import random

array = [random.randrange(0, 40) for i in range(40)]
print(array)
bubble_sort(array)
print(array)
