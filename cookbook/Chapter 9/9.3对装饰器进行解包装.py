# 首先在明确了 装饰器函数的内函数中 使用了 @wraps的 情况下
# 一般来说我们可以通过访问__wrapped__属性来获取对原始数据的访问

# 例如 ：
# 

@somedecorator
def add(x,y):
    return x + y

orig_add = add.__wrapped__
res = orig_add(3,4)  # output 7

# 需要注意的是，如果有多个装饰器已经作用于某个函数上了，那么__wrapped__属性
# 的行为目前是为定义的，应该避免这种情况。