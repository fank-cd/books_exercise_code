# 动态规划
# 题目：给你一根长度为n的绳子，请把绳子剪成m段(m,n都是整数,并且均大于1)
# 每段绳子的长度记为k[0],k[1],k[2]...k[m]。请问k[0]*k[1]*k[2]...*k[m]
# 可能的最大乘积是多少？例如，当绳子的长度为8时，我们把它剪成长度为2，3，3
# 的三段，此时的道德最大乘积为18

def max_solution(n):
    if n<2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    products = []
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3


    for i in range(4, n + 1):
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if product > products[i]:
                products[i] = product
    return products[n]
