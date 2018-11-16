# coding:utf-8

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
# 建立锁对象
MAX = 5
candytray = BoundedSemaphore(MAX)
# BoundedSemaphore 信号量类，MAX 初始值
# 分配资源时，其值减1。MAX，表示计数器的值永远不会超过MAX

# randrange(a,b) 随机生成a-b范围内的随机数 左闭右开（可以等于左边，不能等于右边)


def refill():
    lock.acquire()
    print("Refilling candy..."),
    try:
        candytray.release()
    except ValueError:
        print("full,skipping")
    else:
        print("OK")
    lock.release()


def buy():
    lock.acquire()
    print("Buying candy.."),
    if candytray.acquire(False):  # False 设置为非阻塞模式，如果当前信号量为空，则为一直阻塞至有资源释放。
        print("OK")  # 这里如果为空就直接打印empty，不再等待
    else:
        print("empty, skipping")
    lock.release()


def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    # print loops
    for i in xrange(loops):  # 循环几次，即消费几次
        buy()
        sleep(randrange(3))


def _main():
    print("starting at:", ctime())
    nloops = randrange(2, 6)
    print("THE CANDY MACHINE(full with %d bars)" % MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()  # buy
    Thread(target=producer, args=(nloops,)).start()


@register
def _atexit():
    print("ALL DONE at", ctime())


if __name__ == '__main__':
    _main()
