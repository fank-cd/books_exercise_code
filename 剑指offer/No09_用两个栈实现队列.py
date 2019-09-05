"""
用两个栈实现一个队列。队列的声明如下：请实现它的两个函数，
appendTail,和deleteHEad,分别完成在队列尾部插入节点和在队列
头部删除节点的功能

"""

# 栈：先进后出
# 队列：先进先出

# 基本思想：插入的时候往stack1中插入，
# 主要是取出的时候，如果stack1和stack2都是空，则返回空
# 如果s1不为空，但s2为空，则一直讲s1的值出栈后入s2栈
# 这样顺序就反过来了。
# 如果s2不为空，则直接出栈s2
# 我觉得还是比较巧妙，不错的


class Queue(object):
    """
    两个栈实现一个队列
    stack1作为缓冲区，enqueue都enqueue到stack1中
    dequeue从stack2 dequeue，当stack2为空再把stack1逆向倒到stack2中
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, x):
        self.stack1.append(x)

    def delete_head(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None

        if len(self.stack2) <= 0:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == "__main__":
    q = Queue()
    print(q.delete_head())
    q.append_tail(1)
    q.append_tail(2)
    q.append_tail(3)
    print(q.delete_head())
    q.append_tail(4)
    print(q.delete_head())
    print(q.delete_head())

    print(q.delete_head())
