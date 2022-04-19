"""
Rotate List
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        lastElement = head
        length = 1
        while lastElement.next:
            lastElement = lastElement.next
            length += 1
        k = k % length
        lastElement.next = head

        node = head
        for _ in range(length-k-1):
            node = node.next
        res = node.next
        node.next = None
        return res