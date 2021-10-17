"""
Construct Binary Search Tree from Preorder Traversal
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(i, j, node):
            nonlocal preorder
            if i >= j:
                return
            si = -1
            siFlag = True
            bi = -1
            biFlag = True
            for k in range(i, j):
                if siFlag and preorder[k] < preorder[i]:
                    si = k
                    siFlag = False
                if biFlag and preorder[k] > preorder[i]:
                    bi = k
                    biFlag = False
            if si > 0 and bi > 0:
                node.left = TreeNode(preorder[si])
                node.right = TreeNode(preorder[bi])
                helper(si, bi, node.left)
                helper(bi, j, node.right)
            elif si > 0 and bi == -1:
                node.left = TreeNode(preorder[si])
                node.right = None
                helper(si, j, node.left)
            elif si == -1 and bi > 0:
                node.left = None
                node.right = TreeNode(preorder[bi])
                helper(bi, j, node.right)
            else:
                return
        root = TreeNode(preorder[0])
        helper(0, len(preorder), root)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        dic = {val: i for i, val in enumerate(inorder)}
        def bst(l, r):
            if l >= r:
                return
            val = preorder.pop(0)
            ind = dic[val]
            root = TreeNode(val)
            root.left = bst(l, ind)
            root.right = bst(ind + 1, r)
            return root
        return bst(0, len(inorder))