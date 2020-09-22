class Solution:
    def cuttingRope(self, n):
        if n < 3: return n-1
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(1, n+1):
            for j in range(2, i):
                tmp = max(j, dp[j]) * max(i-j, dp[i-j])
                dp[i] = max(dp[i], tmp)
        return dp[n]

solution = Solution()
res = solution.cuttingRope(6)
print(res)