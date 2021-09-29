"""
Split Linked List in Parts
"""

from typing import Optional, List
from Python.Utils.DataStructure import ListNode

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        n = 0
        curr = head
        while curr is not None:
            n += 1
            curr = curr.next
        div = n//k-1
        divPlus = n//k
        remain = n%k
        curr = head
        if div == -1:
            while curr is not None:
                prev = curr
                res.append(prev)
                curr = curr.next
                prev.next = None
            remain = k-n
            while remain != 0:
                res.append(None)
                remain -= 1
        while curr is not None:
            recurrentNum = divPlus if remain > 0 else div
            res.append(curr)
            while recurrentNum > 0:
                curr = curr.next
                recurrentNum -= 1
            prev = curr
            curr = curr.next
            prev.next = None
            remain -= 1
        return res