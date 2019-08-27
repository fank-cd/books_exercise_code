"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增
的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否
含有该整数

1 2 8 9
2 4 9 12
4 7 10 13
6 8 11 15

思路：正常思路是去依次遍历，但是存在的问题是。如果当前数比需要查找数小，
则会在当前数的左上方，反之则在右下方，存在两种选择。
如果以最右上角的数为当前数，可以规避这个问题。如果比右上角数大，则在下方
如果比右上角数小，则在左方。
"""

def find(matrix:list,rows:int,columns:int,number:int) ->bool:
    found = False
    if (matrix and rows > 0  and columns > 0):
        row = 0
        column = columns -1 # 最右上角数的位置

        while row < rows and column >0:
            # print(matrix[row][column])
            if matrix[row][column] == number:
                found = True
                break
            elif matrix[row][column] > number: # 比目标数小，则找上一列
                column -= 1
            else:
                row += 1  # 比目标数大，则找下一行
    return found



# [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
# print(find([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3,4,3))

print(find([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],4,4,7))