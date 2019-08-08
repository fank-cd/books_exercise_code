# coding:utf-8

# 给一串数、和一个数，要求返回这一串数字能不能加起来等于给出的单独的那个数
# 返回Ture或者False

# arr 3, 34, 4, 12, 5, 2
# sum 9


arr = [3, 34, 4, 12, 5, 2]
sum = 9
leng = len(arr)
subset = [[0 for x in range(sum)] for y in range(leng)]

subset[:] = True
