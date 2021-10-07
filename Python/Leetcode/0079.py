"""
Word Search
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col, wordLen = len(board), len(board[0]), len(word)
        visited = [[0] * col for _ in range(row)]

        def dfs(i, j, k):
            nonlocal board, row, col, wordLen, visited
            if i < 0 or j < 0 or i == row or j == col or visited[i][j] == 1 or board[i][j] != word[k]:
                return False
            if k == wordLen - 1:
                return True
            visited[i][j] = 1
            if dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1):
                return True
            visited[i][j] = 0
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False