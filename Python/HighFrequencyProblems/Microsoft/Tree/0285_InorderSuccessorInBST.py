"""
if p >= root, the successor will be root's right node subtree's left most node
so we go to right node to find the target successor
if p < root, the successor will be its closest parent which p in its left subtree
so if root.left is None -> successor should be root
if not, we go to left node to find the target successor

If the node has a right child, and hence its successor is somewhere lower in the tree.
Go to the right once and then as many times to the left as you could. Return the node you end up with.
If the node has no right child, and hence its successor is somewhere upper in the tree.
Go up till the node that is left child of its parent. The answer is the parent.
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