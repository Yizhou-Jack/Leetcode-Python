"""
Remove Duplicates from Sorted List II
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        start = ListNode(-999)
        start.next = head
        prev = start
        node = head
        while node and node.next:
            if node.val == node.next.val:
                while node and node.next and node.val == node.next.val:
                    node = node.next
                node = node.next
                prev.next = node
            else:
                prev = prev.next
                node = node.next
        return start.next
