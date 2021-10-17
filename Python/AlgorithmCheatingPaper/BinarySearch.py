"""
374: Guess Number Higher or Lower
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def guess():
            return 0

        left = 0
        right = n
        while left <= right:
            mid = (left+right)//2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                left = mid+1
            else:
                right = mid-1