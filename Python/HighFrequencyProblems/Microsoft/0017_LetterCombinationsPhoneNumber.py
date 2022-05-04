from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if digits == "":
            return res

        def helper(hashMap, digits, index, track):
            if len(track) == len(digits):
                res.append("".join(track))
                return
            chars = hashMap[digits[index]]
            for c in chars:
                track.append(c)
                helper(hashMap, digits, index + 1, track)
                track.pop()

        helper(hashMap, digits, 0, [])
        return res
