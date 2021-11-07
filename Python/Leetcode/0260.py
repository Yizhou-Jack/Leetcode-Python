"""
Single Number III
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        def checkBit(n, i):
            return (n&(1<<i)) != 0
        def getBitPos(n):
            for i in range(32):
                if checkBit(n, i):
                    return i
        n = len(nums)
        if n == 2:
            return nums
        x = 0
        for i in range(n):
            x ^= nums[i]
        pos = getBitPos(x)
        res1 = 0
        res2 = 0
        for i in range(n):
            if checkBit(nums[i], pos):
                res1 ^= nums[i]
            else:
                res2 ^= nums[i]
        return [res1, res2]