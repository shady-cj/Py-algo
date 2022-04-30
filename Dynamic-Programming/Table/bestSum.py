# Write a function bestSum(targetSum , numbers) that takes in a target sum and an array of numbers as arguments

# The function should return an array containing the shorterst combination of numbers that add up to exactly the targetSum

# If there is a tie for the shortest combination you may return any one of the shortest. 



def bestSum(targetSum, numbers):
    table = [None] * (targetSum +1)
    table[0] = []

    for i in range(0, targetSum+1):
        if (table[i] != None):
            for num in numbers:
                forwardIndex = num + i
                if forwardIndex <= targetSum:
                    newArr = list(table[i])
                    newArr.append(num)
                    if table[forwardIndex]  == None or len(table[forwardIndex]) > len(newArr):
                        table[forwardIndex] = newArr

    return table[targetSum]

print(bestSum(7, [5,3,4,7]))
print(bestSum(7, [2,3]))
print(bestSum(7, [5,3,4,7]))
print(bestSum(7, [2,4]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
print(bestSum(300, [7,14]))
print(bestSum(100, [25,1,2,5]))

# time complexity O(m^2*n) and space of O(m^2) where m = targetSum and n = number of length