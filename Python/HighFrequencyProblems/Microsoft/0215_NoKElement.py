"""
Time complexity (O(k+(n-k)lgk), Min-Heap) analysis:
Explain n*lgk part: heap push -> lgk
This is Min-Heap.

Max-Heap: Insert the negative number
"""

class Solution:
    def findKthLargest(self, nums, k):
        import heapq as hq
        heap = []
        hq.heapify(heap)
        for num in nums:
            hq.heappush(heap, num)
            if len(heap) > k:
                hq.heappop(heap)
        return heap[0]