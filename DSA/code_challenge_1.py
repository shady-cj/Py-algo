"""
Question:

Given 2 arrays write a function that returns True/False whether the arrays
contains common items

e.g
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']

return: False

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']

return True
"""


# First solution (using brute force) 
# time complexity O(n^2)

def contains_common_item(array1, array2):
    for item_1 in array1:
        for item_2 in array2:
            if item_1 == item_2:
                return True
    return False

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'a']

print(contains_common_item(array1, array2))


# Better solution using hash map, you could use sets or dictionaries

# Time complexity O(n) 
# Space complexity O(n) could be a problem if memory is limited
def contains_common_item_hash(array1, array2):
    memo = set([]) # or you could use a dictionary {}

    for i in array1:
        memo.add(i)
    for j in array2:
        if j in memo: # constant time 0(1) worst case 0(n) you could use dictioinaries too
            return True
    return False

print(contains_common_item_hash(array1, array2))