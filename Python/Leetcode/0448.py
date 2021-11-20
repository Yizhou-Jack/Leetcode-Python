"""
Find All Numbers Disappeared in an Array
"""

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res