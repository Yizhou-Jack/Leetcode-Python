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
    def minSubArrayLen1(self, s, nums):
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

    def minSubArrayLen2(self, target, nums):
        numSum = [nums[0]]
        for i in range(len(nums) - 1):
            numSum.append(numSum[i] + nums[i + 1])

        def findLeft(left, right, numSum, target, subNumSum):
            while left < right:
                mid = (left + right) // 2
                if subNumSum - numSum[mid] >= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        res = float("inf")
        left = 0
        for right in range(len(numSum)):
            subNumSum = numSum[right]
            if subNumSum >= target:
                left = findLeft(left, right, numSum, target, subNumSum)
                res = min(res, right - left + 1)
        return res if res <= len(numSum) else 0

solution = Solution()
res = solution.minSubArrayLen1(3, [1,1])
print(res)