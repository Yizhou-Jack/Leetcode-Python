class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        def dfs(x, y, charIndex, marked):
            if x >= m or x < 0 or y >= n or y < 0 or marked[x][y] or board[x][y] != word[charIndex]: return False
            if charIndex == len(word)-1: return True
            marked[x][y] = True
            res = dfs(x+1, y, charIndex+1, marked) or dfs(x-1, y, charIndex+1, marked) or dfs(x, y+1, charIndex+1, marked) or dfs(x, y-1, charIndex+1, marked)
            marked[x][y] = False
            return res

        marked = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = dfs(i, j, 0, marked)
                    if res: return res
        return False