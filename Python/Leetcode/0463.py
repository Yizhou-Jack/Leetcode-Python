"""
Island Perimeter
"""
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        matrix = [[2]*(col+2)] + grid + [[2]*(col+2)]
        for i in range(1, row+1):
            matrix[i] = [2] + matrix[i] + [2]
        res = 0
        for i in range(row+2):
            for j in range(col+2):
                if matrix[i][j] == 1:
                    up = 1 if matrix[i-1][j] == 1 else 0
                    down = 1 if matrix[i+1][j] == 1 else 0
                    left = 1 if matrix[i][j-1] == 1 else 0
                    right = 1 if matrix[i][j+1] == 1 else 0
                    res += 4-(up+down+left+right)
        return res

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
        perimeter = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0: continue
                perimeter += 4
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == row or nc < 0 or nc == col or grid[nr][nc] == 0: continue
                    perimeter -= 1
        return perimeter