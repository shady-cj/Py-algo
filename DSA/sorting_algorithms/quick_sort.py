# Implementing quick sort


# They are of 2 types Hoare partition scheme, and Lomuto partition sheme


# The general solution also known as the Lomuto Partition scheme


# [4, 2, 3, 1]
# Taking 1 as the pivot
# iterating through the array starting at index 0
# at index 0 value is 4
# is 4 greater 1 ? yes so it needs to be towards the right of 1(pivot)
# then we look for the nearest neighbor to the left of 1 which is 3,
# then swap 3 with 1 now we have [4, 2, 1, 3], now our pivot (1) is at index 2
# then we swap 4 with 3 making sure that 4 is towards the right of the 1 (pivot) now we have [3, 2, 1, 4]
# we don't move our pointer from index 0 yet, we check again since is greater 1 (pivot) then we look at the nearest neighbor to the left 1, and swap then
#  after swapping we now have [3, 1, 2, 4] then we swap the pointer at 3 with 2 thus having [2, 1, 3, 4]
# still having the pointer at index 0 we compare 2 and 1 (pivot) still greater 1 then we need to swap with its nearest neighbor but this time we need to be careful with the swapping
# because if we swap using the nearest neighbor method we might have issues let's try this and seel
# swap with nearest neighbor to the left of 1 we have [1, 2, 3, 4] but then we want to swap again with the value at index 1(we will have [2, 1, 3, 4]) so instead we swap once if the nearest neighbor index is same as the pointer index we just swap once
# Thus we have [1, 2, 3, 4], now 1 is where it is supposed to be in the array
# In our case we have a sorted array after first iteration, it might not always be like that, so basically we divide the array into subproblems, by recalling the algorithm above on what's to the left of the pivot and to the right of the pivot by using the same approach(picking a pivot and swapping elements based on pivot)


def quick_sort(start, end, array):
    if start >= end:
        return None
    pivot = end
    i = start

    while i < pivot:
        current_value = array[i]
        pivot_value = array[pivot]
        if current_value > pivot_value:
            left_neighbor = pivot - 1
            array[pivot], array[left_neighbor] = array[left_neighbor], array[pivot]
            if left_neighbor != i:
                array[i], array[pivot] = array[pivot], array[i]
            pivot = left_neighbor
        else:
            i += 1
    quick_sort(start, pivot - 1, array)
    quick_sort(pivot + 1, end, array)
    return None


import random

array = [random.randrange(0, 40) for i in range(400)]
print(array)
quick_sort(0, len(array) - 1, array)
print(array)
