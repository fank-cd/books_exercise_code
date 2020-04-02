# 任何以下划线开头的名字应该总是被认为只属于内部实现的
# Python不会阻止其他人访问内部名称，但如果这样做了，则被认为是粗鲁的


# 而对于双下划线开头的
class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        print("This is a private method B")
        
# 以双下划线开头的名称会导致出现‘名称重组’。简单来说就是上面这个类的私有属性
# 会被重命名为_B__private_method
# 意义在于 这样的属性不能通过继承而覆盖 

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1
    def __private_method(self):
        print("This is a private method C")
        
if __name__ == '__main__':
    c = C()
    c._C__private_method()  # 并没有被因为继承而被覆盖
# 此外还应该指出，有时候可能想定义一个变量，但是名称可能会和保留字产生冲突
# 应该在名称最后加上一个单下划线以示区别
# 例如 lambada_  = 1    