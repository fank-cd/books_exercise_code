

# 数字金字塔


# 记忆搜索法
pyramid = [
    [13],
    [11, 8],
    [12, 7, 26],
    [6, 14, 15, 8],
    [12, 17, 13, 24, 11]
]

info = {}
max_value = 0
def search_max(depth,y):
    if depth == 4:
        return pyramid[depth][y]
    # 把下方的值交给下一个人得到最大值
    
    left_max = search_max(depth+1,y)
    # 把右下方的值交给下一个人得到最大值
    right_max = search_max(depth+1,y+1)
    if "{}_{}".format(depth,y) in info:
        return info["{}_{}".format(depth,y)]
    else:
        # 1、任务可以下分  2、最优子结构 3、决策问题
        max_value = pyramid[depth][y] +max(left_max,right_max)
        info["{}_{}".format(depth,y)]  = max_value
        return max_value

if __name__ == "__main__":
    # search(1, 0, 0)
    # l = [
    #     [13, 8, 7, 15, 13],
    #     [13, 8, 7, 15, 24],
    #     [13, 8, 26, 15, 13],
    #     [13, 8, 26, 15, 24],
    #     [13, 8, 26, 8, 24],
    # ]

    print(search_max(0,0))
    print(info)
    # a = lambda x,l: 1 for x in l
    # a()
    # sum_ = max(l, key=lambda x: sum(x))
    # print(sum_)
    # print(sum(sum_))