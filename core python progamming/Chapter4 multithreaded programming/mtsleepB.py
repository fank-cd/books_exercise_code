# coding:utf-8
# 使用线程和锁,书上这段代码有问题。。我也看球不懂 让看threading模块，那就先不管这个咯

import thread
from time import ctime,sleep

loops = [4, 2]


def loop(nloop, nsec, lock):
    print("start loop", nloop, "at:", ctime())
    sleep(nsec)
    print("loop", nloop, "done at:", ctime())


def main():
    print("starting at:", ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():pass

    print "all done at:", ctime()

if __name__ == '__main__':
    main()