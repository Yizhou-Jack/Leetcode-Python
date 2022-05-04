from typing import List

class Solution:
    def maxNonOverlapping1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        hashMap = {0: 0}
        res = 0
        for i in range(1, n + 1):
            curr = preSum[i]
            prev = curr - target
            if prev in hashMap:
                res += 1
                hashMap = {}
            hashMap[curr] = i
        return res

    def maxNonOverlapping2(self, nums: List[int], target: int) -> int:
        hashSet = {0}
        res = 0
        curr = 0

        for i, num in enumerate(nums):
            curr += num
            prev = curr - target
            if prev in hashSet:
                res += 1
                hashSet = set()
            hashSet.add(curr)

        return res