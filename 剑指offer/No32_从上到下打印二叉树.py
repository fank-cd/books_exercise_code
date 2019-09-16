# 面试题32：从上到下打印二叉树
# 题目1：不分行从上到下打印二叉树
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
# 例如，如图的二叉树，依次打印出8,6,10,5,7,9,11。二叉树节点的
# 定义如下：
# struct BinaryTreeNode
# {
#     int m_nValue;
#     BinaryTreeNode* m_pLeft;
#     BinaryTreeNode* m_pRight;
# }
#     8
#  /    \
#  6    10
#  /\  /\
# 5 7 9 11

# 思路 让放根节点进列表，弹出后，然后依次放入左右节点。
# 然后打印
# 重点是要拿一个列表来存，先进先出的思想


class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def print_tree_from_top_to_bottom1(root):
    """
    题目一： 不分行从上倒下打印二叉树
    """
    if root is None:
        return

    assert isinstance(root, TreeNode)
    l = []
    l.append(root)

    while len(l):
        node = l.pop(0)
        if node.left_child:
            l.append(node.left_child)

        if node.right_child:
            l.append(node.right_child)

        print(node.value, end=' ')

# 题目二：分行从上到下打印二叉树
# 思路 需要两个变量，一个变量表示在当前层中还没有打印的节点数；另一个表示
# 下一层节点的数目


def print_tree_from_top_to_bottom2(root):
    """
    题目二： 分行从上到下打印二叉树
    """
    if root is None:
        return
    assert isinstance(root, TreeNode)

    l = []
    l.append(root)

    n_node = 1  # 当前层中还没有打印的节点数
    next_n_node = 0  # 下一层节点的数目
    while len(l):
        node = l.pop(0)
        print(node.value, end=' ')

        if node.left_child:
            next_n_node += 1
            l.append(node.left_child)

        if node.right_child:
            next_n_node += 1 # 存在下一层节点，节点数+1
            l.append(node.right_child)

        n_node -= 1 # 已经打印了一个节点，当前还没有打印的节点数-1
        if n_node == 0:  # 当前层节点已经打印完
            print()
            n_node = next_n_node  # 跨入下一层
            next_n_node = 0



if __name__ == "__main__":
    node7 = TreeNode(11)
    node6 = TreeNode(9)
    node5 = TreeNode(7)
    node4 = TreeNode(5)
    node3 = TreeNode(10, left_child=node6, right_child=node7)
    node2 = TreeNode(6, left_child=node4, right_child=node5)
    node1 = TreeNode(8, left_child=node2, right_child=node3)
    root = node1
    print_tree_from_top_to_bottom2(root)
