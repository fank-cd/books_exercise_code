# 反向迭代只有在待处理的对象拥有可确定的大小、
# 或者迭代的对象实现了__reversed__()特殊方法时才可以奏效
# 如果无法满足，则必须转为列表才可以

# a = [1,2,3,4]
# for x in reversed(a):
#   print(x)
#

# Tips： 但是转为列表会消耗非常大的内存，实际上我们
# 可以自己实现这个方法

class Countdown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n 
            n -= 1
    def __reversed__(self): # 不实现这个方法，是不能对这个对象使用reversed方法的
        n = 1
        while n <= self.start:
            yield n 
            n += 1

if __name__ == "__main__":
    countdown  = Countdown(5)

    for i in countdown:
        print(i)
    for i in reversed(countdown):
        print(i)