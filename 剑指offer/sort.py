# @Time : 2019/12/5 10:20
# @Author : 付楷峰
# @Function : details
from timeit import Timer
from random import randint


def generateRandomArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr


def bubbleSort_dev(alist):
    n = len(alist)
    exchange = False
    for i in range(n):
        for j in range(n):
            if alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
                # print(alist)
                exchange = True
        if not exchange:
            break

    return alist


def bubbleSort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(n):
            if alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


def isSorted(alist):
    for i in range(0, len(alist) - 1):
        if alist[i] > alist[i + 1]:
            return False
    return True


def testSort(func, alist):
    alist = func(alist)
    assert isSorted(alist), "排序算法错误\n"


if __name__ == '__main__':
    # l = [5, 4, 7, 2, 8]
    # l = generateRandomArray(100, 1, 100)
    # l =[i for i in range(1000)]
    #
    # t1 = Timer('testSort(bubbleSort, l)', 'from __main__ import testSort, bubbleSort, l')
    # t2 = Timer('testSort(bubbleSort_dev, l)', 'from __main__ import testSort, bubbleSort_dev, l')
    # print('冒泡排序算法：%s s' % t1.timeit(number=100))
    # print('改进冒泡排序算法：%s s' % t2.timeit(number=100))
    nums = [1, 3, 4, 2, 2]
    for i in range(1, len(nums) + 1):
        while nums[i - 1] != i:  # 下标和值不对应
            if nums[i - 1] == nums[nums[i - 1]]:
                print(nums[i - 1])
            # nums[i], nums[nums[i]] = nums[nums[i]],nums[i]
            # 顺序不同会影响结果，需要注意
            nums[nums[i - 1]], nums[i - 1] = nums[i - 1], nums[nums[i - 1]]
    # return False
