"""
154: Find Minimum in Rotated Sorted Array II
"""
from typing import List

class Solution:
    """
    If no duplicates.
    """
    def findMin1(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]
    """
    If contains duplicates.
    """
    def findMin2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid if nums[mid] != nums[right] else right-1
        return nums[left]