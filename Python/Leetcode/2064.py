"""
Minimized Maximum of Products Distributed to Any Store
"""
from math import ceil
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = sum(quantities)
        while left < right:
            mid = (left+right)//2
            storeNum = 0
            for i in range(len(quantities)):
                storeNum += ceil(quantities[i]/mid)
            if storeNum > n:
                left = mid+1
            else:
                right = mid
        return left