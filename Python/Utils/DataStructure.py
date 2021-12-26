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


# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        root = self.root
        for s in word:
            root = root.children.setdefault(s, TrieNode())
        root.isEnd = True


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
# construct heap
data = [5,1,2,5,6,9,4,2,1]
heap = []
for i in data:
    heapq.heappush(heap, i)
# reorder list to make a heap
heapq.heapify(data)
# pop up min element
heapq.heappop(heap)
# replace min element to new element
heapq.heapreplace(heap, 10)
print(heap)


# Priority Queue
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))
q.qsize() # 3
q.get() # (1, 'eat')