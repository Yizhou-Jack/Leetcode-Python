class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsLen = len(nums)
        if numsLen <= 1: return [nums]
        visited = [False for _ in range(numsLen)]
        res = []

        def helper(nums, track, res, visited):
            if len(nums) == len(track):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if visited[i]: continue
                track.append(nums[i])
                visited[i] = True
                helper(nums, track, res, visited)
                track.pop()
                visited[i] = False

        helper(nums, [], res, visited)
        return res