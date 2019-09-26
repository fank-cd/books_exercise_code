# 题目：输入一个整数数组，判断该数组是不是某二叉搜索
# 树的后序遍历结果。如果是则返回true，否则返回false。
# 假设输入的数组的任意两个数字都不相同。
# 后续遍历：左右根

# 思路：最后一位是根节点，比根节点小的是左子树，大的是右子树

def verify_sequence_of_BST(sequence):
    if not isinstance(sequence, list) or len(sequence) == 0:
        return False

    root = sequence[-1] #  根节点
    for index, element in enumerate(sequence):  # 左子树
        i = index
        if element > root:
            break

    for element in sequence[i:]:  # 判断右子树是否符合条件 即右子树大于根节点
        if element < root:
            return False

    left = True
    if i > 0:
        left = verify_sequence_of_BST(sequence[:i])

    right = True
    if i < len(sequence) - 1:
        right = verify_sequence_of_BST(sequence[i:-1])

    return left and right


if __name__ == "__main__":
    print(verify_sequence_of_BST([5, 7, 6, 9, 11, 10, 8]))
    print(verify_sequence_of_BST([7, 4, 6, 5]))