# Write a function "canSum(targetSum, numbers)" that takes in a targetSum and an array of numbers as arguments.
# The function should return a boolean indicating whether or not it is possible to generate the target sum using numbers from the array. 
# You may use an element of the array as many times as need.
# You may also assume that all input numbers are non-negative

def canSum(targetSum, numbers):
    table = [False] * (targetSum + 1)
    table[0] = True
    for i in range(0, targetSum + 1):
        if table[i] == True:
            for num in numbers:
                nextIndex = i + num
                if nextIndex <= targetSum:
                    table[nextIndex] = True

    return table[targetSum]


print(canSum(7, [2,3]))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7,14]))


# time complexity of O(m * n) and space complexity = O(m)

# Where m = targetSum and n = length of arrays