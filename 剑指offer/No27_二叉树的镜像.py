# 面试题27：二叉树的镜像
# 题目：请完成一个函数，输入一棵二叉树，该函数输出它的镜像。二叉树节点的定义
# 如下
# struct BinaryTreeNode
# {
#     int m_nValue;
#     BinaryTreeNode* m_pLeft;
#     BinaryTreeNode* m_pRight;
# }


class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def MirrorRecursively(root):
    if not root:
        return None
    if not root.left and not root.right:
        return root 
    root.left,root.right = root.right, root.left

    if root.left:
        MirrorRecursively(root.left)
    if root.right:
        MirrorRecursively(root.right)



def print_tree(root):
    if root is None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

if __name__ == "__main__":
    node7 = TreeNode(val=11)
    node6 = TreeNode(val=9)
    node5 = TreeNode(val=7)
    node4 = TreeNode(val=5)
    node3 = TreeNode(val=10, left=node6, right=node7)
    node2 = TreeNode(val=6, left=node4, right=node5)
    node1 = TreeNode(val=8, left=node2, right=node3)
    root = node1
    print_tree(root)
    print()
    MirrorRecursively(root)
    print_tree(root)