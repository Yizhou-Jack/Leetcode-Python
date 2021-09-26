"""
Maximum Difference Between Increasing Elements
"""
from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    res = max(res, nums[j]-nums[i])
        return res