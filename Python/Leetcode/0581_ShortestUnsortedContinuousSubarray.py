"""
Given an integer array nums,
you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order.
Return the shortest such subarray and output its length.
"""

from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        left = 0
        right = n - 1
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        if left > right:
            return 0

        intervalMin = min(nums[left:right + 1])
        intervalMax = max(nums[left:right + 1])
        while left > 0 and nums[left - 1] > intervalMin:
            left -= 1
        while right < n - 1 and nums[right + 1] < intervalMax:
            right += 1

        return right - left + 1