"""
Given an array of integers, determine if the array contains a pair
that amounts to a given sum.


return: the pair or [] if not found
clarifications:
- It has to be a pair that amounts to that value (2 numbers)
- There can be negatives
- No repetitive elements i.e given an array of [1, 2, 4] you can't return [4,4]
e.g 
array1 = [2,3,5,2] 
sum = 8
"""

#Brute force
# Time complexity 0(n^2)
def pair_sum(array, sum):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == sum:
                return [array[i], array[j]]
    return []
    
array1 = [2,3,8,2,9,-1] 
sum_value = 8
print(pair_sum(array1, sum_value))


#Better solution

# Time complexity O(n)
# Space complexity O(n)
def pair_sum_hash(array_sum, sum):
    map_set = set([])
    for item in array_sum:
        if item in map_set:
            return [sum-item, item]
        map_set.add(sum-item)
    return []
print(pair_sum_hash(array1, sum_value))
