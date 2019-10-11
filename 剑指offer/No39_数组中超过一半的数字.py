# 题目：数组中有一个数字出现的次数超过数组长度的一半，
# 请找出这个数字。例如，输入一个长度为9的数组[1,3,2,2,2,5,4,2]。
# 由于数字2数组中出现了5次，超过数组长度的一半，因此输出2。

# 思路1：Partition 算法排序后，这个数字一定位于中间


def find_more_than_half_num2(array):
    if not isinstance(array, list) or len(array) == 0:
        return

    result = array[0]
    count = 1
    for i in range(1, len(array)):
        if count == 0:
            result = array[i]
            count = 1
        elif result == array[i]:
            count += 1
        else:
            count -= 1

    if not check_more_than_half(array, result):
        return
    return result

def check_more_than_half(array, target):
    count = 0
    for x in array:
        if x == target:
            count += 1
    return count > len(array) / 2

if __name__ == "__main__":
    print(find_more_than_half_num2([1, 2, 3, 2, 2, 2, 5, 4, 2]))