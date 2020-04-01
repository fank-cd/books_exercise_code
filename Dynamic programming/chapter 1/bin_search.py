# 要求数据是有序的
data = [1, 7, 17, 18, 27, 29, 30, 35, 39, 41, 63, 63, 66, 67, 78, 82, 91, 92]
# 1、二分查找


def search(data_list, target):
    left, right = 0, len(data_list)-1
    while left <= right:  # 这个等于很重要

        mid = (left+right)//2
        guess = data_list[mid]
        print(data_list[left], data_list[right], guess)
        if guess == target:
            return (guess, mid)
        elif guess > target:
            right = mid - 1  # 这里-1 和下面+1 都很重要
        elif guess < target:
            left = mid + 1

# 递归法


def search2(left, right, data_list, target):
    print(left, right)
    mid = (left+right) // 2
    if left > right:
        return False
    if data_list[mid] == target:
        return (data_list[mid], mid)
    elif data_list[mid] < target:
        return search2(mid+1, right, data_list, target)
    elif data_list[mid] > target:
        return search2(left, mid-1, data_list, target)


if __name__ == "__main__":
    print(search2(0, len(data)-1, data, 100000))
