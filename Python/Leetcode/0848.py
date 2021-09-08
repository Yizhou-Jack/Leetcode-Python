"""
Shifting Letters
"""

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        if n == 0: return ""
        map = {}
        convertMap = {}
        for i in range(26):
            map[chr(i+97)] = i
            convertMap[i] = chr(i+97)
        res = ""
        for i in range(n-1, -1, -1):
            addShift = 0 if i == n-1 else shifts[i+1]
            shift = shifts[i]
            startValue = map[s[i]]
            shiftValue = (shift+addShift)%26
            sumValue = (shiftValue+startValue)%26
            shifts[i] = shiftValue
            subRes = convertMap[sumValue]
            res = subRes+res
        return res