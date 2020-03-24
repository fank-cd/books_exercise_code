# coding:utf-8

# 基准值的选择非常影响快排的效率
# 快排最好的情况是，每次正好中分，复杂度为O(nlogn)。最差情况，复杂度为O(n^2)，退化成冒泡排序

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


print (quicksort([10, 5, 2, 3]))
