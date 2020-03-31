
def spam(a,b,c,d):
    print(a+b+c+d)
    
    return a+b+c+d

from functools import partial

s1 = partial(spam,1) # a = 1
s1(4,5,6)
s2 = partial(spam,d=41) # d = 41
s2(4,5,6)

# partial对一个特定的参数赋了一个固定的值并返回一个全新的可调用对象
# 这个方法可以解决一些参数不兼容等等问题。