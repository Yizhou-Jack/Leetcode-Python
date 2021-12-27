"""
Number Complement
"""

class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        count = 0
        while num:
            if not num&1:
                res += 1<<count
            count += 1
            num >>= 1
        return res