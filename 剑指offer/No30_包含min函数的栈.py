# No30_包含min函数的栈
# 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小
# 元素的min函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)

# 思路：用一个辅助栈来存最小值，以及次小值。


# class Stack():
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def peek_min(self):
#         if not self.min_stack:
#             return None
#         return self.min_stack[-1]

#     def push(self, obj):
#         assert isinstance(obj, (int, float))
#         self.stack.append(obj)

#         if not self.min_stack:
#             self.min_stack.append(obj)
#         else:
#             self.min_stack.append(obj if obj <= self.peek_min() else self.peek_min())

#     def pop(self):
#         if not self.stack or not self.min_stack:
#             return None
#         self.min_stack.pop()
#         return self.stack.pop()

# if __name__ == "__main__":
#     s = Stack()
#     s.push(2.98)
#     s.push(3)
#     print(s.stack)
#     print(s.min_stack)
#     print(s.peek_min())
#     s.pop()
#     print(s.stack)
#     print(s.peek_min())
#     s.push(1)
#     print(s.stack)
#     print(s.peek_min())
#     s.pop()
#     print(s.stack)
#     print(s.peek_min())

class StackWithMin(object):
    def __init__(self):
        self.real_stack = []
        self.min_stack = []

    def push(self, obj):
        assert isinstance(obj, (int, float))
        self.real_stack.append(obj)

        if not self.min_stack:
            self.min_stack.append(obj)
        else:

            self.min_stack.append(obj if obj < self.min_stack[-1] else self.min_stack[-1])

    def pop(self):
        if not self.real_stack or not self.min_stack:
            return None

        self.min_stack.pop()
        return self.real_stack.pop()

    def min(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]


if __name__ == "__main__":
    s = StackWithMin()
    s.push(2.98)
    s.push(3)
    print(s.real_stack)
    print(s.min_stack)
    print(s.min())
    s.pop()
    s.pop()
    print(s.real_stack)
    print(s.min())
    s.push(1)
    print(s.real_stack)
    print(s.min())
    s.pop()
    print(s.real_stack)
    print(s.min())