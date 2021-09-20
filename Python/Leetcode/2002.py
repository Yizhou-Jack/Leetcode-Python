"""
Maximum Product of the Length of Two Palindromic Subsequences
"""

class Solution:
    def maxProduct(self, s: str) -> int:
        memo = {}
        n = len(s)
        for i in range(1, 1 << n):
            temp = ""
            for j in range(n):
                if i >> j & 1 == 1:
                    temp += s[j]
            if temp == temp[::-1]:
                memo[i] = len(temp)
        res = 0
        for ix, lenx in memo.items():
            for iy, leny in memo.items():
                if ix & iy == 0:
                    res = max(res, lenx*leny)
        return res