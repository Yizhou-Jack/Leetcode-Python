"""
Largest Divisible Subset
"""

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        resList = [[num] for num in nums]
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(resList[i]) < len(resList[j])+1:
                    resList[i] = resList[j] + [nums[i]]
        return max(resList, key=len)