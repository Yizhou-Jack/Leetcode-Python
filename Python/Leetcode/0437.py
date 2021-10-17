"""
Path Sum III
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node, track):
            nonlocal res, targetSum
            if node is None:
                return
            track.append(0)
            for i in range(len(track)):
                track[i] += node.val
                if track[i] == targetSum:
                    res += 1
            helper(node.left, track)
            helper(node.right, track)
            track.pop()
            for i in range(len(track)):
                track[i] -= node.val
        res = 0
        helper(root, [])
        return res