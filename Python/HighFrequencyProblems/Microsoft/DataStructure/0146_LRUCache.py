"""
LRU Cache
"""

"""
on the top of my mind is that we can use double linked list as cache to solve this problem
the basic unit of double linked list looks like this structure
node -> key, val, prev, next
for the double linked list

if we call the get method, it will check whether this cache has the target value
if no, it will return None. if yes, it will return the value and set the head of the double linked list to be this kv
so we need a method called setHead in the double linked list

if we call the put method,
if the size of the cache is okay with this put
this kv will be put into the head of this double linked list
so we need a method called setTail in the double linked list
and if we put one kv into the double linked list and find the size is larger than capacity
we need to remove the tail of the double linked list
so we need a method called popTail in the double linked list
"""

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, key, val) -> None:
        node = Node(key, val)
        if self.head == self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def setHead(self, node) -> None:
        oldPrev = node.prev
        oldNext = node.next
        if node == self.head:
            return
        if node == self.tail:
            self.tail = oldPrev
        if oldPrev:
            oldPrev.next = oldNext
        if oldNext:
            oldNext.prev = oldPrev
        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node

    def popTail(self) -> Node:
        if self.tail:
            node = self.tail
            self.tail.prev.next = None
            self.tail = node.prev
            return node
        return None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = DoubleLinkedList()
        self.hashMap = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.cache.setHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.hashMap:
            self.cache.push(key, value)
            self.hashMap[key] = self.cache.head
            self.size += 1
            if self.size > self.capacity:
                node = self.cache.popTail()
                del self.hashMap[node.key]
                self.size -= 1
        else:
            node = self.hashMap[key]
            node.val = value
            self.cache.setHead(node)