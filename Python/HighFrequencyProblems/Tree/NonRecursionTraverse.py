#TreeNode
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树非递归前序遍历
def preOrder(root):
    if not root:
        return None
    nodeList = []
    p = root
    res = []
    while p or len(nodeList):
        # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
        while p:
            nodeList.append(p)
            res.append(p.val)
            p = p.left
        # 开始出栈
        if len(nodeList):
            p = nodeList[-1]
            nodeList.pop()
            p = p.right
    return res


# 二叉树非递归中序遍历
def inOrder(root):
    nodeList = []
    p = root
    res = []
    while p or len(nodeList) != 0:
        # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
        while p:
            nodeList.append(p)
            p = p.left
        # 开始出栈
        if len(nodeList):
            p = nodeList[-1]
            nodeList.pop()
            res.append(p.val)
            # 进入右子树
            p = p.right
    return res


# 二叉树非递归后序序遍历
def postOrder(root):
    if not root:
        return None
    nodeList = []
    p = root
    pLast = None
    res = []
    # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
    while p:
        nodeList.append(p)
        p = p.left
    # 开始出栈
    while len(nodeList):
        p = nodeList[-1]
        nodeList.pop()
        # 若无右子树或者右子树被访问，则访问该节点
        if not p.right or p.right == pLast:
            res.append(p.val)
            pLast = p
        else:
            # 节点再次入栈
            nodeList.append(p)
            p = p.right
            while p:
                nodeList.append(p)
                p = p.left
    return res