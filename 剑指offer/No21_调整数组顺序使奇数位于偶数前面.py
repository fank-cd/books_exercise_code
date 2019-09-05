# 面试题21：调整数组顺序使奇数位于偶数前面
# 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

# 思路：维护两个指针，第一个指针初始化时指向数组的第一个数字，
# 它只向后移动；第二个指针初始化时指向数组的最后一个数字，
# 它只向前移动。在两个指针相遇之前，第一个指针总是位于第二个指针的前面。
# 如果第一个指针指向的数字是偶数，并且第二个指针指向的数字是奇数，则交换
# 两个数字。

# 进阶：可以把判断的逻辑变成一个函数，用一个单独的函数
# 来判断数字是不是符合标准，这样可以将函数解耦。


def reorder(nums,target_func):
    if not isinstance(nums,list) or len(nums) == 0:
        return None
    for num in nums:
        if not isinstance(num,int):
            return None
    
    left = 0
    right = len(nums) - 1
    while left < right:
        while left < right and not target_func(nums[left]):
            left += 1
        while left < right and target_func(nums[right]):
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]


def is_even(num):
    """
    解耦
    """
    return (num & 1 ) == 0  # 位运算比除余更好 奇数为1，负数为0


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    reorder(nums=nums, target_func=is_even)
    print(nums)