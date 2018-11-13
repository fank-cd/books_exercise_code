# coding:utf-8
# 派生thread的子类，并创建子类实例
import threading
from time import ctime, sleep

loops = [4, 2]

# MyThread就是threading的子类，继承了了threading.Thread和他的属性，重写了run
class MyThread(threading.Thread):
    def __init__(self,func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at', ctime())


def main():
    print "starting at:", ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # 这里实例化的是Thread的子类的实例，而不是Thread的实例化
        t = MyThread(loop, (i, loops[i]),
                    loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    print("ALL DONE at:", ctime())

if __name__ == '__main__':
    main()