"""
Delete and Earn
"""

from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsList = [0]*(max(nums)+1)
        for num in nums:
            numsList[num] += num
        dp = [0]*len(numsList)
        dp[1] = numsList[1]
        for i in range(2, len(dp)):
            dp[i] = max(numsList[i]+dp[i-2], dp[i-1])
        return dp[len(dp)-1]