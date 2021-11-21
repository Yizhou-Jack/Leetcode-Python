"""
Kth Smallest Number in Multiplication Table
"""

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper(x):
            return sum([min(x // i, n) for i in range(1, m + 1)]) >= k

        left = 0
        right = m * n
        while left < right:
            mid = (left + right) // 2
            if not helper(mid):
                left = mid + 1
            else:
                right = mid

        return left