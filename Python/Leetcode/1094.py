"""
Car Pooling
"""

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        startTimes = sorted([(trip[1], trip[0]) for trip in trips])
        endTimes = sorted([(trip[2], trip[0]) for trip in trips])
        num = 0
        start = 0
        end = 0
        while start < len(trips):
            if startTimes[start][0] < endTimes[end][0]:
                num += startTimes[start][1]
            else:
                num -= endTimes[end][1]
                end += 1
                continue
            start += 1
            if num > capacity:
                return False
        return True