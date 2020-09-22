"""
一个矩阵，左下角填满了0，对角线填满了1
"""

def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dp = [[0] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]