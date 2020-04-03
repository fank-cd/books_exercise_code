# 全排列问题
# 回溯法

data_list = [1,2,3]
arrages = []
def search(depth,datas):
    if depth == len(data_list) +1:
        print(arrages)

    else:
        for data in datas:
            # 1、设置现场
            arrages.append(data)
            # 2、递归
            next_datas = datas[:]
            next_datas.remove(data)
            search(depth+1,next_datas)
            # 3、恢复现场
            arrages.pop()

if __name__ == "__main__":
    search(1,data_list)
