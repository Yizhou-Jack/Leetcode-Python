"""
Maximum Product Sub-array
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        n = len(nums)
        res = float("-inf")
        for i in range(n):
            vals = (nums[i], nums[i]*currMax, nums[i]*currMin)
            currMax = max(vals)
            currMin = min(vals)
            res = max(res, currMax)
        return res