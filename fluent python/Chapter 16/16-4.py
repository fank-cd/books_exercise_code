# @Time : 2019/12/5 15:10
# @Function : 示例16-4 预激协程的装饰器

from functools import wraps


def coroutine(func):
    """装饰器：向前执行到一个‘yield’表达式，预激‘func’"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
        print(average)

if __name__ == '__main__':
    coro_avg = averager()
    from inspect import getgeneratorstate
    getgeneratorstate(coro_avg)
    coro_avg.send(10)
    coro_avg.send(20)

"""
使用yield from 句法（参见16.7 节）调用协程时，会自动预激，因此与示例16-5 中的
@coroutine 等装饰器不兼容。Python 3.4 标准库里的asyncio.coroutine 装饰器
不会预激协程，因此能兼容yield from 句法。
"""
