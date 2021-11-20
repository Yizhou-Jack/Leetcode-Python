"""
LRU Cache
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
        if node == self.head:
            return
        oldPrev = node.prev
        oldNext = node.next
        if oldPrev:
            oldPrev.next = oldNext
        if oldNext:
            oldNext.prev = oldPrev
        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node
        if self.tail == node:
            self.tail = oldPrev

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
        self.hashmap = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.cache.setHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            self.cache.push(key, value)
            self.hashmap[key] = self.cache.head
            self.size += 1
            if self.size > self.capacity:
                node = self.cache.popTail()
                del self.hashmap[node.key]
                self.size -= 1
        else:
            node = self.hashmap[key]
            node.val = value
            self.cache.setHead(node)