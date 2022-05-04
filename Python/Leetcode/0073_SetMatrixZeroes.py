"""
Set Matrix Zeroes
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        zeroList = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeroList.append((i, j))

        for zeroPos in zeroList:
            rowIndex, colIndex = zeroPos
            for i in range(row):
                matrix[i][colIndex] = 0
            for j in range(col):
                matrix[rowIndex][j] = 0
