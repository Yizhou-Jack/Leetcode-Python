class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        numStr = str(num)
        dp = [1 for _ in range(len(numStr))]
        if '10' <= numStr[0:2] < '26':
            dp[1] = 2
        for i in range(2, len(numStr)):
            if '10' <= numStr[i-1:i+1] < '26':
                dp[i] = dp[i-2]+dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[len(numStr)-1]