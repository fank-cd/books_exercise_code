# @Time : 2019/12/5 17:40
# @Function : 示例16-16


# 使用yield from 链接可迭代的对象
def chain(*iterables):
    for it in iterables:
        yield from it


if __name__ == '__main__':
    s = "ABC"
    t = tuple(range(3))
    l = list(chain(s, t))
    print(l)
