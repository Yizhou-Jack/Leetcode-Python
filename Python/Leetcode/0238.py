"""
Product of Array Except Self
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = 1
        res = []
        for i in range(n):
            res.append(temp)
            temp *= nums[i]
        temp = 1
        for i in range(n-1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res