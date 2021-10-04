"""
Jump Game
"""

class Solution:
    def canJump(self, nums):
        if len(nums) == 1: return True
        N, requiredJumps = len(nums), 1
        for i in range(N - 2, 0, -1):
            if nums[i] < requiredJumps:
                requiredJumps += 1
            else:
                requiredJumps = 1
        return nums[0] >= requiredJumps