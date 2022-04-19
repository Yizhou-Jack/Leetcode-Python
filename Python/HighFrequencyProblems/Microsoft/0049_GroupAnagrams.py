# input: ["eat", "tea"]
# output: [["eat", "tea"], [....]]

"""
input: strs -> consist of word
example of the word -> eat -> aet
another example of the word -> tea -> aet
hash(aet -> reordered word) -> number

hash(aet) -> 1
hash(ant) -> 2
hashValues -> store the 1,2
hashtable -> store the original word -> {"1":[]}
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hashValues = set()
        hashTable = defaultdict(list)
        for i in range(n):
            originalWord = strs[i]
            word = list(strs[i])
            word.sort()
            reorderWord = "".join(word)
            if reorderWord not in hashValues:
                hashValues.add(reorderWord)
            hashTable[reorderWord].append(originalWord)
        res = []
        for reorderWord in hashValues:
            res.append(hashTable[reorderWord])
        return res