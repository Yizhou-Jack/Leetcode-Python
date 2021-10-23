"""
Find Minimum in Rotated Sorted Array II
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid if nums[mid] != nums[right] else right-1
        return nums[left]