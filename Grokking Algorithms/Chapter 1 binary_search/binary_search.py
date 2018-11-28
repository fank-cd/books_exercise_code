# coding:utf-8

# 二分要求列表有序，返回的是元素的索引
# 二分查找是不断查找中间位置的值和要查找的值做比较，不断调整猜测地范围来调整中间值
# 复杂度 O(logn)

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    # low和high表明查找范围

    while low <= high:
        # 只要范围没有缩小到只包含一个元素
        mid = (low+high)/2  # 中间位置
        guess = list[mid]  # 猜测的元素
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print binary_search([1,2,3,8,9,10],2)

