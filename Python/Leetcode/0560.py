"""
Subarray Sum Equals K
"""

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1
        res = 0
        tempSum = 0
        for num in nums:
            tempSum += num
            res += hm[tempSum-k]
            hm[tempSum] += 1
        return res