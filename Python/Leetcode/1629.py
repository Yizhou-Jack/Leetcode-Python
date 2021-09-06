"""
Slowest Key
"""

from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxKey = keysPressed[0]
        maxTime = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            time = releaseTimes[i] - releaseTimes[i-1]
            if time > maxTime or (time == maxTime and key > maxKey):
                maxKey = key
                maxTime = time
        return maxKey