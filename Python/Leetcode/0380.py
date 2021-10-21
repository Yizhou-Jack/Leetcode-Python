"""
Insert Delete GetRandom O(1)
"""

import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.nums.append(val)
            self.dict[val] = len(self.nums)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            lastVal = self.nums[-1]
            self.nums[idx] = lastVal
            self.dict[lastVal] = idx
            self.nums.pop()
            self.dict.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()