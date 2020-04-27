# 可以写一个基类来实现这个过程


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:  # 可变参数之后的就是关键词参数
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError("Invalid arguments(s):{}".format(",".join(kwargs)))


if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']
    s = Stock("ACME", "14", "54")
    p = Point(14, 33)
    s = Stock("ACME", "14",price=22)


# 这样就不必写一个Stock类就写一个init 写一个Point类又写一个init 