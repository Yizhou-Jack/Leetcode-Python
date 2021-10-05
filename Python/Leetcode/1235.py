"""
Maximum Profit in Job Scheduling (1235)

dp[i] represents the max profit of take job i
Assume we have job x (x < j):
if time not conflict, we will have dp[i] = max(dp[i], dp[x]+profit[i]);
if time conflict, we can not do job x if we take job i now.
So dp[i] = max(dp[0], dp[1], ..., dp[j]) + profit[i]

Use pos index to record the max index of job which will not cause time conflict.
"""

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        length = len(startTime)
        times = [[0, 0, 0] for _ in range(length)]
        for i in range(length):
            times[i][0] = startTime[i]
            times[i][1] = endTime[i]
            times[i][2] = profit[i]
        times.sort()

        dp = [0]*length
        res = 0
        s = 0
        pos = 0
        for i in range(length):
            for j in range(pos, i):
                if times[i][0] >= times[j][1]:
                    if pos == j:
                        pos += 1
                    s = max(s, dp[j])
            dp[i] = s+times[i][2]
            res = max(res, dp[i])
        return res