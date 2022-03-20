# Insertion sort
# Insertion sort is similar to the sort2 function in bubbleSort.py they both have the same time complexity O(N^2) in the worst case and O(N) in the best where as in this the space complexity is O(1) which gives this a edge over the sort2 function whose space complexity is O(N)
def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums            

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)
# print(insertion_sort(in_list))

[1,2,4,5,6,7]

