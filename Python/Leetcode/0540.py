"""
Single Element in a Sorted Array
"""

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if mid == len(nums)-1 or mid == 0 or (nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]):
                return nums[mid]
            lenN = mid-left+1
            odd = True if lenN%2 == 1 else False
            leftSame = True if nums[mid] == nums[mid-1] else False
            if odd and leftSame:
                right = mid-2
            elif odd and not leftSame:
                left = mid+2
            elif not odd and leftSame:
                left = mid+1
            elif not odd and not leftSame:
                right = mid-1
        return nums[left]