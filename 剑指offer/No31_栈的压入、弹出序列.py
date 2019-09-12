# No31_栈的压入、弹出序列
# 题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第
# 二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如，序列｛1，2，3，4，5｝是某栈的压入顺序，序列｛4，5，3，2，1｝是该
# 压栈序列对应的一个弹出序列，但｛4，3，5，1，2｝

def is_pop_order(push_order, pop_order):
    # 出栈顺序和进栈顺序长度一致， 包含的元素一致， 且都没有重复元素
    assert isinstance(push_order, list) and isinstance(pop_order, list) and \
        len(push_order) == len(pop_order) and set(push_order) == set(pop_order) and \
        len(push_order) == len(set(push_order))

    if len(push_order) == 0:
        return False

    stack = []
    push_index = 0
    pop_index = 0
    while pop_index < len(pop_order):
        while not stack or stack[-1] != pop_order[pop_index]:
            if push_index >= len(push_order):
                break
            stack.append(push_order[push_index])
            push_index += 1

        if stack[-1] != pop_order[pop_index]:
            return False

        stack.pop()
        pop_index += 1

    if pop_index == len(pop_order) and len(stack) == 0:
        return True

    return False


if __name__ == "__main__":
    print(is_pop_order([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(is_pop_order([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))