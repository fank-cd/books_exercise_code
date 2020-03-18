# 面试tips：
# 如果面试题是要求在排序的数组（或者部分排序的数组）中查找一个数字
# 或者统计某个数字出现的次数，那么我们都可以尝试用二分查找算法。
# 面试官会经常要求应聘者比较插入排序、冒泡排序、归并排序、快速排序
# 等不同算法的优劣。强烈建议应聘者再准备面试的时候，一定要对各种
# 排序算法的特点烂熟于心，能够在额外空间消耗、平均时间复杂度和最差
# 时间复杂度等方面去比较他们的优缺点。需要特别强调的是，很多公司的面试官
# 喜欢在面试环节要求应聘者写出快速排序的代码。可以自己写一个来实现



# 快速排序：在数组中选择一个数字，接下来把数组中的数字分为两部分，比
# 选择的数字小的数字，移到数组的左边，比选择的数字大的数字移到数组的右边

# coding:utf-8

# 基准值的选择非常影响快排的效率

def quicksort(array):
    if not isinstance(array,list):
        return None
        
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


# print (quicksort([10, 5, 2, 3]))

# 二分要求列表有序，返回的是元素的索引
# 二分查找是不断查找中间位置的值和要查找的值做比较，
# 不断调整猜测地范围来调整中间值
# 复杂度 O(logn)

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    # low和high表明查找范围

    while low <= high:
        # 只要范围没有缩小到只包含一个元素
        mid = (low+high)//2  # 中间位置
        guess = list[mid]  # 猜测的元素
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# print (binary_search([1,2,3,8,9,10],2))




# 面试题11：旋转数组的最小数字
# 题目:把一个数组最开始的若干元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，
# 数组[3,4,5,1,2]为[1,2,3,4,5]的一个旋转，该数组的最小值为1

def Min(numbers,length):
    if not isinstance(numbers,list) or len(numbers) <=0:
        return None

    index1,index2 = 0,length-1
    index_mid = index1

    while(numbers[index1]>=numbers[index2]):
        if index2 - index1 == 1: # 跳出条件
            index_mid = index2
            break
        index_mid = (index1+index2) //2
        # 如果index1、index2、index_mid 指向的三个数字想等。
        # 则只能顺序查找
        if numbers[index1] == numbers[index2] and numbers[index_mid]== numbers[index1]:
            return min(numbers)

        if numbers[index_mid] >= numbers[index1]:
            index1 = index_mid
        elif numbers[index_mid] <= numbers[index2]:
            index2 = index_mid

    return numbers[index_mid]


print(Min([3,4,5,1,2],5))

"""
这段代码思路更清晰，同样使用二分法。
numbers[mid]和numbers[high] 比较，如果numbers[mid]更大，那么mid是在左侧递增的序列上
所以答案的值是在 [mid,high]的左右闭区间内，所以 low = mid+1

反之更小，则在右侧递增序列上，那么区间是[low,mid]之间，所以high = mid
而相等的时候，high = high -1
而low = high 的时候，返回numbers[low]就ok了
"""

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low,high = 0,len(numbers)-1

        while low<high:
            mid = (low+high) //2
            if numbers[mid] > numbers[high]:
                low = mid + 1 
            elif numbers[mid] < numbers[high]:
                high = mid
            else:
                high = high -1
        return numbers[low]

