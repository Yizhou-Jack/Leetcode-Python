"""
K Closest Points to Origin
Min heap using Priority Queue.
Time complexity: O(NlogK)
"""
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from queue import PriorityQueue
        q = PriorityQueue()
        for x, y in points:
            q.put((-1*(x*x+y*y), [x, y]))
            if q.qsize() > k:
                q.get()
        res = []
        while q.qsize():
            res.append(q.get()[1])
        return res