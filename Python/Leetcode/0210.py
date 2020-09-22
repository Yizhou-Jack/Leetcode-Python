"""
广度优先遍历+贪心算法=拓扑排序
时间复杂度：O(E+V)
"""

from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        cLen = len(prerequisites)
        if cLen == 0: return [i for i in range(numCourses)]
        inDegrees = [0 for _ in range(numCourses)]
        neiborTable = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            inDegrees[second] += 1
            neiborTable[first].add(second)

        res = []
        queue = deque([])
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)

        while queue:
            element = queue.popleft()
            res.append(element)
            for successor in neiborTable[element]:
                inDegrees[successor] -= 1
                if inDegrees[successor] == 0:
                    queue.append(successor)

        if len(res) != numCourses: return []
        return res

solution = Solution()
res = solution.findOrder(2, [[0,1]])
print(res)