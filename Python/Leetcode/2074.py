# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseEvenLengthGroups1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        node = head
        while node:
            nodeList.append(node)
            node = node.next
        groupLen = 1
        startIndex = 0
        while startIndex < len(nodeList):
            print(len(nodeList[startIndex:startIndex+groupLen]))
            print(len(nodeList[startIndex:startIndex+groupLen])%2)
            if len(nodeList[startIndex:startIndex+groupLen])%2 == 1:
                startIndex = startIndex+groupLen
                groupLen += 1
            else:
                for i in range(startIndex+len(nodeList[startIndex:startIndex+groupLen])-1, startIndex, -1):
                    nodeList[i].next = nodeList[i-1]
                nodeList[startIndex].next = None if (len(nodeList[startIndex:startIndex+groupLen]) != groupLen or len(nodeList) <= startIndex+groupLen) else nodeList[startIndex+groupLen]
                temp = len(nodeList[startIndex:startIndex+groupLen])
                temp2 = 1 if (groupLen-1)%2 == 1 else groupLen-1
                nodeList[startIndex-temp2].next = nodeList[startIndex+temp-1]
                startIndex = startIndex+groupLen
                groupLen += 1
        return nodeList[0]

    def reverseEvenLengthGroups2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        n = 0
        while node:
            node = node.next
            n += 1

        node = head
        k = 0
        stack = []
        while n > 0:
            k += 1
            size = min(k, n)
            if size%2 == 0:
                temp = node
                for _ in range(size):
                    stack.append(temp.val)
                    temp = temp.next
            for _ in range(size):
                if stack:
                    node.val = stack.pop()
                node = node.next
            n -= size
        return head