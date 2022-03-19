# Defining the merge_sort function
# This is an approach to sorting an array/list
def merge_sort(nums):
    
    # Checking if the length of the array is 1 or 0
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2


    # Dividing the array into 2 parts recursively
    first_arr =merge_sort(nums[:mid])
    second_arr = merge_sort(nums[mid:])

    # Then merging both arrays into a sorted array
    sorted_arr = merge(first_arr, second_arr)

    return sorted_arr

# Defining the merge function to merge each arrays accordingly

def merge(first_arr, second_arr):
    merged = []

    i = 0 
    j = 0 

    while i < len(first_arr) and j < len(second_arr):
        if first_arr[i] <= second_arr[j]:
            merged.append(first_arr[i])
            i+=1
        elif second_arr[j] <= first_arr[i]:
            merged.append(second_arr[j])
            j+=1

    merged = merged + first_arr[i:] + second_arr[j:]

    return merged



# print(merge_sort([3,6,3,56,7,4,3,34,25,2,5,5,3,6]))
import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)
print(merge_sort(in_list) == out_list)


# The time complexity of the merge_sort operation is O(N log N) due to the fact the there n number of array splitting required of the merge_sort function to be able to sort i.e we split the first array into two and then go on to split the subparts recursively until there are single entities in the array. While the time complexity of the merge function is of the order log N While the space complexity of the merge sort function is O(N) 