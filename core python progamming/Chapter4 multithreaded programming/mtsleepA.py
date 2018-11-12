# coding:utf-8
# 两个循环并发执行，运行的时间只和最慢的线程相关，而不是两个线程相加。
import thread
from time import ctime,sleep


def loop0():
    print 'start loop 0 at', ctime()
    sleep(4)
    print "loop 0 done at ", ctime()


def loop1():
    print("start loop 1 at "), ctime()
    sleep(2)
    print("loop1 done at "), ctime()


def main():
    print "starting at", ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print("all Done at"), ctime()


if __name__ == '__main__':
    main()