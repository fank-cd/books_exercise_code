# @Time : 2019/12/5 12:08
# @Function : 用作协程的生成器的基本行为


# 示例16-1
def simple_coroutine():
    print("->coroutine started")
    x = yield
    print("->coroutine received:", x)


# 示例16-1
my_coro = simple_coroutine()
print(type(my_coro))
# next(my_coro)
# my_coro.send(None)

my_coro.send(42)

