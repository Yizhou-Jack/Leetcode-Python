"""
Largest Component Size by Common Factor
"""

import math
import collections
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, index):
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        self.parent[self.find(index2)] = self.find(index1)


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:

        def primeSet(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return primeSet(n // i) | {i}
            return {n}

        n = len(nums)
        uf = UnionFind(n)
        primes = collections.defaultdict(list)

        for i, num in enumerate(nums):
            pSet = primeSet(num)
            for p in pSet:
                primes[p].append(i)

        for _, indexes in primes.items():
            for i in range(len(indexes) - 1):
                uf.union(indexes[i], indexes[i + 1])

        return max(collections.Counter([uf.find(i) for i in range(n)]).values())