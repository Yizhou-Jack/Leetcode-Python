"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.
"""

from collections import defaultdict
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        div = k // 2
        remain = k % 2
        boundValue = div if remain == 0 else div + 1
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1

        res = 0
        for key in list(hashMap.keys()):
            if key < boundValue:
                res += min(hashMap[key], hashMap[k - key])
        if remain == 0:
            res += hashMap[div] // 2

        return res