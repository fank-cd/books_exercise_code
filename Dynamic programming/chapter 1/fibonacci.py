# 斐波那契数列
# 1、1、2、3、5、8、13、21、34后面的数都等于前面的数的和

# 递归方式


def fib(k):
    if k == 1 or k == 2:
        return 1
    return fib(k-1) + fib(k-2)


# 非递归方式
def fib2(k):
    # 求解k个数的值
    assert k > 0
    k_1 = 1
    k_2 = 1
    for i in range(3,k+1):
        k_1,k_2 = k_1+k_2,k_1
        # tmp = k_1
        # k_1 = k_1 +k_2
        # k_2 = tmp
    return k_1


if __name__ == "__main__":
    print(fib(7))
    print(fib2(7))
     

