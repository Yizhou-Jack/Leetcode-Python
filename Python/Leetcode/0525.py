"""
Contiguous Array
Prefix-sum with Hashmap
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hm = {0:-1}
        count = 0
        res = 0
        for i, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1
            if count in hm:
                res = max(res, i-hm[count])
            else:
                hm[count] = i
        return res