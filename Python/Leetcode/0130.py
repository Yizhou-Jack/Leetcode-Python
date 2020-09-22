from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(board, directions, i, j, n):
            queue = deque([])
            queue.append((i, j))
            while queue:
                rIndex, cIndex = queue.popleft()
                for direction in directions:
                    nrIndex = rIndex + direction[0]
                    ncIndex = cIndex + direction[1]
                    if 0 <= nrIndex < n and 0 <= ncIndex < m and board[nrIndex][ncIndex] == 'O':
                        board[nrIndex][ncIndex] = 'T'
                        queue.append((nrIndex, ncIndex))

        n = len(board)
        if n == 0: return board
        m = len(board[0])

        for i in range(n):
            if board[i][0] == 'O':
                board[i][0] = 'T'
                bfs(board, directions, i, 0, n)
            if board[i][m-1] == 'O':
                board[i][m-1] = 'T'
                bfs(board, directions, i, m-1, n)

        for i in range(m):
            if board[0][i] == 'O':
                board[0][i] = 'T'
                bfs(board, directions, 0, i, n)
            if board[n-1][i] == 'O':
                board[n-1][i] = 'T'
                bfs(board, directions, n-1, i, n)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'