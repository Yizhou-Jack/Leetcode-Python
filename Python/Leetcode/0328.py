"""
Odd Even Linked List
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (head and not head.next) or (head and head.next and not head.next.next):
            return head
        res1 = head
        res2 = head.next
        node1 = head
        node2 = head.next
        node1Last = None
        while node1:
            if node2:
                node1.next = node2.next
                if node2.next:
                    node2.next = node2.next.next
            node1Last = node1
            node1 = node1.next
            if node2:
                node2 = node2.next
        node1Last.next = res2
        return res1