from typing import List

class Solution:
    def countServers1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        res = set()
        for i in range(m):
            memo = []
            for j in range(n):
                if grid[i][j] == 1:
                    memo.append((i, j))
            if len(memo) > 1:
                for server in memo:
                    res.add(server)
        for j in range(n):
            memo = []
            for i in range(m):
                if grid[i][j] == 1:
                    memo.append((i, j))
            if len(memo) > 1:
                for server in memo:
                    res.add(server)
        return len(res)

    def countServers2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    res += 1
        return res