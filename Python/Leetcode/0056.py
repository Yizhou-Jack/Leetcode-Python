"""
Merge Intervals
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prevStart, prevEnd = res[-1]
            currStart, currEnd = intervals[i]
            if prevEnd >= currStart:
                res.pop()
                res.append([min(prevStart, currStart), max(currEnd, prevEnd)])
            else:
                res.append(intervals[i])
        return res