"""
Remove Covered Intervals
"""

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = len(intervals)
        intervals.sort()
        curr = intervals[0]
        for interval in intervals[1:]:
            if curr[1] >= interval[1]:
                res -= 1
            elif curr[0] == interval[0]:
                res -= 1
                curr = interval
            else:
                curr = interval
        return res