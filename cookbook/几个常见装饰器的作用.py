from functools import partial

def add(x, y):
    return x+y

# 这里创造了一个新的函数add2，只接受一个整型参数，然后将这个参数统一加上2
add2 = partial(add, y=2)

add2(3)  # 这里将会输出5
# 这个函数是使用C而不是Python实现的，但是官方文档中给出了Python实现的代码，如下所示，大家可以进行参考：


# wraps修饰器

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


def wrapper(f):
    def wrapper_function(*args, **kwargs):
        """这个是修饰函数"""
        return f(*args, **kwargs)
    return wrapper_function
    
@wrapper
def wrapped():
    """这个是被修饰的函数"""
    print('wrapped')

print(wrapped.__doc__)  # 输出`这个是修饰函数`
print(wrapped.__name__)  # 输出`wrapper_function`
# 从上面的例子我们可以看到，我想要获取wrapped这个被修饰函数的文档字符串，但是却获取成了wrapper_function的文档字符串，
# wrapped函数的名字也变成了wrapper_function函数的名字。这是因为给wrapped添加上@wrapper
# 修饰器相当于执行了一句wrapped = wrapper(wrapped)，执行完这条语句之后，wrapped函数就变成了wrapper_function函数

# 这种情况就可以用wraps修饰器了
from functools import wraps

def wrapper(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        """这个是修饰函数"""
        return f(*args, **kwargs)
    return wrapper_function
    
@wrapper
def wrapped():
    """这个是被修饰的函数
    """
    print('wrapped')

print(wrapped.__doc__)  # 输出`这个是被修饰的函数`
print(wrapped.__name__)  # 输出`wrapped`
# 我想大家应该明白wraps这个修饰器的作用了吧，就是将 被修饰的函数(wrapped) 的一些属性值赋值给 修饰器函数(wrapper) ，
# 最终让属性的显示更符合我们的直觉。