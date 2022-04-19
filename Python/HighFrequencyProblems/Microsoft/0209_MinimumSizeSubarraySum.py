"""
Minimum Size Subarray Sum
"""

"""
On the top of my mind is that we could iterate through the array and do sum for each interval
so we are going to have two nested for loops
for each index pair, we will calculate the sum of this interval, if the value is greater or equal to target
we will record it and compare it with the result value
the time complexity of this solution should be O(n^2)

But this solution could be optimized
we can use two pointers, one is called left and another one is called right
two pointers are all start from the index 0
"""

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