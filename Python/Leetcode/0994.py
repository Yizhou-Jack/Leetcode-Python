"""
Rotting Oranges
"""

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rotOranges = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotOranges.append((i, j))

        res = 0
        while len(rotOranges) > 0:
            lenRotOranges = len(rotOranges)
            for i in range(lenRotOranges):
                idx, idy = rotOranges[i]
                if idx - 1 >= 0 and grid[idx - 1][idy] == 1:
                    grid[idx - 1][idy] = 2
                    rotOranges.append((idx - 1, idy))
                if idx + 1 < row and grid[idx + 1][idy] == 1:
                    grid[idx + 1][idy] = 2
                    rotOranges.append((idx + 1, idy))
                if idy - 1 >= 0 and grid[idx][idy - 1] == 1:
                    grid[idx][idy - 1] = 2
                    rotOranges.append((idx, idy - 1))
                if idy + 1 < col and grid[idx][idy + 1] == 1:
                    grid[idx][idy + 1] = 2
                    rotOranges.append((idx, idy + 1))
            res += 1
            rotOranges = rotOranges[lenRotOranges:]

        num0 = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
                if grid[i][j] == 0:
                    num0 += 1
        if num0 == row * col:
            return 0
        return res - 1