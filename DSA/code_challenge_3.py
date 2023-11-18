# Two sum problem leetcode
# https://leetcode.com/problems/two-sum/


# optimized solution
def twoSum(nums, target):
    hash = {}

    for i in range(len(nums)):
        if nums[i] in hash:
            return [hash[nums[i]], i]
        diff = target - nums[i]
        hash[diff] = i
    return []


# using brute force


def twoSum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
