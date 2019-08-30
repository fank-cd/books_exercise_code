"""
题目：求斐波那契数列的第N项
写一个函数，输入n，求斐波那契数列的第n项。斐波那契数列的定义如下：
     0  n=0
fn = 1  n=1
     f(n-1) + f(n-2) n >1


"""

# 递归写法：
# 这种写法很慢，很慢，会有一些重复的计算过程。而且还容易造成栈溢出
def fib(num):
    if not isinstance(num,int):
        return None
    if num<=0:
        return 0
    if num == 1:
        return 1
    
    return fib(num-1) + fib(num-2)

