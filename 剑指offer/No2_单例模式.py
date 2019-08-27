
# 单例模式即指一个类只有一个实例的设计模式
# 实话是单例模式看不太懂，需要一些很神奇的知识。比如 type，metaclass，new之类的
# 试用函数装饰器实现
# 类地址为键，实例为值

def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()

        return _instance[cls]

    return inner

@singleton
class Cls():
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()

print(cls1==cls2)

# 类装饰器
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

@Singleton
class Cls2(object):
    def __init__(self):
        pass

cls1 = Cls2()
cls2 = Cls2()
print(id(cls1) == id(cls2))

# 试用new关键字实现

class Single(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    def __init__(self):
        pass


single1 = Single()
single2 = Single()
print(id(single1) == id(single2))

# 使用 metaclass 实现单例模式
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Cls4(metaclass=Singleton):
    pass

cls1 = Cls4()
cls2 = Cls4()
print(id(cls1) == id(cls2))