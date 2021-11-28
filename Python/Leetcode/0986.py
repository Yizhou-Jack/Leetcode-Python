"""
Interval List Intersections
"""

from typing import List

class Solution:
    def intervalIntersection1(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        na = len(firstList)
        nb = len(secondList)
        res = []
        for i in range(na):
            aStart, aEnd = firstList[i]
            for j in range(nb):
                bStart, bEnd = secondList[j]
                if aStart > bEnd:
                    continue
                elif bStart > aEnd:
                    break
                elif aStart <= bStart and aEnd >= bEnd:
                    res.append([bStart, bEnd])
                elif aStart >= bStart and aEnd <= bEnd:
                    res.append([aStart, aEnd])
                elif aStart >= bStart and aEnd >= bEnd:
                    res.append([aStart, bEnd])
                elif aStart <= bStart and aEnd <= bEnd:
                    res.append([bStart, aEnd])
        return res

    def intervalIntersection2(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
            else:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1
        return res