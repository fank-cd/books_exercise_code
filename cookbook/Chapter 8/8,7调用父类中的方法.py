"""
super()表示从当前类中的MRO列表中（实际不是列表，是元组，因为只读）
读取下一个基类去搜索

有一些规则：
1、确保在继承体系中所有同名的方法都有可兼容的调用签名（即参数数量相同，参数名称相同）
2、确保顶层的类实现了这个方法通常是个好主意
"""

class A:
    def spam(self):
        print("A,spam")
        
        
class B(A):
    
        
    def spam(self):
        print("B.spam")
        super().spam() 

if __name__ == '__main__':
    b = B()
    b.spam()
    
    
