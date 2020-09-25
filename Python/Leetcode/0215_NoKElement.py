class Solution:
    def findKthLargest(self, A, k):

        def partition(left, right):
            pivot_value = A[right]
            new = left
            for i in range(left, right):
                if A[i] > pivot_value:
                    A[i], A[new] = A[new], A[i]
                    new += 1
            A[new], A[right] = A[right], A[new]
            return new

        left = 0
        right = len(A) - 1
        while left <= right:
            new = partition(left, right)
            if new == k - 1:
                return A[new]
            elif new > k - 1:
                right = new - 1
            else:
                left = new + 1


    def findKthLargest2(self, nums, k):
        import heapq as hq
        heap = []
        hq.heapify(heap)
        for num in nums:
            hq.heappush(heap, num)
            if len(heap) > k:
                hq.heappop(heap)
        return heap[0]