# 大量的，比如百万级

class Date:
    __slots__ = ['year','month','day']
    
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        
        
# 当定义了slots属性，Python就会针对实例采用一种更加紧凑的内部表示。不再让每个实例都创建
# 一个dict字典。

# 关于slots有一个常见的误解，那就是这是一种封装工具，可以阻止 用户为实例添加
# 新的属性。尽管这是slots所带来的的副作用，但绝不是slots的原本意图