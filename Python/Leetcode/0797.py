"""
All Paths From Source to Target
"""

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        def helper(track, candidates):
            if track and track[-1] == n-1:
                res.append(track.copy())
                return
            for candidate in candidates:
                track.append(candidate)
                helper(track, graph[candidate])
                track.pop()
        helper([0], graph[0])
        return res