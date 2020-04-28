class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Except a string")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")
# property 是python内置的装饰器，可以把类中的一个函数变成一个属性，
# 使用property后就会生成 setter 和deleter。一个是用来设置值的，另一个是删除的
# 他们可以根据场景不同来自由变化


if __name__ == '__main__': 
    p = Person("fank")
    print(p.first_name)  # fank
    print(p._first_name)  # fank
    print(p.first_name is p._first_name)  # True
    p.first_name = 123  # Type Error
    p = Person(123)  # Type Error

    """
    可以看出虽然init方法中不是_first_name 而我们返回 设置都是对_first_name 进行操作
    但实际上创建实例的时候 仍然调用的setter方法，因此会跳过self.firt_name 去访问self._first_name
    在这个例子中，对实例设置属性时进行类型检查 就是 property的全部意义
    """
