"""
Diameter of Binary Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node):
            nonlocal res
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            res = max(res, left+right)
            return max(left, right)+1
        helper(root)
        return res