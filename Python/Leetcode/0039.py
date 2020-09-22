class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(candidates, track, target, res):
            if sum(track) == target:
                track.sort()
                if track not in res:
                    res.append(track[:])
                return
            elif sum(track) > target:
                return
            for i in range(len(candidates)):
                helper(candidates, track+[candidates[i]], target, res)

        helper(candidates, [], target, res)
        return res

solution = Solution()
res = solution.combinationSum([1,2], 4)