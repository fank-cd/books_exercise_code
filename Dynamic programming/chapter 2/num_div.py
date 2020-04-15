# num = 7
# 1 + 1 + 1+ 1+ 1 +1 +1
# 给一个数，求该数的所有可能的数之和

datas = []
res = []


def search(rest):
    if rest <= 0:
        res.append(datas[:])

    else:
        for i in range(1, rest + 1):
            # 1、设置现场
            datas.append(i)
            # 2、递归
            search(rest-i)
            # 3、恢复现场
            datas.pop()


search(7)
print(res)
