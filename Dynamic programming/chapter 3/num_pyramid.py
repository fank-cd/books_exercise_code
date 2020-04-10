# 数字金字塔

# 回溯法

pyramid = [
    [13],
    [11, 8],
    [12, 7, 26],
    [6, 14, 15, 8],
    [12, 17, 13, 24, 11]
]
datas = [13]


def search(depth, x, y):
    if depth == 5:
        print(datas)
    else:
        # 选择下方的值，从上往下
        datas.append(pyramid[depth][y])
        search(depth+1, x+1, y)
        datas.pop()

        # 限制右下方的值
        datas.append(pyramid[depth][y+1])
        search(depth+1, x+1, y+1)
        datas.pop()


if __name__ == "__main__":
    search(1, 0, 0)
    l = [
        [13, 8, 7, 15, 13],
        [13, 8, 7, 15, 24],
        [13, 8, 26, 15, 13],
        [13, 8, 26, 15, 24],
        [13, 8, 26, 8, 24],
    ]
    # a = lambda x,l: 1 for x in l
    # a()
    sum_ = max(l, key=lambda x: sum(x))
    print(sum_)
    print(sum(sum_))