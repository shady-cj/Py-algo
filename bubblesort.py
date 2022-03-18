# Program for perform bubble sort 

def sort(nums):
    # Duplicate the list to avoid direct altering of the input list
    nums = list(nums)

    # Iterating n-1 times to ensure thorough sorting through the list 
    for _ in range(len(nums)-1):
        # Iterating through the main list n-1 times to ensure there will be a i+1 data in the list to compare
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1] , nums[i]
    
    return nums



# Not bubble sort, similar to insertion sort but an improved approach where as in the worst case scenario isn't better than bubble sort since the time complexity will be O(N^2) in the worst case and space complexity of O(N) but in the best case time complexity is 0(N)
def sort2(nums):
    # Duplicate the list to avoid direct altering of the input list
    nums = list(nums)
    new_nums = []

    for i in range(len(nums)):
        if i==0:
            new_nums.append(nums[i])
        else:
    
            k = len(new_nums)-1 
            while k >=0 :
                if nums[i] <= new_nums[k]:
                    if k==0:
                        new_nums.insert(k,nums[i])
                        break
                    k -= 1
                else:
                    new_nums.insert(k+1, nums[i])

                    break

    return new_nums

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)


# print(sort2(in_list))  # 3.49 seconds


# print(out_list==sort(in_list))


# print(sort(in_list))  # 12.6 seconds


# It took 12 secs to run this program which is prolly inefficient