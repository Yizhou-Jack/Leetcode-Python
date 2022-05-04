# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashMap = {}
        for i in range(len(inorder)):
            hashMap[inorder[i]] = i

        def helper(inorderLeft, inorderRight, postorderLeft, postorderRight):
            if inorderLeft > inorderRight or postorderLeft > postorderRight:
                return None
            offset = hashMap[postorder[postorderRight]] - inorderLeft
            node = TreeNode(postorder[postorderRight])
            node.left = helper(inorderLeft, inorderLeft + offset - 1, postorderLeft, postorderLeft + offset - 1)
            node.right = helper(inorderLeft + offset + 1, inorderRight, postorderLeft + offset, postorderRight - 1)
            return node

        root = helper(0, len(inorder) - 1, 0, len(postorder) - 1)
        return root