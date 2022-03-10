"""
Arithmetic Slices
"""

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        i = 0
        count = 0
        while i < len(nums)-2:
            if nums[i]-nums[i+1] == nums[i+1]-nums[i+2]:
                count += 1
                i += 1
                continue
            res += (1+count)*count/2
            count = 0
            i += 1
        res += (1+count)*count/2
        return int(res)