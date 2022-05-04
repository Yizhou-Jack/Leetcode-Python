from typing import List

class Solution:
    def arraySign1(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            if nums[i] < 0:
                res *= -1
        return res

    def arraySign2(self, nums: List[int]) -> int:
        sign = False
        for x in nums:
            if x == 0:
                return 0
            sign = sign ^ (x < 0)
        return -1 if sign else 1