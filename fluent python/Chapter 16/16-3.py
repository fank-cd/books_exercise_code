# @Time : 2019/12/5 15:02
# @Function : 16.3示例


# 16.3示例

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        # 这个无限循环表明，只要调用方不断把值发给这个协程，它就会一直
        # 接受值，然后生成结果。仅当调用方在协程上调用.close()方法，
        # 或者没有对协程的引用而被垃圾回收程序回收时，这个协程才会终止。

        term = yield average
        total += term
        count += 1
        average = total / count
        # print(average)

        # 使用协程的好处是，total 和count 声明为局部变量即可，
        # 无需使用实例属性或闭包在多次调用之间保持上下文


if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg)  # 预先激活
    coro_avg.send(23)
    coro_avg.send(2)
    coro_avg.send(3)
    coro_avg.send(223)
    coro_avg.send(213)
    coro_avg.close()
