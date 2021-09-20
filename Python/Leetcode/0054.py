"""
Spiral Matrix
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        up = 0
        down = len(matrix) - 1
        if down == -1: return res
        left = 0
        right = len(matrix[0]) - 1

        direction = [0, 1]

        row = 0
        col = 0

        count = (down + 1) * (right + 1)
        while count > 0:
            res.append(matrix[row][col])
            count -= 1
            if row == up and col == right and direction[1] == 1:
                direction = [1, 0]
                up += 1
            elif row == down and col == right and direction[0] == 1:
                direction = [0, -1]
                right -= 1
            elif row == down and col == left and direction[1] == -1:
                direction = [-1, 0]
                down -= 1
            elif row == up and col == left and direction[0] == -1:
                direction = [0, 1]
                left += 1
            row += direction[0]
            col += direction[1]
        return res