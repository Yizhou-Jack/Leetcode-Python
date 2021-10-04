"""
Find Missing Observations
"""

from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumRolls = sum(rolls)
        sumAll = mean*(n+len(rolls))
        sumRemain = sumAll-sumRolls
        if sumRemain < n or sumRemain / n > 6: return []
        div = sumRemain // n
        remain = sumRemain % n
        res = [div]*n
        for i in range(remain):
            res[i] += 1
        return res