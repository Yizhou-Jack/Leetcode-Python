"""
Arithmetic Slices II - Subsequence
"""
from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        f = [defaultdict(int) for _ in nums]
        for i, numsi in enumerate(nums):
            for j in range(i):
                d = numsi - nums[j]
                count = f[j][d]
                res += count
                f[i][d] += count + 1
        return res