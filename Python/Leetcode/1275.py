"""
Find Winner on a Tic Tac Toe Game
"""
from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def win(matrix, player):
            a = matrix[0][0] == matrix[0][1] == matrix[0][2] == player
            b = matrix[1][0] == matrix[1][1] == matrix[1][2] == player
            c = matrix[2][0] == matrix[2][1] == matrix[2][2] == player
            d = matrix[0][0] == matrix[1][0] == matrix[2][0] == player
            e = matrix[0][1] == matrix[1][1] == matrix[2][1] == player
            f = matrix[0][2] == matrix[1][2] == matrix[2][2] == player
            g = matrix[0][0] == matrix[1][1] == matrix[2][2] == player
            h = matrix[0][2] == matrix[1][1] == matrix[2][0] == player
            if a or b or c or d or e or f or g or h: return True
            return False

        def findZero(matrix):
            for i in range(3):
                for j in range(3):
                    if matrix[i][j] == 0: return True
            return False

        matrix = [[0] * 3 for _ in range(3)]
        for i, move in enumerate(moves):
            x = move[0]
            y = move[1]
            if i % 2 == 0:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 2
        if win(matrix, 1): return "A"
        if win(matrix, 2): return "B"
        if not win(matrix, 1) and not win(matrix, 2) and not findZero(matrix): return "Draw"
        return "Pending"