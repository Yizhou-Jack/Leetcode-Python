"""
House Robber III
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0, 0)
            leftNode = helper(node.left)
            rightNode = helper(node.right)
            return (
            node.val + leftNode[1] + rightNode[1], max(leftNode[0], leftNode[1]) + max(rightNode[0], rightNode[1]))

        return max(helper(root))
