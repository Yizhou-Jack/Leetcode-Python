"""
Reverse Only Letters
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        sList = list(s)
        i = 0
        j = len(sList)-1
        while i < j:
            while i < len(sList)-1 and not sList[i].isalpha():
                i += 1
            while j > 0 and not sList[j].isalpha():
                j -= 1
            if i < j:
                sList[i], sList[j] = sList[j], sList[i]
            i += 1
            j -= 1
        return "".join(sList)