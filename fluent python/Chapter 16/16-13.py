# @Time : 2019/12/5 16:41
# @Function : details
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        print(exc)
        result = exc.value

    print(result)
# 获取协程的返回值虽然要绕个圈子，但这是PEP 380 定义的方式，当我们意识到这一点之
# 后就说得通了：yield from 结构会在内部自动捕获StopIteration 异常
# 自我吐槽：就很搞笑这个东西，不优雅
