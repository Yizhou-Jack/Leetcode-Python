"""
Cousins in Binary Tree
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        isSameParent = False
        xDepth = -1
        yDepth = -1
        def helper(node, level):
            nonlocal isSameParent, xDepth, yDepth, x, y
            if node is None:
                return
            if (node.left is not None and node.left.val == x and node.right is not None and node.right.val == y) or (node.left is not None and node.left.val == y and node.right is not None and node.right.val == x):
                isSameParent = True
                return
            if node.val == x:
                xDepth = level
                return
            if node.val == y:
                yDepth = level
                return
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        if isSameParent:
            return False
        if xDepth == yDepth:
            return True
        return False