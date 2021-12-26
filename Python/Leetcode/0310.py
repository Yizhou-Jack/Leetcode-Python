"""
Minimum Height Trees
"""

from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        if not edges:
            return [0]
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = []
        newLeaves = []
        inDegrees = []
        for i in range(n):
            inDegrees.append(len(graph[i]))
            if len(graph[i]) == 1:
                leaves.append(i)
        while n > 2:
            for leaf in leaves:
                for adj in graph[leaf]:
                    inDegrees[adj] -= 1
                    if inDegrees[adj] == 1:
                        newLeaves.append(adj)
            n -= len(leaves)
            leaves = newLeaves[:]
            newLeaves.clear()
        return leaves