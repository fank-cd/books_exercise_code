"""
前序遍历：根，左，右
中序遍历：左，根，右
后序遍历：左，右，根

广搜：一层一层遍历下去
深搜：###
"""

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，输入前序遍历序列｛1,2,4,7,3,5,6,8｝和中序遍历
{3,7,2,1,5,3,8,6},则重建二叉树并输出它的头结点。


这个代码比较有意思，根据前序和中序可以确定根节点和左右子树，然后一直递归就可以了
（但我递归一直学的不太好，而且前中序遍历理解得不深，我需要再去看看二叉树）
"""


class TreeNode():
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def create_tree(pre_order, in_order):
    if not isinstance(pre_order, list) or not isinstance(in_order, list) \
        or len(pre_order) != len(in_order):
        return False

    for x, y in zip(pre_order, in_order):
        if not isinstance(x, int) or not isinstance(y, int):
            return False


    pre_order_set=set(pre_order)
    in_order_set=set(in_order)

    if pre_order_set != in_order_set or len(pre_order_set) != len(pre_order) or \
        len(in_order_set) != len(in_order):
        return False

    root=create_tree_recursively(pre_order=pre_order, in_order=in_order)
    return root

def create_tree_recursively(pre_order, in_order):
    if len(pre_order) == 0:
        return None

    root=TreeNode(pre_order[0])
    root_index=in_order.index(pre_order[0])

    root.left_child=create_tree_recursively(pre_order=pre_order[1:root_index+1],\
    in_order=in_order[:root_index]
    )
    root.right_child = create_tree_recursively(pre_order=pre_order[root_index + 1:],
                                               in_order=in_order[root_index + 1:])

    return root


def print_level(node, position_name):
    if node is None:
        return
    print_level(node.left_child, "left")
    print_level(node.right_child, "right")
    print()
    print(position_name, " ", node.data, end=' ')


if __name__ == "__main__":
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    root = create_tree(preorder, inorder)
    print_level(root, "root")