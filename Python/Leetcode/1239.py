"""
Maximum Length of a Concatenated String with Unique Characters
"""
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = -1
        strList = []

        def checkValidAddItem(addItem, strList):
            concatStr = ''.join(strList)
            for char in addItem:
                if char in concatStr:
                    return False
            return True

        def checkValidString(string):
            return len(string) == len(set(string))

        def backtrack(index, strList, arr):
            nonlocal res
            res = max(res, len(''.join(strList)))
            for i in range(index, len(arr)):
                if checkValidAddItem(arr[i], strList) and checkValidString(arr[i]):
                    strList.append(arr[i])
                    backtrack(i + 1, strList, arr)
                    strList.pop(-1)

        backtrack(0, strList, arr)

        return res