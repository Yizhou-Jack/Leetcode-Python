#TreeNode
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


#LinkedList
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#Queue
stack = [1, 2, 3]
stack.append(4)
stack.append(5) # [1, 2, 3, 4, 5]
stack.pop() # [1, 2, 3, 4]


#Stack
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham") # deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
queue.popleft()
queue.popleft() # deque(['Michael', 'Terry', 'Graham'])


#Heap
import heapq
#从数据源挨个构建heap
data = [5,1,2,5,6,9,4,2,1]
heap = []
for i in data:
    heapq.heappush(heap, i)
#重新组织列表元素
heapq.heapify(data)
#弹出最小元素
heapq.heappop(heap)
#置换最小元素为新元素
heapq.heapreplace(heap, 10)
print(heap)