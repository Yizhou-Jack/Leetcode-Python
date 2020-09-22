# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        curr1 = l1
        curr2 = l2
        curr = ListNode(0)
        res = curr
        while curr1 and curr2:
            if curr1.val > curr2.val:
                currNext = ListNode(curr2.val)
                curr2 = curr2.next
            else:
                currNext = ListNode(curr1.val)
                curr1 = curr1.next
            curr.next = currNext
            curr = currNext
        if curr1: curr.next = curr1
        if curr2: curr.next = curr2
        return res.next