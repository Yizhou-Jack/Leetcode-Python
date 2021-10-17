"""
Perfect Squares
(knapsack problem)
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1, i+1):
                square = j*j
                if i-square < 0:
                    break
                if 1+dp[i-square] < dp[i]:
                    dp[i] = 1+dp[i-square]
        return dp[n]