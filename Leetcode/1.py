# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.





# using brute force worst case scenario will have a time complexity of O(2n) space of O(1)

def sum(nums, target):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
    return "not found"


    


# def optimized_sum(nums, target):

#     for i in range(len(nums)):
#         find_data= target - nums[i]
#         try:
#             id = nums.index(find_data)
#             if i != id:
#                 return [i, id]
#         except:
#             continue

#     return -1

# using recursion and dynamic programming

def brute_sum(nums, target):
    if target == 0:
        return []
 

    for idx in range(len(nums)):
        if nums[idx] == None:
            continue
        rem = target - nums[idx]
        new_arr = list(nums)
        new_arr[idx] = None 

        remArr =  brute_sum(new_arr, rem)
       
        
        if remArr != None:
            remArr.insert(0,idx)
            return remArr
        
    return None

# print(brute_sum([2,7,11,15], 9))
# print(brute_sum([3,2,95,4,-3], 92))
# print(brute_sum( [1,2,3,5,6,7] ,3))
# print(brute_sum( [3,2,4] ,6))
print(brute_sum([4,4,3,1], 4))
# memoized version


# def optimized_sum(nums, target, memo={}):
#     hashId = target, tuple(nums)
#     if hashId in memo:
#         return memo[hashId]
#     if target == 0:
#         return []
 

#     for idx in range(len(nums)):
#         if nums[idx] == None:
#             continue
#         rem = target - nums[idx]
#         new_arr = list(nums)
#         new_arr[idx] = None 
#         remArr =  brute_sum(new_arr, rem)
#         if remArr != None:
#             remArr.insert(0,idx)
#             memo[hashId] = remArr
#             return memo[hashId]
#     memo[hashId] = None
#     return memo[hashId]
    

# [1,2,3,5,6,7] #3
# [3,2,95,4,-3]
# print(optimized_sum([3,2,95,4,-3], 92))


# print(brute_sum(a, 999))