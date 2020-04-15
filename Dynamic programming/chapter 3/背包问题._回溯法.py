# 通过回溯法求解0-1背包问题

info  =[
    [3,8],
    [2,5],
    [5,12]
]

data = []
def search(depth,rest):
    if depth == 3:
        print(data)
    else:
        # 1、不放
        data.append(0)
        search(depth+1,rest)
        data.pop() 
        
        # 2、 放
        if rest >= info[depth][0]:
            data.append(1)
            search(depth+1,rest-info[depth][0])
            
            data.pop()


if __name__ == "__main__":
    search(0,5)