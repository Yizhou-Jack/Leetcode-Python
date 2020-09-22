"""
matrix = N*N
Time: O(N^3)
Space: O(N^2)
"""
class Solution1:
    def maximalRectangle(self, matrix) -> int:
        maxArea = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: continue
                # compute the maximum width and update dp with it
                dp[i][j] = dp[i][j-1] + 1
                width = dp[i][j]
                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    height = i-k+1
                    maxArea = max(maxArea, width * height)
        return maxArea


"""
matrix = N*N
Time: O(N^2)
Space: O(N)
"""
class Solution2:
    def maximalRectangle(self, matrix):
        maxArea = 0
        heights = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0
            stack = [0]
            newHeight = [-1] + heights + [-1]
            for j in range(1, len(newHeight)):
                while newHeight[j] < newHeight[stack[-1]]:
                    curHeight = newHeight[stack.pop()]
                    curWidth = j-stack[-1]-1
                    maxArea = max(maxArea, curHeight*curWidth)
                stack.append(j)

        return maxArea

matrix = [[1,1,1,1,1,1,1,1],
          [1,0,1,1,1,0,1,1],
          [0,0,1,1,1,0,0,0],
          [0,1,1,1,1,1,0,0],
          [0,0,1,1,1,0,1,1],
          [0,0,1,1,0,0,1,1]]
solution = Solution2()
res = solution.maximalRectangle(matrix)
print(res)