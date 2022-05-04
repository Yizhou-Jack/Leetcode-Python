# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = defaultdict(int)
        for i in range(len(inorder)):
            hashMap[inorder[i]] = i

        def helper(preorderLeft, preorderRight, inorderLeft, inorderRight):
            if preorderLeft > preorderRight or inorderLeft > inorderRight:
                return None
            node = TreeNode(preorder[preorderLeft])
            offset = hashMap[preorder[preorderLeft]] - inorderLeft  # Length of the left subtree
            node.left = helper(preorderLeft + 1, preorderLeft + offset, inorderLeft, inorderLeft + offset - 1)
            node.right = helper(preorderLeft + 1 + offset, preorderRight, inorderLeft + offset + 1, inorderRight)
            return node

        node = helper(0, len(preorder)-1, 0, len(inorder)-1)
        return node