"""
Largest Time for Given Digits
"""

from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        visited = [False for _ in range(4)]
        res = []

        def isValidTime(track):
            index0check = (0 <= int(track[0]) <= 2)
            index1check = (0 <= int(track[0]) <= 1) or (int(track[0]) == 2 and 0 <= int(track[1]) <= 3)
            index2check = (0 <= int(track[2]) <= 5)
            return index0check and index1check and index2check

        def isLargerTime(track):
            nonlocal res
            if not res: return True
            hour1 = int(res[0] + res[1])
            hour2 = int(track[0] + track[1])
            minute1 = int(res[2] + res[3])
            minute2 = int(track[2] + track[3])
            return hour2 > hour1 or (hour2 == hour1 and minute2 > minute1)

        def helper(arr, track, visited):
            nonlocal res
            if len(track) == 4:
                if isValidTime(track):
                    if isLargerTime(track):
                        res = track[:]
                return
            for i in range(4):
                if visited[i]: continue
                visited[i] = True
                track.append(str(arr[i]))
                helper(arr, track, visited)
                track.pop()
                visited[i] = False

        helper(arr, [], visited)

        return "" if res == [] else "".join(res[0:2]) + ":" + "".join(res[2:])