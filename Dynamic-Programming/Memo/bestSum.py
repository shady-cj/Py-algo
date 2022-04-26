# Write a function bestSum(targetSum , numbers) that takes in a target sum and an array of numbers as arguments

# The function should return an array containing the shorterst combination of numbers that add up to exactly the targetSum

# If there is a tie for the shortest combination you may return any one of the shortest. 

def bestSum(targetSum, numbers):
    if (targetSum == 0):
        return []
    if (targetSum < 0):
        return None
    
    shortest_combination = None

    for num in numbers:
        rem = targetSum - num
        rem_combination =  bestSum(rem, numbers)
        if rem_combination != None:
            combination = list(rem_combination)
            combination.insert(0, num)
            if (shortest_combination == None or len(combination) < len(shortest_combination)):
                # print(shortest_combination, rem_combination)
                shortest_combination = combination

    return shortest_combination        


# print(bestSum(7, [5,3,4,7]))
# print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
# print(bestSum(100, [1,2,5,25]))

# brute force time complexity O(n^m * m) and space O(m * m) where n = length of numbers and m = targetSum


def bestSumMemo(targetSum, numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if (targetSum == 0):
        return []
    if (targetSum < 0):
        return None
    
    shortest_combination = None

    for num in numbers:
        rem = targetSum - num
        rem_combination =  bestSumMemo(rem, numbers,memo)
        if rem_combination != None:
            combination = list(rem_combination)
            combination.insert(0, num)
            if (shortest_combination == None or len(combination) < len(shortest_combination)):
                # print(shortest_combination, rem_combination)
                shortest_combination = combination

    memo[targetSum] = shortest_combination
    return memo[targetSum]


# time: O(n*m^2) space: O(m^2) and space O(m * m) where n = length of numbers and m = targetSum



# print(bestSumMemo(8, [2,3,5]))
print(bestSumMemo(8, [1,4,5]))
print(bestSumMemo(100, [1,2,5,25]))
# print(bestSumMemo(30, [1,4,5]))

# print(bestSumMemo(7, [5,3,4,7]))