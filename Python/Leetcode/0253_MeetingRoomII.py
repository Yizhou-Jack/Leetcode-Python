"""
on the top of my mind is that we could use scanning line algorithm
we should order every start time and end time with the increasing order
and the start time should be assign value 1, it means room number should be added by one at that time
and the end time should be assign value -1, it means room number should be minus by one
example: [[0,1], [1,3], [2,4]] -> [(0, 1), (1, -1), (1, 1), (2, 1), (3, -1), (4, -1)]
"""

class Solution:
    def minMeetingRooms(self, intervals):
        room = []
        for interval in intervals:
            room.append((interval[0], 1))
            room.append((interval[1], -1))
        room.sort()
        roomNum = 0
        res = 0
        for _, cost in room:
            roomNum += cost
            res = max(res, roomNum)
        return res