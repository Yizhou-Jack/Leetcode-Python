"""
Reverse Words in a String
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(" ")
        resList = []
        for element in sList:
            if element == "":
                continue
            resList = [element] + resList
        res = " ".join(resList)
        return res