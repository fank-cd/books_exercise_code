# 投资分配
# 一共60w元，分配给四个人，下表是四个人拿n*10 w元时候的利润
values = [
    [0, 20, 50, 65, 80, 85, 85],
    [0, 20, 40, 50, 55, 60, 65],
    [0, 25, 60, 85, 100, 110, 115],
    [0, 25, 40, 50, 60, 65, 70],
]


# # 老三
# pre_max = [0]
# for i in range(10, 61, 10):
#     # i代表老三假设手中有i万元
#     values_list = []
#     for j in range(0,i+1,10):
#         values_list.append(values[3][int(j/10)] + values[2][int((i-j)/10)])
#     pre_max.append(max(values_list))

# print(pre_max)

# # 老二
# pre_max2 = [0]
# for i in range(10, 61, 10):
#     # i代表老二假设手中有i万元
#     values_list = []
#     for j in range(0,i+1,10):
#         values_list.append(pre_max[int(j/10)] + values[1][int((i-j)/10)])
#     pre_max2.append(max(values_list))

# print(pre_max2)

# # 老大
# pre_max3 = [0]
# for i in range(10, 61, 10):
#     # i代表老大假设手中有i万元
#     values_list = []
#     for j in range(0,i+1,10):
#         values_list.append(pre_max2[int(j/10)] + values[0][int((i-j)/10)])
#     pre_max3.append(max(values_list))

# print(pre_max3)

pre_max = values[len(values)-1]
for k in range(len(values)-1, -1, -1):
    new_pre_max = [0]
    for i in range(10, 61, 10):
        values_list = []
        for j in range(0, i+1, 10):
            values_list.append(pre_max[int(j/10)] + values[k-1][int((i-j)/10)])
        new_pre_max.append(max(values_list))
    pre_max = new_pre_max
print(pre_max)
