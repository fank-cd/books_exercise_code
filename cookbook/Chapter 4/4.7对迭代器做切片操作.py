import itertools

# 普通情况下迭代器是不能做切片操作的，但是可以用itertools实现
# 需要强调的是，islice()方法会消耗掉锁提供的迭代器的数据，也就是说之前的数据就被丢弃了

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
for x in itertools.islice(c,10,20):
    print(x)