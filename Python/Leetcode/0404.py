"""
Sum of Left Leaves
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(root, False)]
        while stack:
            curr, isLeft = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right:
                if isLeft:
                    result += curr.val
            else:
                stack.append((curr.left, True))
                stack.append((curr.right, False))
        return result