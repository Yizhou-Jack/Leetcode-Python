class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def helper(candidates, track, j, target, res):
            if sum(track) == target:
                if track not in res:
                    res.append(track[:])
                    return
            elif sum(track) > target:
                return
            for i in range(j, len(candidates)):
                helper(candidates, track+[candidates[i]], i+1, target, res)

        helper(candidates, [], 0, target, res)
        return res

solution = Solution()
res = solution.combinationSum2([10,1,2,7,6,1,5], 8)
print(res)