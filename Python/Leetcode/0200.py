"""
DFS
"""
class DfsSolution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(grid, i, j, n, m, marked, directions):
            marked[i][j] = True
            for direction in directions:
                newI = i + direction[0]
                newJ = j + direction[1]
                if 0 <= newI < n and 0 <= newJ < m and not marked[newI][newJ] and grid[newI][newJ] == '1':
                    dfs(grid, newI, newJ, n, m, marked, directions)

        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        marked = [[False]*m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j, n, m, marked, directions)
        return count


"""
BFS
"""
from collections import deque

class BfsSolution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        marked = [[False]*m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if not marked[i][j] and grid[i][j] == '1':
                    marked[i][j] = True
                    count += 1
                    queue = deque([])
                    queue.append((i,j))
                    while queue:
                        rowIndex, colIndex = queue.popleft()
                        for direction in directions:
                            newRowIndex = rowIndex + direction[0]
                            newColIndex = colIndex + direction[1]
                            if 0 <= newRowIndex < n and 0 <= newColIndex < m and not marked[newRowIndex][newColIndex] and grid[newRowIndex][newColIndex] == '1':
                                queue.append((newRowIndex, newColIndex))
                                marked[newRowIndex][newColIndex] = True
        return count