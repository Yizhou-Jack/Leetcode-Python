# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Each node either needs to pull coins from or push coins to its
left and right subtrees. By a depth first search, we calculate 
the number of coins in each subtree compared to the number of 
nodes in the subtree. The number of moves along the edge connecting
the subtree is the difference between these counts
"""

from typing import Optional

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return (0, 0)
            leftCoin, leftNode = dfs(node.left)
            rightCoin, rightNode = dfs(node.right)
            res += abs(leftCoin-leftNode)
            res += abs(rightCoin-rightNode)
            return (leftCoin+rightCoin+node.val, leftNode+rightNode+1)
        dfs(root)
        return res