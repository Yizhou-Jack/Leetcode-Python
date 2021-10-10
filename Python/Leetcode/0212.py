"""
Word Search II
Like 79 with pruning.
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsList = [[] for _ in range(26)]
        row, col = len(board), len(board[0])
        visited = [[0] * col for _ in range(row)]

        boardCharCount = [0] * 26
        for i in range(row):
            for j in range(col):
                index = ord(board[i][j]) - 97
                boardCharCount[index] += 1
        for word in words:
            wordCharCount = [0] * 26
            flag = False
            for i in range(len(word)):
                index = ord(word[i]) - 97
                wordCharCount[index] += 1
                if wordCharCount[index] > boardCharCount[index]:
                    flag = True
                    break
            if flag: continue
            index = ord(word[0]) - 97
            wordsList[index].append(word)

        def dfs(i, j, k, word):
            nonlocal visited, row, col
            if i < 0 or j < 0 or i == row or j == col or visited[i][j] == 1 or word[k] != board[i][j]:
                return False
            if k == len(word) - 1:
                return True
            visited[i][j] = 1
            if dfs(i - 1, j, k + 1, word) or dfs(i + 1, j, k + 1, word) or dfs(i, j - 1, k + 1, word) or dfs(i, j + 1,
                                                                                                             k + 1,
                                                                                                             word):
                visited[i][j] = 0
                return True
            visited[i][j] = 0
            return False

        res = []
        for i in range(row):
            for j in range(col):
                index = ord(board[i][j]) - 97
                subWords = wordsList[index]
                for subWord in subWords:
                    if dfs(i, j, 0, subWord) and subWord not in res:
                        res.append(subWord)

        return res