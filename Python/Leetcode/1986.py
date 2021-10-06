"""
Minimum Number of Work Sessions to Finish the Tasks
"""

from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        dp = [[999] * n for _ in range(1 << n)]
        dp[0][0] = 0
        for mask in range(1, 1 << n):
            #print("mask: " + str(mask))
            for i in range(n):
                #print("i: " + str(i))
                if (1 << i) & mask:
                    num = (1 << i) ^ mask
                    #print("num: " + str(num))
                    for j in range(n):
                        bagSize = dp[num][j]
                        #print("j:" + str(j))
                        #print("bagsize: " + str(bagSize))
                        if bagSize < 999:
                            if (bagSize + tasks[i]) > sessionTime:
                                dp[mask][j+1] = min(dp[mask][j+1], tasks[i])
                            else:
                                dp[mask][j] = min(dp[mask][j], tasks[i]+bagSize)
                                #print("target:" + str(dp[mask][j]))
        #for i in range(len(dp)):
        #    print(str(i) + ": " + str(dp[i]))
        for i in range(len(dp[(1 << n)-1])):
            if dp[(1 << n)-1][i] < 999:
                return i+1
        return -1

solution = Solution()
tasks = [7,4,3,8,10]
sessionTime = 12
res = solution.minSessions(tasks, sessionTime)
print(res)