from collections import deque

"""
With data comes in order
"""
class HitCounter1:
    def __init__(self):
        self.queue = deque()

    def hit(self, timeStamp: int) -> None:
        self.queue.append(timeStamp)

    def getHits(self, timeStamp: int) -> int:
        while self.queue and timeStamp - self.queue[0] >= 300:
            self.queue.popleft()
        return len(self.queue)

"""
With data comes in unordered and several hits carry the same timestamp

we need to change to array because queue approach is not working since data is unordered
"""
class HitCounter2:
    def __init__(self):
        self.hits = [0]*300
        self.times = [0]*300

    def hit(self, timeStamp: int) -> None:
        index = timeStamp % 300
        if self.times[index] != timeStamp:
            self.times[index] = timeStamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timeStamp: int) -> int:
        res = 0
        for i in range(300):
            if timeStamp-self.times[i] < 300:
                res += self.hits[i]
        return res

"""
Follow Ups:
How to handle concurrent requests?
When two requests update the list simultaneously, there can be race conditions.
It’s possible that the request that updated the list first may not be included eventually.
The most common solution is to use a lock to protect the list.
Whenever someone wants to update the list (by either adding new elements or removing the tail),
a lock will be placed on the container.
After the operation finishes, the list will be unlocked.
This works pretty well when you don’t have a large volume of requests or performance is not a concern.
Placing a lock can be costly at some times and when there are too many concurrent requests,
the lock may potentially block the system and becomes the performance bottleneck.
"""