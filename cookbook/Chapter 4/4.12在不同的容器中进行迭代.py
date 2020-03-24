# 比如有列表a和元组b，你需要遍历a后接着遍历b
# 可以用itertools 的 chain方法

from itertools import chain

a = [1, 2, 3, 4]
b = ("a", "b", "c", "d")
for x in chain(a, b):
    print(x)

# 这样会比a+b更好，理由是a+b会生成一个新的序列，而且要求a和b的类型相同 
