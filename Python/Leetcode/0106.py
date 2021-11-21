"""
Construct Binary Tree from Inorder and Postorder Traversal
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        def helper(inorderStart, inorderEnd, postorderStart, postorderEnd):
            if inorderStart > inorderEnd:
                return
            rootVal = postorder[postorderEnd]
            index = hashmap[rootVal]
            leftSize = index - inorderStart
            root = TreeNode(rootVal)
            root.left = helper(inorderStart, index - 1, postorderStart, postorderStart + leftSize - 1)
            root.right = helper(index + 1, inorderEnd, postorderStart + leftSize, postorderEnd - 1)
            return root

        root = helper(0, len(inorder) - 1, 0, len(postorder) - 1)
        return root