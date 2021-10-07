#TreeNode
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def preOrder(root):
    if root:
        return
    print(root.value)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root:
        return
    inOrder(root.left)
    print(root.value)
    inOrder(root.right)

def postOrder(root):
    if root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.value)