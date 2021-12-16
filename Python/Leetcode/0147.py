from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        dummyHead.next = head
        while head and head.next:
            if head.val > head.next.val:
                insertNode = head.next
                preInsertNode = dummyHead
                while preInsertNode.next.val < insertNode.val:
                    preInsertNode = preInsertNode.next
                head.next = insertNode.next
                insertNode.next = preInsertNode.next
                preInsertNode.next = insertNode
            else:
                head = head.next
        return dummyHead.next