# 有一个嵌套型的数据，怎么处理成扁平的或者用一次遍历来完成呢？
from collections import Iterable

def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1,2,3,[4,5],[6,7,8,9,],[1,2,3,[4,5]]]

for x in flatten(items):
    print(x)

# 如果不这样的话，那么就会编写两层嵌套的代码，虽然只改变了一点点，但是代码更加清晰了
# 而且如果两层以上了，就要继续嵌套for循环。。。这点真的很丑陋