"""
Sort Array By Parity II
"""
from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        n = len(nums)
        while i < n and j < n:
            while i < n and (i%2 == 1 or (i%2 == 0 and nums[i]%2 == 0)):
                i += 1
            while j < n and (j%2 == 0 or (j%2 == 1 and nums[j]%2 == 1)):
                j += 1
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return nums