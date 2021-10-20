"""
Word Break II
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordDict = set(wordDict)
        memo = [1]*(n+1)
        res = []
        def dfs(index, track):
            nonlocal s, n, wordDict, res
            num = len(res)
            if index == n:
                res.append(" ".join(track))
                return
            for i in range(index, n+1):
                if memo[i] == 1 and s[index:i] in wordDict:
                    track.append(s[index:i])
                    dfs(i, track)
                    track.pop()
            memo[index] = 1 if len(res) > num else 0
        dfs(0, [])
        return res