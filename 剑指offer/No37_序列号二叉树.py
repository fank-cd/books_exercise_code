# 题目：请实现两个函数，分别用来序列化和反序列化二叉树

# 通过题目7可知，我们可以从前序遍历和中序遍历构造一棵二叉树
# 所以我们可以先把一棵二叉树序列化成一个前序遍历和中序遍历序列
# 然后反序列化的时候根据序列重构二叉树

# 此思路缺点：要求二叉树中不能有数值重复的节点，二是只有当
# 两个序列中所有数据都读出后才能开始反序列化。如果两个
# 遍历序列的数据是从一个流里读出来的，那么可能需要等待较长的
# 时间

# 实际上，如果二叉树的序列化是从根节点开始的，那么相应的
# 反序列化再根节点的数值读出来的时候就可以开始了。因此，我们可以
# 根据前序遍历的顺序来序列化二叉树，因为前序遍历是从根节点开始的
# 在遍历二叉树碰到nullptr指针时，这些nullptr指针序列化为一个特殊
# 的字符，如（'$'）。另外，节点的数值之间要用一个特殊字符如（','）
# 隔开


    #     1
    #    / \
    #   2   3
    #  /   / \
    # 4    5  6

import sys
from queue import Queue


class TreeNode(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def serialize(root):
    if root is None:
        return

    sys.stdout.write(str(root.value))
    if root.left_child:
        serialize(root.left_child)
    else:
        sys.stdout.write('$')

    if root.right_child:
        serialize(root.right_child)
    else:
        sys.stdout.write('$')


def deserialize(list_of_char):
    if not isinstance(list_of_char, list) or len(list_of_char) == 0:
        return

    if list_of_char[0] == '$':
        node = None
    else:
        node = TreeNode(int(list_of_char[0]))
    list_of_char.pop(0)
    if node:
        node.left_child = deserialize(list_of_char)
        node.right_child = deserialize(list_of_char)
    return node


def print_tree_from_top_to_bottom2(root):
    """
    题目二： 分行从上到下打印二叉树
    """
    if root is None:
        return
    assert isinstance(root, TreeNode)

    node_queue = Queue()
    node_queue.put(root)
    n_node = 1
    next_n_node = 0
    while not node_queue.empty():
        node = node_queue.get()
        print(node.value, end=' ')

        if node.left_child:
            next_n_node += 1
            node_queue.put(node.left_child)

        if node.right_child:
            next_n_node += 1
            node_queue.put(node.right_child)

        n_node -= 1
        if n_node == 0:
            print()
            n_node = next_n_node
            next_n_node = 0


if __name__ == "__main__":
    node6 = TreeNode(6)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node5, node6)
    node2 = TreeNode(2, node4)
    node1 = TreeNode(1, node2, node3)
    root = node1
    serialize(root)
    print()
    new_root = deserialize(['1','2','4','$','$','$','3','5','$','$','6','$','$'])
    print_tree_from_top_to_bottom2(new_root)