"""
Reverse nodes in k groups
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Reverse a node group and return its tail and head
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        curr = head
        while prev != tail:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            tail = prev
            # Check the rest of the length is larger than k or not
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            next = tail.next
            head, tail = self.reverse(head, tail)
            # Connect the reversed sub linked list back to original linked list
            prev.next = head
            tail.next = next
            prev = tail
            head = tail.next

        return dummy.next