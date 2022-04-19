"""
Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
"""

"""
We are going to use prefix-sum to solve this question.
we iterate through the nums and add num into sums.
whenever the sums has increased by a value of k, we found a subarray of sums=k.
Example: Let's say our elements are [1,2,1,3] and k = 3.
and our corresponding running sums = [0,1,3,4,7] (0 should be also contained in the sums array)
Try to see for the increase of k: 0->3, 1->4, 4->7
Hence, 3 sub arrays of sums=k
"""

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1
        res = 0
        tempSum = 0
        for num in nums:
            tempSum += num
            res += hm[tempSum-k]
            hm[tempSum] += 1
        return res