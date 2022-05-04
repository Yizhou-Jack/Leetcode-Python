# Definition for a binary tree node with parent
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def inorderSuccessorInBSTII(self, p: TreeNode) -> TreeNode:
        if p is None:
            return None
        if p.right is not None:
            p = p.right
            while p.left is not None:
                p = p.left
            return p
        while p.parent is not None:
            if p.parent.left == p:
                return p.parent
            p = p.parent
        return None