# 我们正在编写一个类，但是想让用户能够以多种方式创建实例，而不局限于__init__()提供的这一种
# 这种情况，应该使用类方法

import time


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

# 也许你觉得能使用这种方法，但你看看，实际使用的时候，非常不清晰，例如


# class Date:
#     def __init__(self, *args):
#         if len(args) == 0:
#             t = time.localtime()
#             args = (t.tm_year, t.tm_mon, t.tm_mday)
        
#         self.year,self.month,self.day = args
    

# 使用的时候如何呢，
# a = Date(2012, 12, 2)
##  b = Date()  #  ?? 这是在干嘛？？
##c = Date.today()  # 是不是清晰明了多了

if __name__ == '__main__':
    a = Date(2012, 12, 2)
    b = Date.today()
