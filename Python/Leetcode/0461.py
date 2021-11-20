"""
Hamming Distance
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x^y
        res = 0
        for i in range(32):
            if temp & (1 << i) != 0:
                res += 1
        return res