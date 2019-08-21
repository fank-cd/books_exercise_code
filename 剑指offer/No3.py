"""
找出数组中重复的数字
在一个长度为N的数组里的所有数字都在0~N-1的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个
重复的数字。例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，那么对应的输出
是重复的数字2或者3
"""

"""
解决思路1：
将数组排序后找重复数字。排序一个长度为N的数组需要
时间复杂度 O(nlogn)

解决思路2：
遍历一次，用字典存储没有出现过的数字，出现过则重复。
时间复杂度 O(n) 但空间复杂度O(n)


解决思路3：
排序后的数组的下标和值是对应的，如果有重复的数字，则同一个下标会有重复
的数字。我们可以边交换值到对应的下标位置（有点像排序），一边遍历。如果
有重复的则会发生碰撞
时间复杂度 O(n) 但空间复杂度O(1)
"""


def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not isinstance(nums, list) or len(nums) <= 0:  # 检查输入
        return False
    for i in nums:
        if not isinstance(i, int) or i >= len(nums) or i < 0:  # 检查列表值正确
            return False

    for i in range(len(nums)):
        while nums[i] != i:  # 下标和值不对应
            if nums[i] == nums[nums[i]]:
                return nums[i]
            # nums[i], nums[nums[i]] = nums[nums[i]],nums[i]
            # 顺序不同会影响结果，需要注意
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return False


if __name__ == "__main__":
    print(findDuplicate([2, 3, 1, 0, 2, 5, 3]))


