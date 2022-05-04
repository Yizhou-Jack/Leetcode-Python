"""
Questions:
length of the reservedSeats
size of the n
"""

from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def isRowType1(seats):
            return True if (2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats) else False
        def isRowType2(seats):
            return True if (2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats) else False
        def isRowType3(seats):
            return True if (6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats) else False
        def isRowType4(seats):
            return True if (4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats) else False
        rowType1 = 0
        rowType2 = 0
        rowType3 = 0
        rowType4 = 0
        rowType5 = 0
        reservedSeats.sort()
        hashMap = defaultdict(list)
        hashMapKeySet = set()
        for reservedSeat in reservedSeats:
            rowNum, colNum = reservedSeat
            hashMapKeySet.add(rowNum)
            hashMap[rowNum].append(colNum)
        for key in hashMapKeySet:
            seats = hashMap[key]
            if isRowType1(seats):
                rowType1 += 1
            elif isRowType2(seats):
                rowType2 += 1
            elif isRowType3(seats):
                rowType3 += 1
            elif isRowType4(seats):
                rowType4 += 1
            else:
                rowType5 += 1
        res = (n-rowType2-rowType3-rowType4-rowType5)*2 + (rowType2+rowType3+rowType4)
        return res