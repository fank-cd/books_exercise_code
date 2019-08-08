from collections import OrderedDict

d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4

for key,value in d.items():
    print(key,value)
"""
OrderedDict内部维护了一个双向链表，会根据加入顺序来排列键的位置。
第一个新加入的元素被放置在链表的末尾，对已经存在的键重新赋值不影响顺序。

注意：OrderedDIct的大小是普通字典的两倍多
"""