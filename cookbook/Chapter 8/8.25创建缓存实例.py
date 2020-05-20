# 当创建类实例时我们想返回一个缓存引用，让其指向上一个用同样参数（如果有的话）创建出来的实例
# ps：就是如果实例初始化的参数相同，那就让他们指向同一个对象


# 比如在logging模块中，就有这一个功能的实现
# import logging
# a = logging.getLogger("foo")
# b = logging.getLogger("bar")

# a is b  # Flase

# c = logging.getLogger("foo")

# a is c # True
# 可以看出a与c都给的同一参数foo，这时候并没有新建一个实例，而是将a与c指向同一个对象

# 我们可以用另一个工厂函数来实现这一功能
# 工厂函数：个人理解是在‘ 工厂’里组装‘部件’的函数，比如这里是在get_spam中去组装SPam类

# import weakref  # 弱引用


# class Spam:
#     def __init__(self, name):
#         self.name = name


# _spam_cache = weakref.WeakValueDictionary()


# def get_spam(name):
#     if name not in _spam_cache:
#         s = Spam(name)
#         _spam_cache[name] = s
#     else:
#         s = _spam_cache[name]

#     return s

# 使用工厂函数的方法非常简单，但是我们还有其他方法
# 比如重新定义类的__new__()方法

# import weakref


# class Spam():
#     _spam_cache = weakref.WeakValueDictionary()
#     def __new__(cls, name):
#         if name in  cls._spam_cache:
#             return cls._spam_cache[name]

#         else:
#             self = super().__new__(cls)
#             cls._spam_cache[name] = self
#             return self

#     def __init__(self, name):
#         print("Init Spam")
#         self.name = name

# 以上代码的问题在于，每次新建实例的时候都会去初始化，这样也不符合我们定义。
# 这里的弱引用与垃圾回收有极为重要的关系
# 而值得一提的是，这里的WeakValueDictionary 会保存着那些被引用的对象，只要他们存在于程序中的某处即可。
# 否则当实例不再被使用时，字典的键就会消失。

# 还有一些更加高级的技术实现，比如：
import weakref


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]

        return s

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spam(self, name):
        return Spam.manager.get_spam(name)

# 这样就很好了，上面的Manager类也可以用于其他的类，为潜在的灵活性提供更多支持
# 唯一的问题是需要防止其他 程序员直接调用Spam类，这里就在SPam前面加一个_就足够提醒了
# 不用再将代码变得更复杂了
