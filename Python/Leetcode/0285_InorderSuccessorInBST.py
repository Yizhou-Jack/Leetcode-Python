"""
if p >= root, the successor will be root's right node subtree's left most node
so we go to right node to find the target successor
if p < root, the successor will be its closest parent which p in its left subtree
so if root.left is None -> successor should be root
if not, we go to left node to find the target successor
"""

class Solution:
    def inorderSuccessor(self, root, p):
        if root is None or p is None:
            return None
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            if self.inorderSuccessor(root.left, p) is None:
                return root
            else:
                return self.inorderSuccessor(root.left, p)