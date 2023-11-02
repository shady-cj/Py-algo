# insertion sort implement

# the algorithm involves comparing a number with its previous one and the concurrently swapping until it's in the right position it's meant to be


def insertion_sort(array):
    length = len(array)

    for i in range(1, length):
        j = i
        while j >= 1:
            current = array[j]
            prev = array[j - 1]
            if current < prev:
                array[j], array[j - 1] = array[j - 1], array[j]  # swap
                j -= 1
            else:
                break

    return array


import random

array = [random.randrange(0, 40) for i in range(40)]
print(array)
insertion_sort(array)
print(array)
