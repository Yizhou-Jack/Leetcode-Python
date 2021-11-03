"""
Unique Paths III
"""

from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        start = None
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    count += 1
                if not start and grid[i][j] == 1:
                    start = (i, j)
        DIR = [-1, 0, 1, 0, -1]

        res = 0

        def dfs(i, j):
            nonlocal count, DIR, res
            for k in range(4):
                nr = DIR[k] + i
                nc = DIR[k + 1] + j
                if 0 <= nr < row and 0 <= nc < col:
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        count -= 1
                        dfs(nr, nc)
                        grid[nr][nc] = 0
                        count += 1
                    elif grid[nr][nc] == 2 and count == 0:
                        res += 1

        dfs(start[0], start[1])

        return res