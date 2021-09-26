"""
Grid Game
"""
from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = float("inf")

        sumGrid = grid.copy()
        sumGrid[0] = [0] + sumGrid[0] + [0]
        sumGrid[1] = [0] + sumGrid[1] + [0]

        for i in range(n - 1, 0, -1):
            sumGrid[0][i] += sumGrid[0][i + 1]
        for i in range(1, n + 1):
            sumGrid[1][i] += sumGrid[1][i - 1]
        print(sumGrid)

        for i in range(1, n + 1):
            value = max(sumGrid[1][i - 1], sumGrid[0][i + 1])
            if value < res:
                res = value
        return res