import heapq

# 实现优先级队列
class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue,(-priority,self._index, item))
        self._index += 1

    def pop(self):  # 这代码应该是有问题的，如果为空应该是不能取[-1]的
        return heapq.heappop(self._queue)[-1]

class Item():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r}):".format(self.name)

q = PriorityQueue()

q.push(Item("foo"), 1)
q.push(Item("bar"), 5)
q.push(Item("spam"), 4)
q.push(Item("grok"), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())


# 堆是一种特殊的树形数据结构，每个节点都有一个值，通常我们所说的堆的数据结构指的是二叉树。
# 堆的特点是根节点的值最大（或者最小），而且根节点的两个孩子也能与孩子节点组成子树，亦然称之为堆。
# 堆分为两种，大根堆和小根堆是一颗每一个节点的键值都不小于（大于）其孩子节点的键值的树。
# 无论是大根堆还是小根堆（前提是二叉堆）都可以看成是一颗完全二叉树。
# 在Python中也对堆这种数据结构进行了模块化，我们可以通过调用heapq模块来建立堆这种数据结构，
# 同时heapq模块也提供了相应的方法来对堆做操作。
# 有兴趣的朋友可以直接导入heapq模块来查看它提供了哪些方法。在这里我们简单的来介绍一下。

# heap = [] #创建了一个空堆
# heappush(heap,item) #往堆中插入一条新的值
# item = heappop(heap) #从堆中弹出最小值
# item = heap[0] #查看堆中最小值，不弹出
# heapify(x) #以线性时间讲一个列表转化为堆
# item = heapreplace(heap,item) #弹出并返回最小值，
# # 然后将heapqreplace方法中item的值插入到堆中，堆的整体结构不会发生改变。
# 这里需要考虑到的情况就是如果弹出的值大于item的时候我们可能就需要添加条件来满足function的要求
