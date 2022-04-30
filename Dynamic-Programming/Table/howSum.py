# write a function howSum(targetSum, numbers) that takes in a targetsum and an array of numbers as arguments .
# The function should return an array containing any combination of elements that add up exactly the targetSum. if there is no combination that adds up to the targetSum, then return null
# if there are multiple combinations possibe, you may return any single one

def howSum(targetSum , numbers):
    table = [None] * (targetSum+1)
    table[0] = []

    for i in range(0, targetSum+1):
        if table[i] != None:

            for num in numbers:
                nextIndex = i + num
                if nextIndex <= targetSum:
                    newArr = list(table[i])
                    newArr.append(num)
                    table[nextIndex] = newArr
    return table[targetSum]


print(howSum(7, [2,3]))
print(howSum(7, [5,3,4,7]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
print(howSum(300, [7,14]))


# Time complexity of O(m^2*n) and space complexity O(m^2)