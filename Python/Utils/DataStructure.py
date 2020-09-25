# TreeNode
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


# LinkedList
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Stack
stack = [1, 2, 3]
stack.append(4)
stack.append(5) # [1, 2, 3, 4, 5]
stack.pop() # [1, 2, 3, 4]


# Queue
queue = [1, 2]
queue.append(3) # [1, 2, 3]
queue.pop(0) # [2, 3]

from collections import deque
queue2 = deque([1, 2])
queue2.append(3)
queue2.popleft()


# Heap
import heapq
# 从数据源挨个构建heap
data = [5,1,2,5,6,9,4,2,1]
heap = []
for i in data:
    heapq.heappush(heap, i)
# 重新组织列表元素
heapq.heapify(data)
# 弹出最小元素
heapq.heappop(heap)
# 置换最小元素为新元素
heapq.heapreplace(heap, 10)
print(heap)