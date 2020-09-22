class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k < 0: return 0

        def sums(x):
            if x < 0: return float('inf')
            s = 0
            while x != 0:
                s += x % 10
                x = x // 10
            return s

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        marked = [[False] * n for _ in range(m)]
        marked[0][0] = True
        queue = []
        queue.append((0, 0))
        res = 1
        while queue:
            x, y = queue.pop(-1)
            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]
                newSums = sums(newX) + sums(newY)
                if 0 <= newX < m and 0 <= newY < n and not marked[newX][newY] and newSums <= k:
                    res += 1
                    marked[newX][newY] = True
                    queue.append((newX, newY))
        return res

solution = Solution()
res = solution.movingCount(2, 3, 1)
print(res)