# 题目：输入n个整数，找出其中最小的k个数。
# 例如，输入，4,5,1,6,2,7,3,8,则最小的4个数字是1,2,3,4

# 思路1：最容易想到的就是排序后找前面k个数。复杂度是O(nlogn),
# 不过还有更快的办法

# 思路2：时间复杂度为O(n)的算法，只有当我们可以修改输入的数组时
# 可以用

# 从面试题39得到启发，我们同样可以基于Partition函数来解决这个问题，
# 如果基于数组的第k个数字来调整，则使得比第k个数字小的所有数字都
# 位于数组的左边，比第k个数字大的所有数字都位于数组的右边。

# 思路3：直接堆排序，return heapq.nsmalest(arr,k) 这样可以
# 刚刚那样的问题在于，python是最小堆，所以需要把全部元素都堆排序，并且修改原来的数组
# 我们可以将元素变为负数，比较的时候再负负得正，这样可以实现一个最大堆
# 再去比较剩下的元素，如果比堆顶的元素小，则弹出再push
#
#  代码如下

# def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#     if k == 0:
#         return list()

#     hp = [-x for x in arr[:k]]
#     heapq.heapify(hp)
#     for i in range(k, len(arr)):
#         if -hp[0] > arr[i]:
#             # heapq.heappop(hp)
#             # heapq.heappush(hp, -arr[i])
#             heapq.heapreplace(hp,-arr[i]) # 这样比弹出再pushpush更快
#     ans = [-x for x in hp]
#     return ans

import random


def partitaion(array,start,end):
    if not isinstance(array,list) or not isinstance(start,int) \
        or not isinstance(end,int) or start<0 or end> len(array) -1:

        return None

    pivot = random.randint(start,end)
    array[pivot],array[start], = array[start],array[pivot]
    
    left = start + 1
    right = end
    while True:
        while left <= right and array[left] < array[start]:
            left +=1
        while left <= right and array[right] > array[start]:
            right -=1

        if left > right:
            break
        array[left], array[right] = array[right],array[left]

    array[start], array[right] = array[right], array[start]

    return right



def get_least_numbers1(array, k):
    if not isinstance(array, list) or len(array) == 0 \
        or not isinstance(k, int) or k <= 0 or k > len(array):
        return

    start = 0
    end = len(array) - 1
    index = partitaion(array, start, end)
    while index is not None and index != k - 1:
        if index > k - 1:
            end = index - 1
        else:
            start = index + 1
        index = partitaion(array, start, end)

    if index is None:
        return

    for i in range(k):
        print(array[i], end=" ")
    print()


def get_least_numbers2(array, k):
    import heapq

    max_heap = []
    for x in array:
        heapq.heappush(max_heap, -x)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    for x in max_heap:
        print(-x, end=" ")
    print()


if __name__ == "__main__":
    get_least_numbers1([4, 5, 1, 6, 2, 7, 3, 8], 4)