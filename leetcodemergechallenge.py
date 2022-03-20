# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
def merge(nums1, nums2):
    i, j, merged = 0,0,[]
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
    return merged+nums1[i:]+nums2[j:]


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_list = merge(nums1, nums2)
#         check if length of list is odd or even

        if len(merged_list) % 2 == 0:
            mid1 = int(len(merged_list)/2)
            print(mid1)
            mid2 = mid1 - 1
            median = (merged_list[mid1] + merged_list[mid2])/ 2
            return median
        import math
        median =merged_list[math.floor(len(merged_list)/2)]
        return median
            
nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))