# Write a function "canSum(targetSum, numbers)" that takes in a targetSum and an array of numbers as arguments.
# The function should return a boolean indicating whether or not it is possible to generate the target sum using numbers from the array. 
# You may use an element of the array as many times as need.
# You may also assume that all input numbers are non-negative

def canSum(targetSum, numbers):
    if (targetSum == 0):
        return True

    if targetSum < 0:
        return False
    
    for i in numbers:
        remainder = targetSum - i
        if canSum(remainder, numbers) == True:
            return True
        
    return False

# time complexity O(n^m) and space of O(m) where n = length of array of numbers and m = target sum



# print(canSum( 92,[3,2,95,4]))

# Memoized version
def canSumMemo(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if (targetSum == 0):
        return True

    if targetSum < 0:
        return False
    
    for i in numbers:
        remainder = targetSum - i
        if canSumMemo(remainder, numbers, memo) == True:
            memo[targetSum]=True
            return True
    memo[targetSum] =False  
    return False

print(canSumMemo( 92,[3,2,95,4]))

# time complexity of O(n*m) and space complexity of O(m) where n = length of array of numbers and m = target sum
