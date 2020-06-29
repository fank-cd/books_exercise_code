# 写一个可以给函数添加日志功能，并接受参数以允许用户自定义日志等级

from functools import wraps
import logging

def logged(level,name=None,message=None):
    
    def decorate(func):
        logname =  name if name else func.__module__
        log = logging.getLogger(logname)
        logmesg = message if message else func.__name__
        # print(func.__name__,func.__module__)
        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmesg)
            return func(*args,**kwargs)
        
        return wrapper
    
    return decorate

@logged(logging.DEBUG)
def add(x,y):
    return x + y

add(2,3)

@logged(logging.CRITICAL,"example")
def spam():
    print("Spam!")
    
spam()


# 一个装饰器函数的调用顺序其实是这样的：

# @decorator(x,y,z)
# def func(a,b):
#     pass

# def func(a,b):
#     pass

# func = decorator(x,y,z)(func)

# 其中 decorator返回的结果必须是一个可调用对象