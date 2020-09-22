"""
用一个二维数据dp记录当前情况是从i到j时，先取分数的人，能比后取分数的人多得多少分
length=j-i+1从1开始递增：
1. 当长度是1时，先取数的可以多得nums[i]分；
2. 当长度大于等于2时，可能先取左边的数，也可能先取右边的数，分别可以多得nums[i] - dp[i + 1][j]和num[j] - d[i][j - 1]分，取两者中较大的数即可
"""

def PredictTheWinner(nums):
    n = len(nums)
    if n == 1: return True
    dp = [[0]*n for i in range(n)]
    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if length == 1:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
    return dp[0][n-1] >= 0