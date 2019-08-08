# 保存有限的历史记录
# 当匹配成功时，输出匹配结果和之前不匹配的结果（但是只能输出不匹配结果的前五样
from collections import deque

def search(lines,pattern,histroy=5):
    previous_line = deque(maxlen=histroy)
    for line in lines:
        if pattern in line:
            yield line, previous_line
        previous_line.append(line)


if __name__ == '__main__':
    with open("./somefile.txt") as f:
        for line, prelines in search(f, "python", 5):
            for pline in prelines:
                print(pline, end="")
            print(line,end="")
            print("-"*20)
