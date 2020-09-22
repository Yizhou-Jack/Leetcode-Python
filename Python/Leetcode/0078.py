class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsLen = len(nums)
        if numsLen == 0: return []
        res = []

        def helper(nums, j, track, res):
            track.sort()
            if track not in res:
                res.append(track[:])
            for i in range(j+1, len(nums)):
                helper(nums, i, track+[nums[i]], res)

        nums.sort()
        helper(nums, -1, [], res)
        return res