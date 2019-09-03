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

    products = [0 for _ in range(n + 1)]
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3


    for i in range(4, n + 1):
        for j in range(1, i // 2 + 1):
            product = products[j] * products[i - j]
            if product > products[i]:  # 得到products[i]的最优解
                products[i] = product
    return products[n]

print(max_solution(8))

# 贪婪法
# 如果我们按照如下的策略来剪绳子，则得到的各段绳子的长度的乘积
# 将最大；当n大于等于5时，我们尽可能多地剪长度为3的绳子；当剩下的绳子
# 长度为4时；把绳子剪成两端长度为2的绳子。这种思路对应的代码如下：

# 当n 大于等于5的时候，我们可以证明2(n-2) > n 并且3(n-3)>n。也就是
# 说，当绳子剩下的长度大于或者等于5的时候，我们就把它剪成3或者2的绳子
# 段。另外，当n大于等于5时候，3(n-3)>=2(n-2)。所以我们应该尽可能地多
# 剪长度位3的绳子段。

def max_product_after_cuting2(length):
    """
    贪婪法
    时间 O(1)，空间O(1)
    """
    if not isinstance(length, int):
        return

    if length < 2:
        return 0

    if length == 2:
        return 1

    if length == 3:
        return 2

    times_of_3 = length // 3
    if (length - 3 * times_of_3) == 1:
        times_of_3 -= 1

    times_of_2 = (length - 3 * times_of_3) / 2
    return int((3 ** times_of_3) * (2 ** times_of_2))
