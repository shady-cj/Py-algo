# write a function howSum(targetSum, numbers) that takes in a targetsum and an array of numbers as arguments .
# The function should return an array containing any combination of elements that add up exactly the targetSum. if there is no combination that adds up to the targetSum, then return null
# if there are multiple combinations possibe, you may return any single one

def howSum(targetSum, numbers):
    if (targetSum == 0 ):
        return []
    if (targetSum < 0):
        return None
    
    for num in numbers:
        rem = targetSum - num
        rem_result = howSum(rem, numbers)
        if rem_result != None:
            rem_result.append(num)
            return rem_result
    return None
    
    
# Time complexity of O(n^m * m) n = length of array , m = target sum , space O(m)

# print(howSum(92,[3,2,95,4,-3]))
# print(howSum(7,[2,3,3]))
# print(howSum(300,[7,14]))

# Memoized version



def howSumMemo(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum] 

    if (targetSum == 0 ):
        return []
    if (targetSum < 0):
        return None
    
    for num in numbers:
        rem = targetSum - num
        rem_result = howSumMemo(rem, numbers, memo)
        if rem_result != None:
            rem_result.append(num)
            memo[targetSum] = rem_result
            return memo[targetSum]

    memo[targetSum] = None
    return None
    
print(howSumMemo(0,[7,14,0,0]))

# Time complexity O(n*m^2) space O(m^2)  n = length of array , m = target sum 
# print(howSum(999, a))