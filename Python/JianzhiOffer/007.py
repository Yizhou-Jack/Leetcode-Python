class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        hm = {}
        for i in range(len(inorder)):
            hm[inorder[i]] = i

        def treeBuilder(preRootIndex, inLeftIndex, inRightIndex):
            if inLeftIndex > inRightIndex:
                return None
            rootValue = preorder[preRootIndex]
            root = TreeNode(rootValue)
            inRootIndex = hm[rootValue]
            root.left = treeBuilder(preRootIndex+1, inLeftIndex, inRootIndex-1)
            root.right = treeBuilder(preRootIndex+inRootIndex-inLeftIndex+1, inRootIndex+1, inRightIndex)
            return root

        root = treeBuilder(0, 0, len(inorder)-1)
        return root