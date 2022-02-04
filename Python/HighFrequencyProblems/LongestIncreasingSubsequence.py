"""
最长上升子序列 (300)
"""

class Solution:
    def lengthOfLIS(self, nums):
        if not nums: return 0
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)