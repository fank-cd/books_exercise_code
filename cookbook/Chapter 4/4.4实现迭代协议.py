# 实现一个能够以深度优先的模式遍历树的节点
# Python的迭代协议要求__iter__()返回一个特殊的迭代器对象，该对象必须实现__next__()
# 方法，并使用StopIteration异常来通知迭代的完成

# (这代码我有点看不懂。)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f"Node{self._value}"
    
    def add_child(self,node):
        self._children.append(node)
    
    def __iter__(self):
        print(self,self._children)
        return iter(self._children)

    def depth_fisrt(self):
        yield self
        # print(self.__iter__())
        for c in self:
            
            yield from c.depth_fisrt()


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_fisrt():
        print(ch)
    