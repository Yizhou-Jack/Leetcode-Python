"""
Topological Sort
Time complexity：O(E+V)
"""

from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        inDegrees = defaultdict(int)
        for u, v in prerequisites:
            graph[v].add(u)
            inDegrees[u] += 1
        queue = deque()
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for adj in graph[curr]:
                inDegrees[adj] -= 1
                if inDegrees[adj] == 0:
                    queue.append(adj)
        return res if len(res) == numCourses else []

solution = Solution()
res = solution.findOrder(2, [[0,1]])
print(res)