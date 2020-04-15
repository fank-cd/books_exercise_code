# 数字金字塔

# 动态规划
# 自底向上

pyramid = [
    [13],
    [11, 8],
    [12, 7, 26],
    [6, 14, 15, 8],
    [12, 17, 13, 24, 11]
]


if __name__ == "__main__":
    for j in range(4, 0, -1):
        for i in range(j):
            pyramid[j-1][i] += max(pyramid[j][i],pyramid[j][i+1])

print(pyramid)
