
# 对于序列中的值是可哈希的，那么这个问题就可以使用集合和生成器解决
# 可哈希的：如果一个对象是可哈希的，那么在它的生存期内必须是不变的，它需要有一个__hash__()方法。
# 整数、浮点数、字符串、元组都是不可变的。


def dequpe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dequpe(a)))


# 如果序列中的元素是不可哈希的，那又如何呢？
# 比如元素是字典的情况

def dequpe(items, key=None):
    seen = set()
    for item in items:
        val = item if not key else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [
    {"x": 1, "y": 1},
    {"x": 1, "y": 3},
    {"x": 1, "y": 2},
    {"x": 2, "y": 4},
]


print(list(dequpe(a,key=lambda d: (d['x'],d['y'])))) # 将元素变为了元组，元组不可变可哈希

a = [
    {"x": 1, "y": 1},
    {"x": 1, "y": 3},
    {"x": 1, "y": 2},
    {"x": 2, "y": 4},
]

print(list(dequpe(a,key=lambda d: (d['x']))))
