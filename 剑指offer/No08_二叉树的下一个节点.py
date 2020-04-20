r"""
给定一棵二叉树和其中的一个节点，如何找出中序遍历的下一个节点？
书中的节点除了有两个分别指向左、右节点的指针，还有一个指向父指针的节点。

       a
    /    \\
    b      c
   / \    / \\
  d   e  f   g
     / \\
    h   i

"""

"""
这个题主要就是判断各种情况，考察对中序遍历的了解程度。
众所周知，中序就是，左，根，右
其他情况都比较容易想得通，比较特殊的情况是
'如果一个节点既没有右子树，并且还是它父节点的右子节点'
这种情况，我们可以沿着指向父节点的指针一直向上遍历，直到找到一个是
它父节点的左子节点的节点。如果这样的节点存在，那么这个节点的父节点
就是我们要找的节点
"""

class TreeNode(object):
    def __init__(self, data, parent=None, left_child=None, right_child=None):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


def set_relation(parent, left_child, right_child):
    parent.left_child = left_child
    parent.right_child = right_child
    left_child.parent = parent
    right_child.parent = parent


def find_next_node_in_inordered1(node):
    """
    给定树中的一个节点，返回该节点在中序遍历中的下一个节点
    """
    if node is None:
        return None

    # 有右子树，返回右子树中的最左边的节点
    if node.right_child:
        next_node = node.right_child
        while next_node.left_child:
            next_node = next_node.left_child
        return next_node

    # 没有右子树，有父节点
    if node.parent:
        parent = node.parent

        # 节点是父节点的左子节点，返回父节点
        if id(node) == id(parent.left_child):
            return parent

        # 节点是父节点的右子节点，返回是左子节点的祖先节点的父节点
        if id(node) == id(parent.right_child):
            while parent.parent:
                if id(parent) == id(parent.parent.left_child):
                    return parent.parent
                parent = parent.parent
        # 不会出现父节点是祖先节点的右节点，理由是如果是这样，那么node就是最右的节点，在中序遍历中是不会存在下一个节点的
    return None


if __name__ == "__main__":
    node_i = TreeNode("i")
    node_h = TreeNode("h")
    node_g = TreeNode("g")
    node_f = TreeNode("f")
    node_e = TreeNode("e")
    node_d = TreeNode("d")
    node_c = TreeNode("c")
    node_b = TreeNode("b")
    node_a = TreeNode("a")
    set_relation(node_e, node_h, node_i)
    set_relation(node_c, node_f, node_g)
    set_relation(node_b, node_d, node_e)
    set_relation(node_a, node_b, node_c)

    print(find_next_node_in_inordered1(node_e).data)
