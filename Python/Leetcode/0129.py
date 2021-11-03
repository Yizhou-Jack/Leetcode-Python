"""
Sum Root to Leaf Numbers
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node, track):
            nonlocal res
            if node is None:
                return
            track.append(str(node.val))
            if node.left is None and node.right is None:
                res += int("".join(track))
                return
            if node.left:
                helper(node.left, track)
                track.pop()
            if node.right:
                helper(node.right, track)
                track.pop()
        helper(root, [])
        return res