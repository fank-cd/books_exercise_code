#coding:utf-8

# O(n^2)
# 选择排序是不断去查找列表中最小值，第一次找最小值，交换位置，第二次找次小值，交换位置。
# 这里使用了新的列表，实际可能不需要新的空间


def findSmall(arr):
    smallest = arr[0]  # 存储最小值，默认为列表第一位
    smallest_index = 0  # 存储最小值的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmall(arr)
        newArr.append(arr.pop(smallest))  # 找出列表中最小值，并加入新数组中然后从原数组中删去

    return newArr


l = [5, 7, 2, 1, 3]
print selectionSort(l)
