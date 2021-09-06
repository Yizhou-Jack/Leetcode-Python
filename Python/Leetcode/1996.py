"""
The Number of Weak Characters in the Game
"""

from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        res = 0
        currMax = 0
        for attack, defense in properties:
            if defense < currMax:
                res += 1
            else:
                currMax = defense
        return res