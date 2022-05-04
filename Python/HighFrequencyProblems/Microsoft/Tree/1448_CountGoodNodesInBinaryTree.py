# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def helper(node, maxValue):
            nonlocal res
            if node is None:
                return
            if node.val >= maxValue:
                res += 1
            maxValue = max(maxValue, node.val)
            helper(node.right, maxValue)
            helper(node.left, maxValue)
        helper(root, float("-inf"))
        return res