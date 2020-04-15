# 通过回溯法求解0-1背包问题

info  =[
    [3,8],
    [2,5],
    [5,12]
]

selects = []
mem = {}
def search(depth,rest):
    if "{}_{}".format(depth,rest) in mem:
        return mem["{}_{}".format(depth,rest)]
    # 放还是不放 决策问题
    if depth >= 2:
        data =info[depth][1] if rest >= info[depth][0] else 0
    else:
        # 1\ 分任务
        values = []

        values.append(search(depth+1,rest))
        
        if rest >= info[depth][0]:
            values.append(search(depth+1, rest-info[depth][0]) + info[depth][1])
        # 2\ 选最大
        data = max(values)
    if "{}_{}".format(depth,rest) not in mem:
        mem["{}_{}".format(depth,rest)] = data
    return data
if __name__ == "__main__":
    print(search(0,5))
    print(mem)