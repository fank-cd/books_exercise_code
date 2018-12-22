
# 从任意长度的可迭代对象中分解元素

def drop_first_last(grades):
    first, *middle, last= grades
    return middle



print(drop_first_last([1,2,3,4,5]))  # [2,3,4]