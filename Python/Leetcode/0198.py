"""
House Robber
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        dp_0 = nums[0]
        dp_1 = max(nums[0], nums[1])
        for i in range(2, n):
            temp = dp_1
            dp_1 = max(dp_1, dp_0+nums[i])
            dp_0 = temp
        return dp_1