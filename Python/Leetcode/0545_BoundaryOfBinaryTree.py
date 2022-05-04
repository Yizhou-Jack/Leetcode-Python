# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root):
        if root is None:
            return []

        def findLeftBoundary(node):
            res = []
            while node:
                res.append(node.val)
                if node.left:
                    node = node.left
                elif node.right:
                    node = node.right
                else:
                    break
            return res

        def findRightBoundary(node):
            res = []
            while node:
                res.append(node.val)
                if node.right:
                    node = node.right
                elif node.left:
                    node = node.left
                else:
                    break
            return res

        def findLeaves(root):
            stack = [root]
            res = []
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return res

        leftBoundary = findLeftBoundary(root.left)
        rightBoundary = findRightBoundary(root.right)
        leaves = findLeaves(root)
        if leftBoundary and leaves and leftBoundary[-1] == leaves[0]:
            leaves = leaves[1:]
        if rightBoundary and leaves and rightBoundary[-1] == leaves[-1]:
            leaves = leaves[:-1]
        return [root.val] + leftBoundary + leaves + rightBoundary[::-1]
