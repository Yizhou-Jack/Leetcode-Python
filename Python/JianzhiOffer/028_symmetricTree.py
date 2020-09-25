# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(leftNode, rightNode):
            if not leftNode and not rightNode: return True
            if not leftNode or not rightNode or leftNode.val != rightNode.val: return False
            return helper(leftNode.left, rightNode.right) and helper(leftNode.right, rightNode.left)

        if not root: return True
        res = helper(root.left, root.right)
        return res