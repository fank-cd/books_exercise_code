# coding:utf-8
# 调用一个Thread实例，传给他一个函数
import threading
from time import ctime, sleep

loops = [4.2]


def loop(nloop,nsec):
    """
    :param nloop: loop函数的序列号，如loop0 ,loop1
    :param nsec:  sleep的秒数
    :return:
    """
    print("start loop ", nloop, "at:", ctime())
    sleep(nsec)
    print("loop", nloop, "done at:", ctime())


def main():
    print "startting at:", ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
        # 这个循环创建Thread实例，加入threads队列

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
        # 直至启动的线程终止之前一直被挂起，除非给出了timeout,否则会一直阻塞
    print("ALL DONE at:", ctime())


if __name__ == '__main__':
    main()