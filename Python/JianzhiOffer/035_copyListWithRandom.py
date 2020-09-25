# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None
        node = head
        while node:
            nNode = Node(node.val)
            temp = node.next
            node.next = nNode
            nNode.next = temp
            node = temp
        node = head
        while node:
            randomNode = node.random
            sameNode = node.next
            if randomNode:
                sameNode.random = randomNode.next
            else:
                sameNode.random = None
            node = node.next.next
        res = head.next
        node = head.next
        while node.next:
            node.next = node.next.next
            node = node.next
        return res