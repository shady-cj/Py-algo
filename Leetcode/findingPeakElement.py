"""
162. Find Peak Element
Medium
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.



Example:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""

class Solution:
    def findPeakRecursive(self, nums, lo, hi):
        mid = (lo + hi) // 2    
        left = mid - 1
        right = mid + 1
    
        if left < 0 and nums[mid] >= nums[right]:
            return mid
        elif right >= len(nums) and nums[mid] >= nums[left]:
            return mid
        elif nums[mid] >= nums[left] and nums[mid] >= nums[right]:
            return mid
        if lo == hi:
            return None
        searchLeft = self.findPeakRecursive(nums, lo, mid)
        searchRight = self.findPeakRecursive(nums, mid + 1, hi)
        if searchLeft is None:
            return searchRight
        return searchLeft
    
    
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.findPeakRecursive(nums, 0, len(nums) - 1)
        
