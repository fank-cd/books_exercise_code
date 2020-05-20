# 我们想在访问实例的属性时能将将其委托（delegate）到一个内部持有的对象上。
# 这可以作为继承的替代方案或者是为了实现一种代理机制


# 最简单的委托看起来是这样的

class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to th internal self._a instance
        return self._a.foo()

    def bar(self):
        pass


# 如果有许多方法都需要委托，另一种实现方式是__getattr__()方法,

class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, name):
        return getattr(self._a, name)

# __getattr__()方法能用来查找所有的属性。如果代码中尝试访问一个不存在的属性
# 就会调用这个方法

# 需要重点强调的是，__getattr__方法通常不适用于大部分名称以双下线开头和结尾的特殊方法。