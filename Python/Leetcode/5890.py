"""
Minimum Moves to Convert String
"""

class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        strList = list(s)
        n = len(strList)
        for i in range(n):
            if strList[i] == 'X':
                res += 1
                strList[i] == 'O'
                if i+1 < n: strList[i+1] = 'O'
                if i+2 < n: strList[i+2] = 'O'
        return res