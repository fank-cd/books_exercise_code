# @Time : 2019/12/5 15:02
# @Function : 示例16-2

# 四个状态
# GEN_CREATGED 等待开始执行
# GEN_RUNNING 解释器正在执行
# GEN_SUSENDED 在yield表达式处暂停
# GEN_CLOSED 执行结束
#
# 示例16-2 产出两个值的协程
from inspect import getgeneratorstate


def simple_coro2(a):
    print("->Started:a=", a)
    b = yield a
    print("->Received:b = ", b)
    c = yield a + b
    print("->Received:c = ", c)


my_coro2 = simple_coro2(14)

print(getgeneratorstate(my_coro2))
a = next(my_coro2)
print(getgeneratorstate(my_coro2))
my_coro2.send(28)
my_coro2.send(99)

for i in simple_coro2(14):
    print(i)

