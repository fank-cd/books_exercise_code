# coding:utf-8
from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
# 随机生成3-6次的2-5的随机数
remaining = CleanOutputSet()


def loop(nesc):
    myname = currentThread().name

    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname))
    lock.release()
    sleep(nesc)
    lock.acquire()
    remaining.remove(myname)
    print("[%s] Completed %s (%d sec)" % (ctime(), myname, nesc))
    lock.release()
    print("     (remaining: %s)" % (remaining or None))
    """
    使用上下文管理器
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    sleep(nesc)
    with lock:
        remaining.remove(myname)
        print("[%s] Completed %s (%d sec)" % (ctime(), myname, nesc))
        print("     (remaining: %s)" % (remaining or None))
    """


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print("ALL DONE at %s", ctime())


if __name__ == '__main__':
    _main()