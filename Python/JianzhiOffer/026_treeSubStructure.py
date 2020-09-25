# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None: return False

        def helper(ANode, BNode):
            if not BNode:
                return True
            elif not ANode:
                return False
            if ANode.val == BNode.val:
                res1 = helper(ANode.left, BNode.left)
                res2 = helper(ANode.right, BNode.right)
                return res1 and res2
            else:
                return False

        nodeList = []
        p = A
        while p or len(nodeList):
            while p:
                nodeList.append(p)
                if p.val == B.val:
                    res = helper(p, B)
                    if res: return res
                p = p.left
            if len(nodeList):
                p = nodeList[-1]
                nodeList.pop()
                p = p.right
        return False