import time
from threading import Thread


def countdoen(n):
    while n >0:
        print("T-minus",n)
        n -= 1
        time.sleep(5)


t = Thread(target=countdoen,args=(2,))
t.start()
t.join()
if t.is_alive():
    print("running")
else:
    print("compeleteda")