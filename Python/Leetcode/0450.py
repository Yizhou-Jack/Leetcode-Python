"""
Delete Node in a BST
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(node, key):
            if not node:
                return None
            if node.val == key:
                if not node.right:
                    return node.left
                if not node.left:
                    print(" ")
                    return node.right
                if node.right and node.left:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    node.val = temp.val
                    node.right = helper(node.right, node.val)
            elif node.val > key:
                node.left = helper(node.left, key)
            else:
                node.right = helper(node.right, key)
            return node

        res = helper(root, key)
        return res