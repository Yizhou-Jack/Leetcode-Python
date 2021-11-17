"""
Unique Paths
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        temp1 = None
        temp2 = None
        for i in range(m):
            if i == 0:
                continue
            for j in range(n):
                temp1 = 0 if j == 0 else dp[j-1]
                temp2 = dp[j]
                dp[j] = temp1+temp2
        return dp[-1]