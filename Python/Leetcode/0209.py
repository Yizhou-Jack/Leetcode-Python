class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums: return 0
        if max(nums) >= s: return 1
        right = 0
        left = 0
        subSum = 0
        res = float('inf')
        while right < len(nums):
            subSum += nums[right]
            while subSum >= s:
                res = min(res, right-left+1)
                subSum -= nums[left]
                left += 1
            right += 1
        if res == float('inf'): return 0
        return res

solution = Solution()
res = solution.minSubArrayLen(3, [1,1])
print(res)