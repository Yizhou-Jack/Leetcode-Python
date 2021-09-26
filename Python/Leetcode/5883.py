"""
Check if Word Can Be Placed In Crossword
"""
from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        for i in range(m):
            index = 0
            for j in range(n+1):
                if j == n or board[i][j] == '#':
                    if index == w:
                        return True
                    else:
                        index = 0
                else:
                    if board[i][j] == ' ':
                        index += 1
                    elif index >= w or board[i][j] != word[index]:
                        index = w+1
                    else:
                        index += 1
        for i in range(m):
            index = 0
            for j in range(n-1, -2, -1):
                if j == -1 or board[i][j] == '#':
                    if index == w:
                        return True
                    else:
                        index = 0
                else:
                    if board[i][j] == ' ':
                        index += 1
                    elif index >= w or board[i][j] != word[index]:
                        index = w+1
                    else:
                        index += 1
        for j in range(n):
            index = 0
            for i in range(m+1):
                if i == m or board[i][j] == '#':
                    if index == w:
                        return True
                    else:
                        index = 0
                else:
                    if board[i][j] == ' ':
                        index += 1
                    elif index >= w or board[i][j] != word[index]:
                        index = w+1
                    else:
                        index += 1
        for j in range(n):
            index = 0
            for i in range(m-1, -2, -1):
                if i == -1 or board[i][j] == '#':
                    if index == w:
                        return True
                    else:
                        index = 0
                else:
                    if board[i][j] == ' ':
                        index += 1
                    elif index >= w or board[i][j] != word[index]:
                        index = w+1
                    else:
                        index += 1
        return False