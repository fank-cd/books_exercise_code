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
时间复杂度 O(n) 但空间复杂度O(n)。
再思考：字典的内存占用比数组大很多，既然存的是数字，可以用数组的下标来
代替字典的键，比如l[0]的数字就必定为0,l[1]必定为1


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


# if __name__ == "__main__":
#     print(findDuplicate([2, 3, 1, 0, 2, 5, 3]))


"""
不修改数组找出重复的数字
在一个长度为N+1的数组里的所有数字都在1~N的范围内。所以数组中至少有一个数字是重复的，
请找出任意一个重复的数字，但不能修改输入的数组。
例如，如果输入长度为8的数组[2,3,5,4,3,2,6,7]，那么对应的输出
是重复的数字2或者3
"""

"""
思路1：创造n+1的辅助数组，数字m放到对应下标m的位置。需要O(n)的辅助空间

思路2：我觉得思路更有意思，因为是长度N+1,范围1-N,所以 1-middle 中间只能有middle
个数字，如果大于middle，则有重复的。就继续在这个范围内缩小范围。
比如1-4的数字范围内，去找数组中有1-4的数字，1,2,3,4这四个数字出现的次数为5，
所以有重复数字。再继续1-4一分为二，1-2出现了两次，符合规则，3-4出现了三次，
就一定有一个数字重复了。
 
这个代码非常有意思，明明有点二分的意思，但写出来又像是划窗。
时间复杂度O(nlogn)，空间复杂度为O(1)。但是这个算法不能保证找出所有重复的数字
"""

def coutRange(numbers,start,middle):
    """
    计算范围内的数字，在数组中出现的次数
    """
    count = 0
    for i in numbers:
        if i >= start and i <= middle:
            count +=1
    return count


def findDuplicate2(numbers:list,length:int) -> int:
    if not isinstance(numbers, list) or len(numbers) <= 0:  # 检查输入
        return False
    start = 1
    end = length -1
    while end >= start:
        middle = (start+end) // 2
        count = coutRange(numbers,start,middle)

        if end == start:
            if count >1:
                return start
            else:
                break
        if count>(middle-start+1):  # 此范围内 start-middle 中有重复数字
                end = middle
        else:
            start =  middle +1  # 范围内没有重复数字，则找数组右侧

    return -1

print(findDuplicate2([2,3,5,4,3,2,6,7],8))