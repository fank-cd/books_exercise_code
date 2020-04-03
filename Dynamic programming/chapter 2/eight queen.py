# 经典的八皇后问题
# 回溯法

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],

]


def can_place(x, y):
    """
    判断x，y坐标能否放皇后
    """
    # 判断x行是否有皇后(感觉其实没有必要。)
    for i in range(0, y):
        if board[x][i] == 1:
            return False
    # 判断y列是否有皇后
    for i in range(0, x):
        if board[i][y] == 1:
            return False
    # 同一对角线的xy的和是一样的
    # 判断斜线(/)方向是否有皇后
    for i in range(0, x):
        if x + y - i <= 7:  # x+y-i 等于需要判断的其他地方的坐标的y值
            if board[i][x+y-i] == 1:  # 这里实际上在判断 [i] [x+y-i]的坐标有没有被占用
                # 可以想象成，x+y=i,m。其中x，y是当前判断的左边，i,m是需要遍历的对角线坐标
                # 因为同一对角线的横从坐标的和是一样的，所以m = x+y -i 所以这里是这样判断的
                return False

    # 判断反斜线(\)方向是否有皇后
    for index, i in enumerate(range(x-1, -1, -1), start=1):  # 左闭右开
        s_y = y - index
        if s_y >= 0:
            if board[i][s_y] == 1:
                return False

    return True


def print_board():
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                print("□", end=' ')
            else:
                print("■", end=' ')
        print("")


def put_queen(step):
    if step == 8:
        print_board()
        print("---------------------------------")
        return
    for i in range(8):
        # 判断该位置是否能放置当前皇后
        if can_place(step, i):
            # 1、设置现场
            board[step][i] = 1
            # 2、开始递归
            put_queen(step+1)
            # 3、恢复现场
            board[step][i] = 0


if __name__ == "__main__":
    put_queen(0)
