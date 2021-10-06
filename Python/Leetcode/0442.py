"""
Find All Duplicates in an Array
"""
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums: return []
        res = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num-1] < 0:
                res.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return res