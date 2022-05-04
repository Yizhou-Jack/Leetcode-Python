"""
Palindrome Linked List
"""

"""
on the top of my mind is that we could iterate through the whole linked list
and store all of its values into a list
then we can check whether this list is palindrome or not using two pointer
one starts from the start of the list and one starts from the end of the list
the time complexity of this solution shoud be O(N) and the space complexity should be O(N) too

this solution could be optimized
we could have two pointers first. one is called slow and one is called fast
two pointers iterate through the start of this array
the slow pointer is updated by slow = slow.next()
the fast pointer is updated by fast = fast.next().next()
so when the fast pointer becomes None or the fast.next() becomes None
the slow pointer will reach the middle point of this linked list

then for the next half of the linked list
we can reverse it
then we assign two different pointers
one starts from the start of the linked list
another one starts from the start of the reversed linked list
we iterate through these two linked list simultaneously and check whether their value is equal
return true if all of their values are equal, return false if we meet other cases
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        curr = middle
        prev = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        pointer1 = dummy.next
        pointer2 = prev
        while pointer1 is not None and pointer2 is not None:
            if pointer1.val != pointer2.val:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return True