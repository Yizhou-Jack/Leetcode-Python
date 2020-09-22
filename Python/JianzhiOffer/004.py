class Solution:
    def findNumberIn2DArray(self, matrix, target):
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        x = 0
        y = n-1
        while x < m and y > -1:
            num = matrix[x][y]
            if target == num:
                return True
            elif target > num:
                x += 1
            else:
                y -= 1
        return False