

# 混乱代码：

with open('/etc/password') as f:
    while True:
        line = next(f,"")
        if not line.startwith('#'):
            break
# 优雅方案：

from itertools import dropwhile
with open("/etc/passwd") as f:
    for line in dropwhile(lambda line: line.startwith("#"),f):
        print(line,end="")