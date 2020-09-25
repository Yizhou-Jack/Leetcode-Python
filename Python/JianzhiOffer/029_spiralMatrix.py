class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        num = m*n
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        res = []
        row = 0
        col = 0
        up = 0
        down = m-1
        left = 0
        right = n-1
        direction = (0, 1)
        while num:
            if direction == directions[3] and row == up:
                left += 1
                direction = directions[0]
            if direction == directions[0] and col == right:
                up += 1
                direction = directions[2]
            if direction == directions[2] and row == down:
                right -= 1
                direction = directions[1]
            if direction == directions[1] and col == left:
                down -= 1
                direction = directions[3]
            res.append(matrix[row][col])
            row += direction[0]
            col += direction[1]
            num -= 1
        return res

solution = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
res = solution.spiralOrder(matrix)
print(res)