class Solution:
    def findRepeatNumber(self, nums):
        hm = {}
        for i in range(len(nums)):
            v = hm.get(nums[i], 0)
            if v == 1: return nums[i]
            v += 1
            hm[nums[i]] = v