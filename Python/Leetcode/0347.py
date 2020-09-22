class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq as hq
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items():
            if len(heap) == k:
                if heap[0][0] < freq:
                    hq.heapreplace(heap, (freq, num))
            else:
                hq.heappush(heap, (freq, num))
        while heap:
            res.append(hq.heappop(heap)[1])
        return res

solution = Solution()
res = solution.topKFrequent([5,3,5,6,2,1,4,8,9,9,3], 2)
print(res)