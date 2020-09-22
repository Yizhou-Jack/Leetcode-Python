class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None: return None

    fast = head
    slow = head
    flag = False
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            flag = True
            break
    if not flag:
        return None
    else:
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast